from common.basepage import BasePage


class UserCenterPage(BasePage):
    # 编辑资料区域
    edit_profile_text_loc = '//div[@class="portrait-box"]'
    # 编辑头像元素
    portrait_loc = '//img[@class="pic avatar"]'
    # 保存账户信息
    save_info_btn_loc = '//a[text()="保存账户信息"]'
    # 修改成功提示
    success_tips_loc = '.el-message__content'

    # 封装修改头像的实例方法
    def modify_portrait_method(self, file_path):
        # 1.点击编辑资料
        self.click_ele(self.edit_profile_text_loc)
        # 2.上传文件
        self.upload_file(self.portrait_loc, file_path)

        self.page.wait_for_timeout(500)
        # 3.点击保存
        self.click_ele(self.save_info_btn_loc)
        # self.page.pause()

    # 断言是否成功
    def assert_modify_success_tips_method(self):
        self.assert_ele_visible(self.success_tips_loc)
