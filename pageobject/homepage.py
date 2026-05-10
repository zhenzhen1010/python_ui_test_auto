'''
首页页面类
'''
from common.basepage import BasePage
from loguru import logger


class HomePage(BasePage):
    # 登录link按钮元素定位
    login_link_loc = '//a[text()="登录"]'
    # 搜索框
    search_loc = '//div[@class="search-input-box"]/input'
    # 搜索确认按钮
    search_btn_loc = '//div[@class="search-msg"]/input'
    # 个人中心的链接
    user_center_link_loc = '//span[text()="个人中心"]'
    # 欢迎来到柠檬班提示语
    welcome_tips_loc = '//span[text()="欢迎来到柠檬班"]'
    # 用户名
    uname_text_loc = '//a[@class="link-name"]'

    # 处理点击登录按钮的方法
    def click_login_link_method(self):
        logger.info("------start 处理点击登录按钮的方法------")
        # 点击按钮
        # page.locator(self.login_link_loc).click()
        self.click_ele(self.login_link_loc)
        logger.info("------end 处理点击登录按钮的方法------")
    # 处理搜索商品方法
    def search_prod_method(self, prod_name):
        logger.info("------start 处理搜索商品方法------")
        # 输入搜索的商品
        # page.locator(self.search_loc).fill(prod_name)
        self.fill_text(self.search_loc, prod_name)
        logger.info(f"输入搜索商品{prod_name}")
        # 点击搜索按钮
        # page.locator(self.search_btn_loc).click()
        logger.info(f"点击搜索按钮{self.search_btn_loc}")
        self.click_ele(self.search_btn_loc)
        logger.info("------end 处理搜索商品方法------")

    # 点击打开的个人中心页面
    def open_user_center_method(self):
        logger.info("------start 点击打开的个人中心页面------")
        logger.info(f"点击元素{self.user_center_link_loc}")
        self.click_ele(self.user_center_link_loc)
        self.page.wait_for_timeout(500)
        logger.info("------end 点击打开的个人中心页面------")

    # 断言欢迎语可见
    def assert_welcome_visible_method(self):
        logger.info("------start 断言欢迎语可见方法------")
        logger.info(f"定位元素：{self.welcome_tips_loc}")
        self.assert_ele_visible(self.welcome_tips_loc)
        logger.info("------end 断言欢迎语可见------")

    # 断言用户名正确
    def assert_uname_contain_method(self, text):
        logger.info("------start 断言用户名正确------")
        logger.info(f"定位元素：{self.uname_text_loc},比较text：{text}")
        self.assert_ele_contain(self.uname_text_loc, text)
        logger.info("------end 断言用户名正确------")
