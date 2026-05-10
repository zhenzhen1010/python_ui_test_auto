# 引入playwright库
import time

from playwright.sync_api import sync_playwright
from common.handle_path import screenshot_path

with sync_playwright() as pw:
    browser = pw.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context()
    page = browser.new_page()
    # page.goto("https://www.baidu.com/")
    # page.goto("file:///E:/%E5%AD%A6%E4%B9%A0/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/%E6%9F%A0%E6%AA%AC%E7%8F%AD/Python%E8%87%AA%E5%8A%A8%E5%8C%96/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/alert_demo.html")
    # 双击操作
    # page.locator("#chat-textarea").dblclick()
    # 鼠标右键
    # page.locator("#chat-textarea").click(button="right")
    # 清空输入
    # page.locator("#chat-textarea").fill("123344")
    # page.wait_for_timeout(1000)
    # page.locator("#chat-textarea").clear()
    # hover
    # page.locator("//div[@class='chat-voice-input-mic-icon']").hover()

    # 单选
    # page.locator("#s-usersetting-top").hover()
    # page.locator("//span[text()='高级搜索']").click()
    # page.wait_for_timeout(1000)
    # page.locator("#q5_1").set_checked(True)
    # 复选
    # page.locator("#s-top-loginbtn").click()
    # page.wait_for_timeout(1000)
    # page.locator("#TANGRAM__PSP_11__isAgree").set_checked(True)
    # page.wait_for_timeout(1000)
    # page.locator("#TANGRAM__PSP_11__isAgree").set_checked(False)
    # page.wait_for_timeout(1000)
    # page.locator("#TANGRAM__PSP_11__isAgree").check()
    # page.wait_for_timeout(1000)
    # page.locator("#TANGRAM__PSP_11__isAgree").uncheck()
    # 下拉选择框
    # page.locator("#select").select_option(value="o4")

    # 其他类型拉下
    # page.locator("#s-usersetting-top").hover()
    # page.locator("//span[text()='高级搜索']").click()
    # page.locator("//span[text()='时间不限']").click()
    # page.locator("//p[text()='一月内']").click()

    # 滚动操作
    # page.goto("https://cn.bing.com/")
    # page.locator("#sb_form_q").fill("柠檬班")
    # page.locator("#sb_form_q").press("Enter")
    # page.wait_for_timeout(4000)
    # page.locator("//a[@aria-label='第 1 页']").scroll_into_view_if_needed()

    # 页面截图
    page.screenshot(path=f"{screenshot_path}/screenshot_{int(time.time() * 1000)}.png", full_page=True)  # 截图整个页面

    # 获取元素文本
    # print(page.locator("#chat-submit-button").inner_text())
    # 获取元素的属性
    # print(page.locator("#chat-textarea").get_attribute("class"))
    # 获取元素的value值，只有input、textarea、select可以
    # print(page.locator("#chat-textarea").input_value())

    # 多个元素
    # loc = page.locator(".title-content-title")
    # print(loc.count())
    # print(loc.all_inner_texts())
    # print(loc.first.inner_text())
    # print(loc.last.inner_text())
    # print(loc.nth(3).inner_text())

    # 文件上传【input类型】
    # page.goto("file:///E:/%E5%AD%A6%E4%B9%A0/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/%E6%9F%A0%E6%AA%AC%E7%8F%AD/Python%E8%87%AA%E5%8A%A8%E5%8C%96/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/upload_demo.html")
    # page.locator("#fu").set_input_files(r"E:\python\py_UI自动化\baidu.png")

    # 文件上传 【非input类型】
    # page.goto("https://caesium.app/")
    # # 监听下⾯的操作是否打开了⽂件上传的框
    # with page.expect_file_chooser() as fc_info:
    #     page.locator('//button[contains(text(),"浏览")]').click()
    #     # 监听到变化则直接上传文件
    #     fc_info.value.set_files(r"E:\python\py_UI自动化\baidu.png")
    #
    # page.wait_for_timeout(2000)
