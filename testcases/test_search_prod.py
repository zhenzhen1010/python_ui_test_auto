'''
用例层：
    -需要调用页面层的不同的元素的操作，来组成用例的每一个步骤，形成业务流程
    -用pytest编写测试用例
登录用例步骤：
    1.点击首页的登录链接
    2.完成登录页面的登录操作
商品用例步骤
    1.调用首页搜索商品方法
'''
from config.env import config
from pageobject.homepage import HomePage
from pageobject.loginpage import LoginPage


def test_search_prod_case(page):
    page.goto(config.data["base_url"])
    # 1.点击首页的登录链接,调用首页页面对象的方法
    HomePage(page).click_login_link_method()
    # 2.完成登录页面的登录操作
    LoginPage(page).login_method(config.data["username"], config.data["password"])
    page.wait_for_timeout(500)
    # 3.调用搜索方法进行搜索
    HomePage(page).search_prod_method("真皮圆筒包")
    page.wait_for_timeout(2000)
