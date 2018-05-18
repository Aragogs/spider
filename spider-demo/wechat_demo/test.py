
'''
通过接口访问北京拆哪公众号
'''
import requests
from bs4 import BeautifulSoup
import re
import json
import time

while True:
    url="https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI2MTYxNTg3NA==&scene=124&devicetype=android-22&version=26051633&lang=zh_CN&nettype=WIFI&a8scene=1&pass_ticket=Q8Q1WRz0SHnytsBiee6vhbrTwMxLU8WxBW6qguRY12i1EQ727rP%2Ffy8DCAm1JnGN&wx_header=1"
    headers={
        "Host":"mp.weixin.qq.com",
        "Connection":"keep-alive",
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; MX4 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043909 Mobile Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
        #"x-wechat-key": "195f5369276b3268a517c533661e87df71e44a00121f29e421ba75588fbef43fa9a4530b19b0cf0d2d705d5dff54d31f21fea325c1816927b927ca3bb6538e1bf6230bc1752e3b96549488600ea8eb4f",
        "x-wechat-key": "b3aaf236e5f9a333a1b35c83bff9665db4976a56d07c8a421297df77158ebeeb50e821bca0fff99c7c5df96c1913d0caf310a2dcd863b3628dde84021d5154d7a531984221ecb83bb7b67705dd2014dd",
        "x-wechat-uin": "MjUxODExNDYzMQ%3D%3D",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,en-US;q=0.8",
        #"Cookie":"rewardsn=; wxuin=2518114631; devicetype=android-22; version=26051633; lang=zh_CN; pass_ticket=Q8Q1WRz0SHnytsBiee6vhbrTwMxLU8WxBW6qguRY12i1EQ727rP/fy8DCAm1JnGN; wap_sid2=CMfC3bAJElxaZzRuNjN6bW53OU1ZSDI4OWdNTlpzQlFhc1FVaUFmTjJGUHVjazVYbFFQRS0tdk9vLUsxU2NWTGtmVEVldXVzV1ZEY2dBd1JsNTViTW45cFdVRGlEcmNEQUFBfjCTvqHWBTgNQAE=; wxtokenkey=777",
        "Cookie": "rewardsn=; wxuin=2518114631; devicetype=android-22; version=26051633; lang=zh_CN; pass_ticket=Q8Q1WRz0SHnytsBiee6vhbrTwMxLU8WxBW6qguRY12i1EQ727rP/fy8DCAm1JnGN; wap_sid2=CMfC3bAJElxQTnNYdzdXdU1WdTF6UHA5MXh1cVVDbGZGc19vb3NkTUJCQmVMZnZQSndEMGxrVVc1ejdTQVM1QkZCWkNlX2QwTmpPaVByeGFNdDdTX3lqNHg5TTRXYmNEQUFBfjCWmKHWBTgNQAE=; wxtokenkey=777",
        "Q-UA2": "QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.5.22&TBSVC=43602&CO=BK&COVC=043909&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MX4 &RL=1152*1920&OS=5.1&API=22",
        "Q-GUID": "56bb6324d5fcb44d8dcdaff613b788cb",
        "Q-Auth": "31045b957cf33acf31e40be2f3e71c5217597676a9729f1b"
    }
    response=requests.get(url=url,headers=headers,verify=False)
    if "操作频繁" in response.text:
        print("操作频繁,等会试一试")
        break
    if "验证" in response.text:
        print("x-wechat-key 已失效，需要重新获取")
        break
    else:
        list_str = re.search("var msgList =.*'(.*?)';", response.text).group(1).replace("&quot;", "\"")
        # print(list_str)
        # print(response.headers)
        json = json.loads(list_str)
        for item in json["list"]:
            # print(item["app_msg_ext_info"]["cover"].replace("\\",""))
            print(item["app_msg_ext_info"]["content_url"].replace("\\", ""))

        urll = "https://mp.weixin.qq.com/s?__biz=MzI2MTYxNTg3NA==&mid=2247484248&idx=1&sn=16968437d177a24cebb3f55669856193&chksm=ea56fb35dd21722392ed13506aaf6495165dbe9a4587dacc4274c5060fb8e3dde63b0923377e&scene=38&ascene=0&devicetype=android-22&version=26051633&nettype=WIFI&abtest_cookie=BQABAAgACgALAAwADQALAJ6GHgCdih4ApYoeAD6LHgDUix4A5IseABCMHgCljB4AuoweAL6MHgDQjB4AAAA%3D&lang=zh_CN&pass_ticket=Q8Q1WRz0SHnytsBiee6vhbrTwMxLU8WxBW6qguRY12i1EQ727rP%2Ffy8DCAm1JnGN&wx_header=1"
        response2 = requests.get(url=urll, headers=headers, verify=False)
        html = BeautifulSoup(response2.text)
        activity_name = html.find("h2", {"id": "activity-name"}).text
        print("解析成功--------》" + activity_name)


    print(time.localtime(time.time()))
    time.sleep(5)




