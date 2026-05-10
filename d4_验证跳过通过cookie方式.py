'''
1.cookie跳过验证
    1、先登陆百度网站，-保存登录状态到文件
    2、再后面UI自动化的脚本里 支持预存储这个登录状态文件的方式打开上下文-content --直接会时登录状态
'''
# 引入playwright
from playwright.sync_api import Playwright, sync_playwright


# 第一次登录，手动验证，通过后保存状态
# def run(playwright:Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.baidu.com/")
#     page.locator("#s-top-loginbtn").click()
#     page.locator('#TANGRAM__PSP_11__changePwdCodeItem').click()
#     page.locator('#TANGRAM__PSP_11__userName').fill('13560088365')
#     page.locator('#TANGRAM__PSP_11__password').fill('Zhen@022495')
#     page.locator('#TANGRAM__PSP_11__isAgree').check()
#     page.locator('#TANGRAM__PSP_11__submit').click()
#     page.pause() # 暂停脚本运行 -- 手动去完成验证码的操作  认证完成后
#
#     # 生成并保存登录状态的存储文件
#     sto_file = context.storage_state(path="state.json")
#     print(sto_file)
#
# with sync_playwright() as pw:
#     run(pw)

# 登录后读取登录状态
def rep_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    # 初始化上下文的时候带上刚生成的登录信息存储文件，完成登录操作
    context = browser.new_context(storage_state='state.json')
    page = context.new_page()
    page.goto("https://www.baidu.com/")

    page.wait_for_timeout(4000)


with sync_playwright() as pw:
    rep_run(pw)
