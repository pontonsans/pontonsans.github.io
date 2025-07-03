# update_page.py
import datetime
import shutil  # 用于文件复制
from jinja2 import Environment, FileSystemLoader

# --- 1. 配置 ---
# 定义源文件和输出文件的目录
SOURCE_DIR = 'templates'
OUTPUT_DIR = '.'  # '.' 表示当前目录，即项目根目录

# --- 2. 准备要填充到模板里的数据 ---
# 这些数据可以是动态计算的，也可以是从别的文件或API读取的
page_data = {
    'page_title': "我的动态主页",
    'welcome_message': "欢迎来到我的个人空间！",
    'build_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'skills_list': [
        "HTML & CSS",
        "JavaScript for interactivity",
        "Python for automation",
        "Jinja2 for templating"
    ],
    'github_username': 'pontonsans',
    'github_url': 'https://github.com/pontonsans'
}

# --- 3. 使用 Jinja2 渲染 HTML ---
# 设置 Jinja2 环境，告诉它去哪里找模板
env = Environment(loader=FileSystemLoader(SOURCE_DIR))
# 加载 HTML 模板文件
template = env.get_template('index.html.j2')
# 用我们的数据渲染模板，生成最终的 HTML 内容
output_html = template.render(page_data)

# 将生成的 HTML 内容写入到输出目录的 index.html 文件中
with open(f'{OUTPUT_DIR}/index.html', 'w', encoding='utf-8') as f:
    f.write(output_html)

# --- 4. 复制静态文件 (CSS 和 JS) ---
# 将源目录的 style.css 复制到输出目录
shutil.copy(f'{SOURCE_DIR}/style.css', f'{OUTPUT_DIR}/style.css')
# 将源目录的 script.js 复制到输出目录
shutil.copy(f'{SOURCE_DIR}/script.js', f'{OUTPUT_DIR}/script.js')

# --- 5. 完成 ---
print("✅ 网站构建成功！")
print(f"最终文件已生成在项目根目录: index.html, style.css, script.js")