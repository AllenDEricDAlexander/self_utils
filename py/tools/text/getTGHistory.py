from bs4 import BeautifulSoup
import re

# 本地HTML文件路径
# 替换为你本地文件的路径
html_file_path = r'messages1.html'

# 打开并读取本地HTML文件
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(html_content, 'html.parser')
# 提取目标内容
try:
    history_div = soup.find('div', class_='history')  # 查找class为'history'的div
    text_div = history_div.find_all('div',
                                    class_='text') if history_div else None  # 查找class为'clearfix'的div
    for element in text_div:
        if element:
            matches = re.findall(r'：([^<]+)', element.get_text(separator='<br>'))
            print(matches)
            a_tags = element.find('a')  # 获取第一个a标签
            href = a_tags.get('href')  # 提取href属性
            if href:
                print(href)  # 打印href属性值
        else:
            print("未找到指定的div标签")
except Exception as e:
    print(f"发生错误: {e}")
