'''
提交订单测试用例
'''
from pageobject.homepage import HomePage
from pageobject.prod_list_page import ProdListPage
from pageobject.prod_detail_page import ProdDetailPage
from pageobject.submit_order_page import SubmitOrderPage


def test_submit_order_case(page, login_fixture):  # 调用夹具处理登录操作，不需要返回值
    search_prod_name = "圆筒包"
    # 3.调用搜索方法进行搜索
    HomePage(page).search_prod_method(search_prod_name)
    page.wait_for_timeout(1000)
    # 4.添加返回列表断言
    ProdListPage(page).assert_prod_name_method(search_prod_name)
    # 获取商品价格
    prod_price = ProdListPage(page).get_prod_price_text_method()[1]

    prod_name = ProdListPage(page).get_prod_name_text_method()[1]

    # 5.点击进入详情页
    ProdListPage(page).open_prod_detail_page_method()

    page.wait_for_timeout(1000)

    # 断言
    ProdDetailPage(page).assert_prod_price_method(prod_price)
    ProdDetailPage(page).assert_prod_name_method(prod_name)

    # 点击购买商品，进入订单提交页面
    ProdDetailPage(page).buynow_btn_click()

    SubmitOrderPage(page).assert_prod_submit_order_method(prod_name,prod_price)

    SubmitOrderPage(page).submit_order_method()
    page.wait_for_timeout(2000)