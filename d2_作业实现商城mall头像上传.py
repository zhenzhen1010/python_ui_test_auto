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
    page.goto("http://mall.lemonban.com:3344/")
    # 选中登陆元素,并点击登陆
    page.locator("//a[text()='登录']").click()
    # 选中用户名输入元素，并输入内容
    page.locator("//div[@class='item account']/input").fill("lemon_python")
    # 选中密码输入元素，并输入内容
    page.locator("//div[@class='item password']/input").fill("12345678")
    # 选中登陆按钮元素，并点击登陆
    page.locator("//a[@class='login-button']").click()
    # 点击个人中心
    page.locator("//span[text()='个人中心']").click()
    # 进入账户信息
    # page.locator("//a[text()='账户信息']").click()
    page.locator('//div[@class="portrait-box"]').hover()
    page.locator('//div[@class="edit"]').click()
    # 监听打开上传窗口
    with page.expect_file_chooser() as fc:
        page.locator("//img[@class='pic avatar']").click()
        fc.value.set_files(r"E:\python\py_UI自动化\data\baidu.png")
        page.wait_for_timeout(1000)
        # 点击保存信息
        page.locator("//a[text()='保存账户信息']").click()

    page.wait_for_timeout(3000)