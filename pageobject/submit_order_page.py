'''
商品详情页面类
'''
from common.basepage import BasePage
import re


class SubmitOrderPage(BasePage):
    # 获取列表商品名称元素
    prod_name_loc = '.goods-box .name'
    # 获取列表商品价格元素
    prod_price_loc = '.goods-box .unit-price'
    # 获取商品数量元素
    prod_number_loc = '.goods-box .number'
    # 获取商品总价
    prod_total_loc = '.goods-box .total'
    #获取提交订单按钮元素
    submit_order_btn_loc = 'a.btn'

    # 断言商品名称 价格 数量 总价
    def assert_prod_submit_order_method(self, prod_name, prod_price):
        self.assert_ele_contain(self.prod_name_loc, prod_name)
        self.assert_ele_contain(self.prod_price_loc, prod_price)
        num_text = self.get_text(self.prod_number_loc)
        num = int(re.findall(r'\d+', num_text)[0])

        price_text = self.get_text(self.prod_price_loc)
        price = float(re.findall(r'\d+\.\d+', price_text)[0])

        self.assert_ele_have(self.prod_total_loc, price_text)
        # total_text = self.get_text(self.prod_total_loc)
        # tottal = float(re.findall(r'\d+\.\d+', total_text)[0])
        # print(num*price == tottal)

    # 点击提交订单
    def submit_order_method(self):
        self.click_ele(self.submit_order_btn_loc)