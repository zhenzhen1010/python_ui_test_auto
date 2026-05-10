'''
商品详情测试用例
'''
from pageobject.homepage import HomePage
from pageobject.prod_list_page import ProdListPage
from pageobject.prod_detail_page import ProdDetailPage


def test_prod_detail_case(page, login_fixture):  # 调用夹具处理登录操作，不需要返回值
    search_prod_name = "圆筒包"
    # 3.调用搜索方法进行搜索
    HomePage(page).search_prod_method(search_prod_name)
    page.wait_for_timeout(1000)
    # 4.添加返回列表断言
    ProdListPage(page).assert_prod_name_method(search_prod_name)
    # 获取商品价格
    price_list = ProdListPage(page).get_prod_price_text_method()

    name_list = ProdListPage(page).get_prod_name_text_method()

    print(price_list, name_list)
    # 5.点击进入详情页
    ProdListPage(page).open_prod_detail_page_method()

    page.wait_for_timeout(1000)

    # 断言
    ProdDetailPage(page).assert_prod_price_method(price_list[1])
    ProdDetailPage(page).assert_prod_name_method(name_list[1])
