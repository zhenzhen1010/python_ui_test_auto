'''
登录页面类
    -元素定位：类属性
    -操作方法及操作动作：实例方法
'''
from common.basepage import BasePage


class LoginPage(BasePage):
    # 登录渠道
    channel_account_loc = '//div[text()="账号登录"]'
    channel_phone_loc = '//div[text()="手机登录"]'
    # 用户名输入框
    uname_loc = '//input[@placeholder="请输入手机号/用户名"]'
    # 密码输入框
    password_loc = '//input[@placeholder="请输入密码"]'
    # 登录按钮
    login_btn_loc = '//a[@class="login-button"]'

    def login_method(self, uname, password):
        # 输入用户名
        # page.locator(self.uname_loc).fill(uname)
        self.fill_text(self.uname_loc, uname)
        # 输入密码
        # page.locator(self.password_loc).fill(password)
        self.fill_text(self.password_loc, password)
        # 点击登录按钮
        # page.locator(self.login_btn_loc).click()
        self.click_ele(self.login_btn_loc)
        # 登录完成后，因发生页面切换，运行脚本发现报错，加个强制等待
        self.page.wait_for_timeout(500)
