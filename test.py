#
#导入 requests 包 (续安装 pip install requests 慢的话需要换镜像源)
# requests 的 7 个主要方法
# requests.request() 构造一个请求,支撑以下各方法的基础方法
# requests.get() 获取 HTML 网页的主要方法,对应于 HTTP 的 GET
# requests.head() 获取 HTML 网页头信息的方法,对应于 HTTP 的 HEAD
# requests.post() 向 HTML 网页提交 POST 请求的方法,对应于 HTTP 的 HEAD
# requests.put() 向 HTML 网页提交 PUT 请求的方法,对应于 HTTP 的 PUT
# requests.patch() 向 HTML 网页提交局部修改请求,对应于 HTTO 的 PATCH
# requests.delete() 向 HTML 页面提交删除请求,对应于 HTTP 的 DELETE

import requests

r = requests.get("http://www.baidu.com")

print(r.text)

