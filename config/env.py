'''
环境读取工具
'''
# 引入库
import yaml
import os
import pathlib


class Config:
    _instance = None
    env = "test"  # 默认测试环境
    data = {}

    # 单例模式创建实例对象，返回实例对象
    def __new__(cls):
        if not cls._instance:
            # 第一次：借用父类底层，创建唯一一个对象
            cls._instance = super().__new__(cls)
        # 第二次及以后：直接返回已经创建好的那个对象，不再新建
        return cls._instance

    # 加载对应的配置文件
    def load(self, env_name):
        self.env = env_name
        # path = os.path.join(os.path.dirname(__file__), f"{env_name}.yaml")
        path = pathlib.Path(__file__).parent/f"{env_name}.yaml"
        with open(path, "r", encoding="utf8") as f:
            self.data = yaml.safe_load(f)

# 实例化
config = Config()