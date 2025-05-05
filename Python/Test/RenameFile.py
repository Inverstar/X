#RenameFile.py
import os
from datetime import datetime
#directory = "your_directory_path"
# 替换为你的文件所在目录的路径
directory = "C:\\Users\\lnq12\\Documents\\Logseq\\journals"

for filename in os.listdir(directory):
    # 检查文件名是否符合格式（例如：2024_08_18.md）
    if filename.endswith(".md") and len(filename) == 13:
        # 分离文件名和扩展名
        name, ext = os.path.splitext(filename)
        # 提取日期部分（YYYY_MM_DD）
        date_str = name  # 文件名本身是 YYYY_MM_DD 格式
        # 将下划线替换为连字符
        new_date_str = date_str.replace('_', '-')
        # 转换为日期对象
        date_obj = datetime.strptime(new_date_str, "%Y-%m-%d")
        # 获取星期几（例如：Friday）
        weekday = date_obj.strftime("%A")
        # 构造新文件名
        new_filename = f"{new_date_str} {weekday}{ext}"
        # 重命名文件
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
