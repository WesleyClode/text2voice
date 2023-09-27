import requests
import json

# 定义要监听的网站URL
url_to_monitor = "https://cloud.google.com/text-to-speech?hl=zh-cn"

# 定义JSON文件路径
json_file_path = "responses.json"

# 监听请求的回调函数
def response_callback(response, *args, **kwargs):
    # 判断是否是我们关心的请求
    if response.url.startswith("https://cloud.google.com/proxy?url="):
        # 获取响应内容
        response_content = response.text

        # 将响应内容写入JSON文件
        with open(json_file_path, "a") as json_file:
            data = {"url": response.url, "content": response_content}
            json.dump(data, json_file, indent=4)
            json_file.write("\n")

# 发送GET请求并监听
try:
    response = requests.get(url_to_monitor, timeout=5)  # 设置请求超时时间
    response.raise_for_status()
    print("监听已启动，收集响应数据...")
except requests.exceptions.RequestException as e:
    print(f"发生请求错误: {e}")

# 调用回调函数并传递响应对象
response_callback(response)
