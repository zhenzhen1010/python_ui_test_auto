'''
关键字驱动思想：参考Robotframework【RF】工具
关键字的封装
    -点击关键字：click_ele()
    -输入关键字：fill_text()
    -js操作关键字：
    -获取文本关键字：
    -断言关键字：
    -上传文件关键字：
'''
from playwright.sync_api import expect
from loguru import logger
import allure


class BasePage:
    # 初始化一个page对象--设置实例属性
    def __init__(self, page):
        self.page = page

    # 点击关键字
    def click_ele(self, loc, iframe_loc=None):
        '''
        如果本页面元素直接点击，如果是iframe子页面，要定位到iframe
        :param page: 页面对象
        :param loc: 要点击的元素定位
        :param iframe_loc: 判断是否有iframe子页面 默认没有
        :return: None 不需要返回值
        '''
        logger.info("----------start 进入方法click_ele-------------")
        if iframe_loc:  # iframe元素定位非空，先进行iframe元素定位
            logger.info(f"-----有iframe子页面：{iframe_loc},先定位iframe元素")
            self.page.frame_locator(iframe_loc).locator(loc).first.click()
            logger.info(f"------end 点击iframe_loc下，元素{loc}------------")
        else:  # 没用iframe子页面 直接进行点击操作
            # 处理多个元素时的点击，默认都选择第一个
            loc_list = self.page.locator(loc).all()
            if len(loc_list) > 1:
                loc_list[1].click()
            else:
                loc_list[0].click()
            logger.info(f"------end 点击元素{loc}------------")

    # 输入关键字
    def fill_text(self, loc, text, iframe_loc=None):

        logger.info("----------start 进入方法fill_text-------------")
        if iframe_loc:  # iframe元素定位非空，先进行iframe元素定位
            logger.info(f"-----有iframe子页面：{iframe_loc},先定位iframe元素")
            self.page.frame_locator(iframe_loc).locator(loc).fill(text)
            logger.info(f"------end 点击iframe_loc下，元素{loc}------------")
        else:  # 没用iframe子页面 直接进行点击操作
            self.page.locator(loc).fill(text)
            # self.page.fill(loc, text) 都可以实现，但不推荐使用，不会智能等待，容易出现元素还没加载就执行，导致报错
            logger.info(f"------end 点击元素{loc}------------")

    # 获取文本
    def get_text(self, loc, iframe_loc=None):
        logger.info("----------start 进入方法get_text-------------")
        if iframe_loc:  # iframe元素定位非空，先进行iframe元素定位
            logger.info(f"-----有iframe子页面：{iframe_loc},先定位iframe元素")
            text = self.page.frame_locator(iframe_loc).locator(loc).inner_text()
        else:  # 没用iframe子页面 直接进行点击操作
            text = self.page.locator(loc).inner_text()
        logger.info(f"------end 元素：{loc}，返回值{text}------------")
        return text

    # 获取列表
    def get_list_text(self, loc, iframe_loc=None):
        logger.info("----------start 进入方法get_list_text-------------")
        if iframe_loc:  # iframe元素定位非空，先进行iframe元素定位
            logger.info(f"-----有iframe子页面：{iframe_loc},先定位iframe元素")
            text = self.page.frame_locator(iframe_loc).locator(loc).inner_text()
        else:  # 没用iframe子页面 直接进行点击操作
            # 如果存在多个值时，循环获取返回list
            result_list = self.page.locator(loc).all()
            text = []
            for el in result_list:
                text.append(el.inner_text())
        logger.info(f"------end 元素：{loc}，返回值{text}------------")
        return text

    # 获取属性
    def get_attribute(self, loc, attr_name, iframe_loc=None):
        logger.info("----------start 进入方法get_attribute-------------")
        if iframe_loc:  # iframe元素定位非空，先进行iframe元素定位
            logger.info(f"-----有iframe子页面：{iframe_loc},先定位iframe元素")
            attr = self.page.frame_locator(iframe_loc).locator(loc).get_attribute(attr_name)
        else:  # 没用iframe子页面 直接进行点击操作
            attr = self.page.locator(loc).get_attribute(attr_name)
        logger.info(f"------end 元素：{loc}，返回值{attr}------------")
        return attr

    # 窗口切换
    def switch_windows(self, context, title):
        '''
        :param context: 浏览器上下文
        :param title: 目标页面标题
        :return: 返回page对象
        '''
        logger.info("----------start 进入方法switch_windows-------------")
        pages = context.pages
        for page in pages:
            # 判断列表是否在想要操作的页面
            if title in page.title():
                logger.info(f"页面：{page}，页面标题：{title}")
                page.bring_to_front()  # 设置高亮页面
                return page
        logger.info("----------end 执行完成 switch_windows-------------")

    # 文件上传
    def upload_file(self, loc, file_path):
        # 监听下⾯的操作是否打开了⽂件上传的框
        logger.info("----------start 进入方法upload_file-------------")
        with self.page.expect_file_chooser() as fc_info:
            logger.info(f"监听页面file变更弹窗：{fc_info}")
            self.page.locator(loc).click()
            # 监听到变化则直接上传文件
            fc_info.value.set_files(file_path)
            logger.info(f"设置files：{file_path}")
            self.page.wait_for_timeout(500)
        logger.info("----------end 执行完成 upload_file-------------")

    # 判断元素是否可见
    def assert_ele_visible(self, loc, iframe_loc=None):
        logger.info("----------start 进入方法assert_ele_visible-------------")
        if iframe_loc:  # iframe元素定位非空，先进行iframe元素定位
            logger.info(f"-----有iframe子页面：{iframe_loc},先定位iframe元素")
            logger.info(f"判断元素{loc}是否可见")
            try:
                expect(self.page.frame_locator(iframe_loc).locator(loc)).to_be_visible()
                logger.info("-------assert_ele_visible 断言通过-----------")
            except AssertionError as error:
                logger.error("-------assert_ele_visible 断言失败！-------")
                allure.attach(body=self.screenshot_api(), name="失败用例截图", attachment_type=allure.attachment_type.PNG)
                raise error
        else:  # 没用iframe子页面 直接进行点击操作
            logger.info(f"判断元素{loc}是否可见")
            try:
                expect(self.page.locator(loc)).to_be_visible()
                logger.info("-------assert_ele_visible 断言通过-----------")
            except AssertionError as error:
                logger.error("-------assert_ele_visible 断言失败！-------")
                allure.attach(body=self.screenshot_api(), name="失败用例截图", attachment_type=allure.attachment_type.PNG)
                raise error

    # 判断元素是否包含
    def assert_ele_contain(self, loc, text: str, iframe_loc=None):
        logger.info("----------start 进入方法assert_ele_contain-------------")
        if iframe_loc:  # iframe元素定位非空，先进行iframe元素定位
            logger.info(f"-----有iframe子页面：{iframe_loc},先定位iframe元素")
            logger.info(f"判断远元素{loc}，是否包含{text}信息")
            try:
                expect(self.page.frame_locator(iframe_loc).locator(loc)).to_contain_text(text)
                logger.info("-------assert_ele_contain 断言通过-----------")
            except AssertionError as error:
                logger.error("-------assert_ele_contain 断言失败！-------")
                allure.attach(body=self.screenshot_api(), name="失败用例截图", attachment_type=allure.attachment_type.PNG)
                raise error
        else:  # 没用iframe子页面 直接进行点击操作
            list = self.page.locator(loc).all()
            logger.info(f"判断远元素{loc}，是否包含{text}信息")
            for item in list:
                try:
                    expect(item).to_contain_text(text)
                    logger.info("-------assert_ele_contain 断言通过-----------")
                except AssertionError as error:
                    logger.info("-------assert_ele_contain 断言失败！-----------")
                    allure.attach(body=self.screenshot_api(), name="失败用例截图", attachment_type=allure.attachment_type.PNG)
                    raise error

    # 断言两个值是否相等
    def assert_ele_have(self, loc, text: str, iframe_loc=None):
        logger.info("----------start 进入方法assert_ele_have-------------")
        if iframe_loc:  # iframe元素定位非空，先进行iframe元素定位
            logger.info(f"-----有iframe子页面：{iframe_loc},先定位iframe元素")
            logger.info(f"判断远元素{loc}，是否包含{text}信息")
            try:
                expect(self.page.frame_locator(iframe_loc).locator(loc)).to_have_text(text)
                logger.info("-------assert_ele_have 断言通过-----------")
            except AssertionError as error:
                logger.error("-------assert_ele_have 断言失败！-------")
                allure.attach(body=self.screenshot_api(), name="失败用例截图", attachment_type=allure.attachment_type.PNG)
                raise error
        else:  # 没用iframe子页面 直接进行点击操作
            list = self.page.locator(loc).all()
            logger.info(f"判断远元素{loc}，是否包含{text}信息")
            for item in list:
                try:
                    expect(item).to_contain_text(text)
                    logger.info("-------assert_ele_have 断言通过-----------")
                except AssertionError as error:
                    logger.info("-------assert_ele_have 断言失败！-----------")
                    allure.attach(body=self.screenshot_api(), name="失败用例截图", attachment_type=allure.attachment_type.PNG)
                    raise error

    # -截图操作
    def screenshot_api(self, path=None, loc=None, full_page=False):
        if loc:  # 如果时元素截图
            pic_byte = self.page.locator(loc).screenshot(path=path)
            logger.info(f"做元素截图{loc}，截图位置在{path}")
        else:  # 否则做页面截图，窗口或者整个页面
            pic_byte = self.page.screenshot(path=path, full_page=full_page)
            logger.info(f"做页面截图，位置保存在{path}")
        return pic_byte  # 返回截图的二进制数据，方便allure附近添加
