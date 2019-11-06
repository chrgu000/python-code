import webbrowser
import requests

url = "http://47.244.212.164:8888/login"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer" : "http://47.244.212.164:8888/u5r1f2uo/"

}

cookies = dict(request_token="ASCYPK8MeTIO59absnRlRS0jUVFw0pmOmVo8Z0ShdSqvGwnV", order="id%20desc", memSize="7821", serverType="nginx", BT_PANEL_6="9817fd4e-b441-45af-951c-1d606ed1a4f8.Ei9t9PpwauYKJAQ8Exr1j7u4ayI")

data = {
    "username" : "fa6730xm",
    "password" : "4f7d2a7d841a837d9d7067f13a45591f"
}


requests.packages.urllib3.disable_warnings()
with requests.Session() as s:  # 持续会话
    reponse = s.post(url, data=data, headers=header, verify=False, cookies=cookies)

    # print(reponse.text)
    print(reponse.headers)
    webbrowser.open("http://47.244.212.164:8888/firewall")