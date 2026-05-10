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
import pytest

from pageobject.homepage import HomePage
from pageobject.prod_list_page import ProdListPage

@pytest.mark.p1
def test_search_prod_case(page, login_fixture):  # 调用夹具处理登录操作，不需要返回值
    search_prod_name = "圆筒包"
    # 3.调用搜索方法进行搜索
    HomePage(page).search_prod_method(search_prod_name)
    page.wait_for_timeout(1000)
    # 4.添加返回列表断言
    ProdListPage(page).assert_prod_name_method(search_prod_name)
    page.wait_for_timeout(2000)
