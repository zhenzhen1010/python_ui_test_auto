from common.basepage import BasePage


class ProdListPage(BasePage):

    # 商品名称元素定位
    prod_name_loc = '//div[@class="goods-name"]'

    # 商品元素定位
    prod_loc = '.list-con.normalList .item'

    #商品价格元素定位
    prod_price_loc = '.goods-price'

    # 对返回列表商品名称进行断言
    def assert_prod_name_method(self, prod_name):
        # 调用公共方法获取商品名称列表
        self.assert_ele_contain(self.prod_name_loc, prod_name)

    # 点击商品进入详情页
    def open_prod_detail_page_method(self):
        self.click_ele(self.prod_loc)

    # 获取商品价格，返回列表
    def get_prod_price_text_method(self):
        return self.get_list_text(self.prod_price_loc)

    # 获取商品名称，返回列表
    def get_prod_name_text_method(self):
        return self.get_list_text(self.prod_name_loc)