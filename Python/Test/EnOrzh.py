#EnOrzh.py
import os
#from datetime import datetime
import re

#directory = "your_directory_path"
# 替换为你的文件所在目录的路径
directory = "C:\\Users\\l30036344\\Documents\\Test\\journals"

# 映射中文星期几到英文，以及英文到中文
weekday_mapping = {
    "星期一": "Monday",
    "星期二": "Tuesday",
    "星期三": "Wednesday",
    "星期四": "Thursday",
    "星期五": "Friday",
    "星期六": "Saturday",
    "星期日": "Sunday",
    "Monday": "星期一",
    "Tuesday": "星期二",
    "Wednesday": "星期三",
    "Thursday": "星期四",
    "Friday": "星期五",
    "Saturday": "星期六",
    "Sunday": "星期日"
}

for filename in os.listdir(directory):
    # 检查文件名是否符合格式（例如：2024-08-18 星期日.md 或 2024-08-18 Sunday.md）
    if filename.endswith(".md"):
        # 使用正则表达式匹配日期和星期几
        match = re.match(r"(\d{4}-\d{2}-\d{2})\s([a-zA-Z]+|星期[一二三四五六日])\.md", filename)
        if match:
            date_str = match.group(1)
            weekday = match.group(2)

            # 判断当前星期几是中文还是英文
            if weekday in weekday_mapping:
                # 转换为另一种语言
                new_weekday = weekday_mapping[weekday]
                # 构造新文件名
                new_filename = f"{date_str} {new_weekday}.md"
                # 重命名文件
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")

