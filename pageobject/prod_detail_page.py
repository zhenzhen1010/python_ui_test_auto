'''
商品详情页面类
'''
from common.basepage import BasePage


class ProdDetailPage(BasePage):
    # 获取商品价格元素
    prod_price_loc = '.price-box .goods-price .price'
    # 获取商品名称元素
    prod_name_loc = '.name-box .name'
    # 立即购买按钮元素
    buynow_btn_loc = '.buy-now'

    # 商品价格断言
    def assert_prod_price_method(self, text):
        self.assert_ele_contain(self.prod_price_loc, text)

    # 商品名称断言
    def assert_prod_name_method(self, text):
        self.assert_ele_contain(self.prod_name_loc, text)

    # 点击立即购买
    def buynow_btn_click(self):
        self.click_ele(self.buynow_btn_loc)