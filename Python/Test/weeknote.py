import os
from datetime import datetime, timedelta
from lunardate import LunarDate  # 使用 lunardate 库
import chinese_calendar  # 使用 chinese_calendar 库判断节气

# 农历数字转中文
def format_lunar_date(lunar_date, solar_date):
    # chinese_months = ["正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "冬月", "腊月"]
    chinese_months = ["青阳", "竹秋", "落花", "槐夏", "仲夏", "林钟", "流火", "橘春", "小雪", "霜华", "龙潜", "星回"]
    chinese_days = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
                    "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
                    "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]
    
    # 检查是否是节气
    solar_date = solar_date.date()  # 获取日期部分
    solar_term = chinese_calendar.get_solar_terms(solar_date,solar_date)
    if solar_term:  # 如果是节气
        solar_term_name = solar_term[0][1] # 获取节气名称
        return f"{chinese_months[lunar_date.month - 1]}{solar_term_name}"
    
    # 如果不是节气，返回普通农历日期
    month = chinese_months[lunar_date.month - 1]
    day = chinese_days[lunar_date.day - 1]
    return f"{month}{day}"

def process_file(filepath):

    # 读取文件内容
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    if "第 ww 周" not in content:
        print(f"文件 {filepath} 中未找到 '第 ww 周'，跳过处理。")
        return
    # 从文件名提取信息
    filename = os.path.basename(filepath)
    year = 2000 + int(filename[:2])  # 提取年份
    week_number = int(filename[2:4])  # 提取第几周
    monday_date = filename[5:9]  # 提取周一日期 (MMDD)
    
    # 计算一周的日期
    monday = datetime.strptime(f"{year}{monday_date}", "%Y%m%d")
    dates = [monday + timedelta(days=i) for i in range(7)]
    
    # 获取农历日期并格式化为“五月初五”或“四月立夏”形式
    lunar_strings = []
    for date in dates:
        lunar_date = LunarDate.fromSolarDate(date.year, date.month, date.day)
        lunar_strings.append(format_lunar_date(lunar_date, date))
    

    # 替换内容
    content = content.replace("第 ww 周", f"第 {week_number} 周")  # 替换周数
    content = content.replace("gggg", str(year))  # 替换年份
    content = content.replace("农历", lunar_strings[0], 1)  # 替换第一个农历为周一的农历
    content = content.replace("农历", lunar_strings[6], 1)  # 替换第二个农历为周日的农历
    
    # 替换表格中的农历
    for i in range(7):
        content = content.replace("农历", f"{lunar_strings[i][2:4]}", 1)
    
    # 替换周一到周日的公历和农历
    for i, date in enumerate(dates):
        content = content.replace("MMDD", f"{date.strftime('%m%d')} {lunar_strings[i][2:4]}", 1)
    
    # 写回文件
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"已处理文件：{filepath}")

def batch_process_files(directory):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(".md") and len(filename) == 12:
            print(f"正在处理文件：{filename}")
            filepath = os.path.join(directory, filename)
            process_file(filepath)

if __name__ == "__main__":
    # 指定文件所在的目录
    target_directory = "C:\\Users\\lnq12\\Documents\\obsidian\\weeks\\2025"  # 替换为你的文件夹路径
    batch_process_files(target_directory)

# if __name__ == "__main__":
#     # 指定文件所在的目录
#     target_directory = "C:\\Users\\l30036344\\Documents\\Test\\weeks\\test"  # 替换为你的文件夹路径
#     batch_process_files(target_directory)
