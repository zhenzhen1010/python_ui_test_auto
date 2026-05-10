'''
1.默认等待机制：
    -默认等待时间：30s
    -对于要执行click的元素，playwroght会确保
        -元素存在
        -元素是否可见
        -元素是否稳定，即没用动画或已完成动画
        -元素接受事件，即未被其他元素遮挡
        元素是否可用
2.显性等待机制：
    等待页面处于某种状态：domcontentloaded，load，networkidle
    wait_for_load_state("xxx")
    等待元素出现
    wait_for_selector()
    等待元素消失
    wait_for_selector("",state="hidden")
    等待js函数执行完成
    wait_for_function("return document.readyState === 'complete')
    等待事件出现：等待下载事件
    wait_for_event("download")
    等待页面调整到指定的url
    wait_for_url("")
3.强制等待：
    wait_for_timeout(),如果页面元素定位没问题，但执行页面无法完全加载到，可以设置等待时间，一般设置1-2s，不适应过长
    影响用例执行时间

4.iframe页面处理
    -方法：
        先定位到iframe框架，在从iframe框架定位到里面的元素，page.frame_locator("")
    page.frames 获取页面所有iframe标签，返回列表

5.窗口切换
    获取窗口列表：context.pages # 注意：需要等待碰面加载完成
    获取最新一个窗口：pages[-1] # 窗口列表的最后一个
    page.bring_to_front() # 激活窗口

6.弹窗
    dialog: 通过page.on 监听弹窗事件，再调用里面的方法关闭，以及做其他操作，后续可能有场景会使用到

7.expect断言
    expect(目标元素).xxx_have_(期望值)
8.js操作
    需要使用page.evaluate()方法执行js代码
    例如：page.evaluate("document.getElementById('xxx').innerHTML='xxx'")
'''

# 导入库
from playwright.sync_api import sync_playwright


# 封装方法
def switch_windows(context, title):
    '''
    :param content: 浏览器上下文
    :param title: 目标页面标题
    :return: 返回page对象
    '''
    pages = context.pages
    for page in pages:
        # 判断列表是否在想要操作的页面
        if title in page.title():
            page.bring_to_front()  # 设置高亮页面
            return page


# 实例化
with sync_playwright() as pw:
    # 创建浏览器对象
    browser = pw.chromium.launch(channel="msedge", headless=False)
    # 创建浏览器上下文
    context = browser.new_context()
    # 创建页面
    page = context.new_page()
    # page.goto("https://www.baidu.com/")
    # 打开QQ空间
    # page.goto("https://qzone.qq.com/")
    # QQ邮箱
    # page.goto("https://mail.qq.com/")
    # 126邮箱
    # page.goto("https://www.126.com/")
    # 弹窗地址
    page.goto(
        "file:///E:/%E5%AD%A6%E4%B9%A0/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/%E6%9F%A0%E6%AA%AC%E7%8F%AD/Python%E8%87%AA%E5%8A%A8%E5%8C%96/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/alert_demo.html")
    # 全局修改超时时间,默认是30000ms
    page.set_default_timeout(10000)


    # locator自带默认等待机制，等待时间默认为30s
    # page.locator("//a[text()='登录1']").click(timeout=10000)  # 单独对这个查询修改为10000ms

    # iframe 定位
    # frame_page = page.frame_locator("#login_frame")
    # frame_page.locator("#switcher_plogin").click()
    # frame_page.locator("#u").fill("123456")

    # 多层次的iframe嵌套
    # frame_page = page.frame_locator("#login_frame").frame_locator("#ptlogin_iframe")
    # frame_page.locator("#switcher_plogin").click()
    # 获取所有的frame列表
    # frame_list = page.frames
    # frame_page = frame_list[3]
    # frame_page.locator("#switcher_plogin").click()
    # id不固定，有随机数,使用xpath方式获取
    # frame_page = page.frame_locator('//iframe[contains(@id,"x-URS-iframe")]')
    # frame_page.locator("#un-login").check()

    # 5.页面切换
    # page.locator('//a[contains(text(),"新闻")]').click()
    # page.locator('//a[@class="mnav c-font-normal c-color-t" and contains(text(),"图片")]').click()
    # page.locator('//a[@class="mnav c-font-normal c-color-t" and contains(text(),"文库")]').click()
    # 延迟，等待页面加载完成
    # page.wait_for_timeout(3000)
    # 获取页面列表
    # pages = context.pages
    # # 循环pages列表
    # for page in pages:
    #     # 判断列表是否在想要操作的页面
    #     if "新闻" in page.title():
    #         page.bring_to_front() # 设置高亮页面
    #         # 输入内容
    #         page.locator("#ww").fill("新闻123")
    # new_page = switch_windows(context, "新闻")
    # new_page.locator("#ww").fill("新闻123")

    # 封装弹窗处理方法
    def handledlg(dialog):
        page.wait_for_timeout(1000)  # 等待1s看弹窗效果
        # 触发弹窗方法
        dialog.accept()  # 相当于点击确认，让弹窗消失
        # dialog.dismiss() # 相当于点击取消，让弹窗消失


    # 监听弹窗事件
    page.on("dialog", handledlg)

    # 触发弹窗
    page.locator("#alert").click()
    page.locator("#confirm").click()
    page.locator("#prompt").click()
    # 获取窗口列表
    page.wait_for_timeout(3000)
