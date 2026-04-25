import logging

# 日志基础配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(r"C:\Users\Administrator\Desktop\run_log.txt", encoding="utf-8"),
        logging.StreamHandler()
    ],
    force=True
)

# 接口基础地址
BASE_URL = "https://jsonplaceholder.typicode.com"

# 请求超时时间
TIMEOUT = 10