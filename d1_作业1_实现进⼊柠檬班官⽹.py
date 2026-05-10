# 导入库
from playwright.sync_api import sync_playwright

# 实例化
with sync_playwright() as pw:
    # 创建浏览器对象
    browser = pw.chromium.launch(channel="msedge",headless=False)
    # 创建浏览器上下文
    context = browser.new_context()
    # 创建页面
    page = context.new_page()
    # 打开必应网页
    page.goto("https://cn.bing.com/")
    # 选中输入框元素,并输入搜索内容
    page.locator("#sb_form_q").fill("柠檬班")
    # 回车
    page.locator("#sb_form_q").press("Enter")
    # 点击搜索
    # page.locator("#search_icon").click()
    # 点击进入官网首页
    page.locator("//div[text()='lemonban.com']/ancestor::a[@class='tilk']").click()
    page.wait_for_timeout(3000)