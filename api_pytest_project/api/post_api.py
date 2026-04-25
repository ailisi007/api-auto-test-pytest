import requests
import logging
# 导入全局的地址和超时时间
from config.settings import BASE_URL, TIMEOUT


# 获取所有帖子数据
def get_post_list():
    # 拼接接口地址
    url = f"{BASE_URL}/posts"
    # 发送get请求
    response = requests.get(url, timeout=TIMEOUT)
    
    # 简单判断状态码对不对
    assert response.status_code == 200, f"查询接口状态码异常，实际：{response.status_code}"
    post_list = response.json()
    
    # 确保有数据返回
    assert len(post_list) > 0, "查询结果：帖子列表为空"
    logging.info(f"✅ 查询帖子列表成功，数据条数：{len(post_list)}")
    return post_list


# 用来新建帖子
def add_post(title: str, body: str, user_id: int = 1):
    url = f"{BASE_URL}/posts"
    # 准备要传的参数
    request_data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    # 发起post请求
    response = requests.post(url, json=request_data, timeout=TIMEOUT)

    # 新增成功一般是200或201
    assert response.status_code in [200, 201], f"新增接口状态码异常，实际：{response.status_code}"
    new_post = response.json()

    # 核对一下标题有没有对上
    assert new_post["title"] == title, "新增帖子标题不一致"
    logging.info(f"✅ 新增帖子成功，帖子ID：{new_post['id']}")
    return new_post


# 修改帖子信息
def update_post(post_id: int, new_title: str):
    # 拼接要修改的帖子id
    url = f"{BASE_URL}/posts/{post_id}"
    request_data = {"title": new_title}
    response = requests.put(url, json=request_data, timeout=TIMEOUT)

    # 校验接口返回状态
    assert response.status_code == 200, f"修改接口状态码异常，实际：{response.status_code}"
    updated_post = response.json()

    # 判断修改后的内容
    assert updated_post["title"] == new_title, "修改后标题校验失败"
    logging.info(f"✅ 修改帖子成功，新标题：{new_title}")


# 删除指定帖子
def delete_post(post_id: int):
    url = f"{BASE_URL}/posts/{post_id}"
    # 执行删除请求
    response = requests.delete(url, timeout=TIMEOUT)

    assert response.status_code == 200, f"删除接口状态码异常，实际：{response.status_code}"
    logging.info(f"✅ 删除帖子成功，删除ID：{post_id}")