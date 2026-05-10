'''
用例层：
    -需要调用页面层的不同的元素的操作，来组成用例的每一个步骤，形成业务流程
    -用pytest编写测试用例
登录用例步骤：
    1.点击首页的登录链接
    2.完成登录页面的登录操作
'''
from pageobject.homepage import HomePage
from pageobject.user_center_page import UserCenterPage


def test_avatar_case(page, login_fixture):
    # 点击进入个人中心
    HomePage(page).open_user_center_method()
    # 修改头像并保存
    UserCenterPage(page).modify_portrait_method(r"E:\python\py_UI自动化\data\baidu.png")

    UserCenterPage(page).assert_modify_success_tips_method()
