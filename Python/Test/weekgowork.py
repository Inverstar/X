import os
from datetime import datetime, timedelta

def update_file_content(file_path):
    """
    更新文件内容中的日期和星期。
    """
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查内容中是否包含 MMDD 占位符
    if "MMDD" not in content:
        print(f"跳过文件：{os.path.basename(file_path)}（内容中不包含 MMDD 占位符）")
        return

    # 提取文件名中的日期
    filename = os.path.basename(file_path)

    try:
        # 假设文件名格式为 "2518-0428.md"，提取 MMDD 部分
        start_date_str = filename[5:9]  # 提取 0428
        year_part = filename[:2]  # 提取 25
    except IndexError:
        print(f"文件名格式错误：{filename}")
        return

    # 将字符串转换为日期对象
    try:
        # 假设年份是 20YY（例如，25 表示 2025 年）
        year = int(f"20{year_part}")
        month = int(start_date_str[:2])
        day = int(start_date_str[2:4])
        start_date = datetime(year, month, day)
    except ValueError:
        print(f"无效的日期格式：{filename}")
        return

    # 生成周一到周日的日期和星期
    days = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d %A") for i in range(7)]

    # 替换占位符
    for i in range(14):
        placeholder = "YYYY-MM-DD dddd"
        replacement = days[i // 2]  # 每两个占位符对应一个日期和星期
        content = content.replace(placeholder, replacement, 1)

    # 处理 MMDD~MMDD 占位符
    # 计算周日的日期
    end_date = start_date + timedelta(days=6)
    week_range = f"{start_date.strftime('%m%d')}~{end_date.strftime('%m%d')}"

    # 替换 MMDD~MMDD 占位符
    content = content.replace("MMDD~MMDD", week_range)

    # 保存修改后的内容
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def batch_process_files(directory):
    """
    批量处理指定目录中的所有文件。
    """
    for filename in os.listdir(directory):
        if filename.endswith(".md") and len(filename) == 12:
            print(filename,"start")
            file_path = os.path.join(directory, filename)
            update_file_content(file_path)
            print(filename,"over")

# # 使用示例
# if __name__ == "__main__":
#     # 指定文件所在的目录
#     target_directory = "your_directory_path"  # 替换为你的文件夹路径
#     batch_process_files(target_directory)

# 使用示例
if __name__ == "__main__":
    # 指定文件所在的目录
    target_directory = "C:\\Users\\l30036344\\Documents\\Test\\weeks"  # 替换为你的文件夹路径
    batch_process_files(target_directory)
