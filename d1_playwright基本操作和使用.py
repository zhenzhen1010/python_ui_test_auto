# 引入playwright库
from playwright.sync_api import sync_playwright
'''
方式一：需要手动打开和关闭
'''
# # 1.实例化并启动
# pw = sync_playwright().start()
# # 2.创建对应型号的浏览器，默认是无头模式（没用界面的），有头模式（有界面）设置headless=False
# # 本地打开chrome有问题
# # browser = pw.chromium.launch(channel="chrome", headless=False)
# # 打开火狐浏览器
# browser = pw.firefox.launch(channel="firefox", headless=False)
# # 3.创建上下文
# context = browser.new_context()
# # 4.在浏览器中创建新页面
# page = browser.new_page()
# # 5.并访问地址：https://www.baidu.com
# page.goto("https://www.baidu.com")
#
# page.wait_for_timeout(2000)
# # 6.手动关闭页面
# page.close()
# # 7.手动关闭浏览器
# browser.close()

'''
方式二：使用上下文管理with
'''

with sync_playwright() as pw:
    browser = pw.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context()
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    page.wait_for_timeout(2000)