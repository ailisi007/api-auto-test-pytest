import logging
import pytest
from api.post_api import get_post_list, add_post, update_post, delete_post
from data.test_data import test_data

# 日志配置（保留你原来的）
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(r"C:\Users\Administrator\Desktop\run_log.txt", encoding="utf-8"),
        logging.StreamHandler()
    ],
    force=True
)

# 正确的pytest参数化写法
@pytest.mark.parametrize("case", test_data)
def test_post_flow(case):
    title = case["title"]
    body = case["body"]

    logging.info("---------- 开始本轮业务流程 ----------")

    # 1 查询
    get_post_list()

    # 2 新增
    new_post = add_post(title=title, body=body)
    new_post_id = new_post["id"]

    # 3 修改
    update_post(new_post_id, f"修改后的：{title}")

    # 4 删除
    delete_post(new_post_id)

    logging.info("---------- 本轮流程执行成功 ----------\n")