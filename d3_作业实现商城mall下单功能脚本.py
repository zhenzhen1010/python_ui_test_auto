# 导入库
from playwright.sync_api import sync_playwright, expect
import re

# 实例化
with sync_playwright() as pw:
    # 创建浏览器对象
    browser = pw.chromium.launch(channel="msedge",headless=False)
    # 创建浏览器上下文
    context = browser.new_context()
    # 创建页面
    page = context.new_page()
    # 打开必应网页
    page.goto("http://shop.lemonban.com:3344/")
    # 选中登陆元素,并点击登陆
    page.locator("//a[text()='登录']").click()
    # 选中用户名输入元素，并输入内容
    page.locator("//div[@class='item account']/input").fill("lemon_python")
    # 选中密码输入元素，并输入内容
    page.locator("//div[@class='item password']/input").fill("12345678")
    # 选中登陆按钮元素，并点击登陆
    page.locator("//a[@class='login-button']").click()
    # 强制等待，不然输入不了
    page.wait_for_timeout(2000)
    # 添加断言，是否成功登陆页面
    expect(page.locator('//div[@class="item"]/span[@class="text"]')).to_have_text("欢迎来到柠檬班")
    # 点击搜索，输入搜索内容
    page.locator('//div[@class="search-input-box"]/input[@class="search-input"]').fill("真皮圆筒包")
    # 点击搜索
    page.locator('//div[@class="search-msg"]/input[@class="search-btn"]').click()
    page.wait_for_timeout(1000)
    # 添加断言，查询框是否输入 ”真皮圆筒包“
    expect(page.locator('//div[@class="search-input-box"]/input[@class="search-input"]')).to_contain_text("真皮圆筒包")
    # 添加断言，返回列表数据是否都为包含”真皮圆筒包“
    expect(page.locator('//div[@class="goods-name"]')).to_contain_text("真皮圆筒包")
    # 添加判断，可能存在多条数据
    ele_list = page.locator('//div[@class="goods-img"]/img').all()
    # 无论有多少个产品，都是选择第一个
    ele_list[0].click()
    # 添加断言，判断进入的是否为筛选的产品
    expect(page.locator('//div[@class="name-box"]/div[@class="name"]')).to_contain_text("真皮圆筒包")
    # 点击立即购买
    page.locator('//a[text()="立即购买"]').click()
    # 等待加载地址
    page.wait_for_timeout(1000)
    # 添加断言，进入提交订单页面
    expect(page).to_have_url(re.compile(r'http://shop.lemonban.com:3344/submit-order\?orderEntry=\d+'))
    # 点击提交订单
    page.locator('//a[text()="提交订单"]').click()
    # 点击选择支付方式：微信
    page.locator('//span[text()="微信支付"]/parent::div').click()
    # 等待选择支付方式
    page.wait_for_timeout(1000)
    # 添加断言，进入支付页面
    expect(page).to_have_url("http://shop.lemonban.com:3344/payment")
    # 点击立即支付
    page.locator('//a[text()="立即付款"]').click()
    page.wait_for_timeout(2000)