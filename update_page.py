import datetime
import os

# 获取当前时间
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC") # 使用 UTC 时间

# 定义新的 HTML 内容 (可以根据需要读取模板文件等)
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>我的网站</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>欢迎来到我的网站！</h1>
    <p>这里的内容由 Python 定时更新。</p>
    <p id="update-time">上次更新时间: {now}</p>
    <p>这是一个由 Python 脚本在 GitHub Actions 中自动生成的时间戳。</p>
</body>
</html>
"""

# 获取脚本所在的目录，确保 index.html 在同一目录下
script_dir = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(script_dir, 'index.html')

# 将新内容写入 index.html
try:
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Successfully updated {html_file_path} at {now}")
except Exception as e:
    print(f"Error writing to {html_file_path}: {e}")
    exit(1) # 出错时退出，Action 会知道失败