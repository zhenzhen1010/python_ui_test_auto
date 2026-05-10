'''
定义夹具文件
    -login_fixture：处理登录前置处理
'''

import pytest
from config.env import config
from pageobject.homepage import HomePage
from pageobject.loginpage import LoginPage


# 在钩子函数中添加环境命令，方便执行时选择环境配置
def pytest_addoption(parser):
    '''
    :param parser: 参数解析器，固定写法，不能改名字
    parser.addoption:⽤于⾃定义参数的⽅法
    '''
    # 注册⾃定义参数命令⾏参数
    parser.addoption("--env", default="test", choices=['dev', 'test', 'pre', 'prod'], help="命令⾏参数'--env'设置环境切换")

# 读取环境并加载配置
@pytest.fixture(scope="session", autouse=True)
def get_env(request):
    # 从命令行参数中读取evn参数的值
    env_name = request.config.getoption("--env")
    print(f"--env的参数是：{env_name}")
    # yield option
    config.load(env_name)
    print(f"当前环境URL：{config.data['base_url']}")
    # return config.data['base_url']


@pytest.fixture()  # 定义为夹具
def login_fixture(page):
    page.goto(config.data["base_url"])
    # 1.点击首页的登录链接,调用首页页面对象的方法
    HomePage(page).click_login_link_method()
    # 2.完成登录页面的登录操作
    LoginPage(page).login_method(config.data["username"], config.data["password"])
    page.wait_for_timeout(500)
