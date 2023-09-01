import requests

"""
a_bogus 获取地址
curl --location --request POST 'aHR0cDovLzE4Mi40NC4xNy4xMTY6Njc4OS9keS1zaWduYXR1cmU=' \
--header 'Content-Type: application/json' \
--header 'Accept: */*' \
--data-raw '{
    "token": "bf207221-3879-4ea1-b390-ed4a6ff41004",
    "url": "https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7052149213647342862&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333",
    "data": {} # 如果是post请求可以添加data
}'
"""

cookies = {
    'ttwid': '1%7CmpYTi1goGC0adR0cCiRXi9cuBb2H1bK_e5U7qbyAYtY%7C1693459855%7Ce6cc5f347a0c1b6570c113082168f74e58087649c30382de093663243af1abdd',
}

headers = {
    'authority': 'www.iesdouyin.com', # 这里必须和你的 host 一致
  	# 正常 referer 即可
    'referer': 'https://www.iesdouyin.com/share/video/7267887627636837673/?region=CN&mid=7236664966387271682&u_code=4aacl8fi0b0k&did=MS4wLjABAAAAFObUk9-cB96WUY51tzzxUB-rA-Znp1IUqgpe8KjP0a52EudcSS-8OKG6Y_ccfFD7&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=Lf7w_g03wFW8o.B8fqoyjZnnPoYUSI1Qkxl0mWyy3mo-&share_version=170400&ts=1693301622&from_ssr=1&from=web_code_link',
  	# 使用返回的ua确保一致性
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}

url = "https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7052149213647342862&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333&msToken=_9XcLxMOd8Mx__7bMEXwi5fSYtVVRsTI9T63VD9OWf7pINn3QdjGUuCFXpayIOAJh8VTh8naEwS6j1yVRva8sOmnwQypaB6RtEduypTSlAVthDnAim3AyZaPvi0gHqY%3D&a_bogus=QJBYvcZVMsR1afV6-7kz9e4mZuD0YW4QgZEzEh-X8ULv&X-Bogus=DFSzswSLewJANrmsty3Nc09WcBr8"
response = requests.get(url, cookies=cookies, headers=headers)
print(response.text)
