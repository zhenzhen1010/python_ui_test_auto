'''
入口文件：
    1.日志持久化 写入日志文件：路径处理
    2.收集搜友的测试哦那管理并执行
    3.生成测试报告-allure：路径处理
'''
import pytest
from loguru import logger
from common.handle_path import log_path, report_path
import sys  # 内置模块，不需要安装

# 1.日志持久化，写入日志文件
logger.add(sink=log_path,
           encoding="utf-8",
           level="INFO",
           rotation="20MB",
           retention=20)
# 准备pytest参数
args = [
    "-sv",
    f"--alluredir={report_path}",
    "--clean-alluredir",
    # "-m p1",
]
print(f"传进来的参数111：{sys.argv}")
# 2. 获取命令行环境参数 --env=xxx
for arg in sys.argv[1:]:
    # if arg.startswith("--env="):
    args.append(arg)

# 面试官会问，如何保证我们UI自动化测试用例的稳定性
#     通过失败重运行可能有更高几率保证UI自动化测试执行通过和成功
# 收集用例并执行，生成测试报告  --reruns=2 遇到失败用例则重新执行2次(不推荐使用)，--reruns-delay=3 间隔时间
# pytest.main(["-sv", f"--alluredir={report_path}", "--clean-alluredir", "-m p1", "--env=test"])

pytest.main(args)

