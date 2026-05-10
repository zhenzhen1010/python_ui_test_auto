'''
1.pytest 结合使用
    -安装pytest插件
        pip install pytest-playwright
    -自动初始化调用浏览器的操作
        -默认隐式启动
    -修改启动方式：
        脚本运行：putest --headed --browser chromium
        pytest.main(["--headed"])
    -添加配置文件：
        [pytest]
        addopts = --headed --browser firefox

2.录制脚本
    启动录制脚本功能：playwright codegen

3.cookie跳过验证
    1、先登陆百度网站，-保存登录状态到文件
    2、再后面UI自动化的脚本里 支持预存储这个登录状态文件的方式打开上下文-content --直接会时登录状态
'''
# 引入playwright
from playwright.sync_api import sync_playwright,expect

# 显式启动浏览器
def test_baidu():
    with sync_playwright() as pw:
        # 1.打开浏览器，默认无头模式，headless=False关闭无头模式
        browser = pw.chromium.launch(headless=False)
        # 2.开启上下文
        content = browser.new_context()
        # 3.创建页面
        page = content.new_page()
        # 4.打开页面访问网址
        page.goto("https://www.baidu.com")

        page.wait_for_timeout(2000)

#隐式启动浏览器
def test_implicit_baidu(page):
    page.goto("https://www.baidu.com/")
    print(page.title())


def test_codegen(page):
    page.goto("https://www.baidu.com/")
    page.locator("#chat-textarea").fill("柠檬班")
    # page.get_by_text().click()
    page.get_by_role("button", name="百度一下").click()
    expect(page.locator("#content_left")).to_contain_text("柠檬班(湖南省零檬信息技术有... - 百度百科")
