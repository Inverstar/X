#tagTowiki.py
import os
import re


def replace_in_file(file_path):
    # 定义正则表达式
    pattern = r'#([^\W]+)'
    replacement = r'[[\1]]'

    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 替换内容
    modified_content = re.sub(pattern, replacement, content)

    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)


def process_folder(folder_path):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 处理文本文件（可以根据需要修改文件扩展名）
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f'Processing: {file_path}')
                replace_in_file(file_path)


# 指定要处理的文件夹路径
# my_folder_path = 'C:\\Users\\l30036344\\Documents\\Test\\weeks\\test'  # 替换为你的文件夹路径
# my_folder_path = 'C:\\Users\\l30036344\\PycharmProjects\\PythonProject'  # 替换为你的文件夹路径
# process_folder(my_folder_path)

# 指定要处理的文件夹路径
my_folder_path = 'C:\\Users\\lnq12\\Documents\\Logseq\\pages'  # 替换为你的文件夹路径
process_folder(my_folder_path)