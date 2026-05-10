import pathlib

# 日志文件的路径处理
log_path = pathlib.Path(__file__).parent.parent / "logs" / "mall_UI.log"

# 报告路径处理
report_path = pathlib.Path(__file__).parent.parent / "allure_report"

# 截图路径处理
screenshot_path = pathlib.Path(__file__).parent.parent / "screenshot"
