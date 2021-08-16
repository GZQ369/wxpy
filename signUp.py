import json
import requests
from fake_useragent import UserAgent

headers={"Proxy-Connection": "keep-alive","Pragma": "no-cache",#"DNT":"1",\
"User-Agent":ua.random,"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4","Referer": "www.huixiaoer.com","\
Accept-Charset": "gb2312,gbk;q=0.7,utf-8;q=0.7,*;q=0.7","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
*/*;q=0.8","Accept-Encoding":"gzip, deflate, sdch","Cache-Control":"max-age=0","Connection":"keep-alive","Content-Type":\
    "application/x-www-form-urlencoded",#"Cookie":"pgv_pvi=9755294720; aliyungf_tc=AQAAAIEbHSUhVA4ATkxVeHH7o+UfJUCq; \
    acw_tc=AQAAAFesTD4BeQ4ATkxVeNrQ4zX/wI03; PHPSESSID=flc3hhtdbcgvr4pgekhvk7rrb1; pgv_si=s7094364160; city=440100; \
        _ga=GA1.2.968334469.1525633526; _gid=GA1.2.1982983394.1525633526; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22162fc16d967476-00a0ee49af4a81-5d4e211f-1049088-162fc16d9684e5%22%2C%22%24device_id%22%3A%22162fc16d967476-00a0ee49af4a81-5d4e211f-1049088-162fc16d9684e5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22bdpp_web%22%2C%22%24latest_utm_medium%22%3A%22ppc%22%2C%22%24latest_utm_campaign%22%3A%22title_20180223%22%7D%7D; Hm_lvt_d47d0c2743e9b14d07c86e077d6bdaa2=1524647779,1524651322,1525633526,1525673504; Hm_lpvt_d47d0c2743e9b14d07c86e077d6bdaa2=1525674666",

"Host":"www.huixiaoer.com","Upgrade-Insecure-Requests":"1","X-Requested-With":"XMLHttpRequest"}

class signUp:
    def __init__(self) -> None:
        
        self.tokenUrl =  "https://eamidentity.britishcouncil.org/connect/token"
        self.userInfo = "https://eamidentity.britishcouncil.org/connect/userinfo"
        self.headers = {'Content-Type': 'application/json',
            'authority': 'eamidentity.britishcouncil.org',
'method': 'POST',
'path': '/connect/token',
'scheme': 'https',
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'content-length':'294',
'content-type':'application/x-www-form-urlencoded',
'origin':'https://ieltsindicator.britishcouncil.org',
'referer':'https://ieltsindicator.britishcouncil.org/',
    'sec-fetch-site': 'same-site',
    'sec-ch-ua': "Chromium" ;v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
        
        
        
        
        self.fromDate = {'client_id': 'ieltsindicator.b2c.app',
            'code': 'c25UEey0EPX1TtQk9q4HnOenmoj0BTXJvBduXC1rZqg',
            'redirect_uri': 'https://ieltsindicator.britishcouncil.org/callback',
            'code_verifier': '7697d7a8fbae49189473dfaa5b449e36ec1a5bd54d8a4f9ea43f0342ad960742da536a3c863740ab8067efa6276b3e55',
            'grant_type': 'authorization_code'}



    def login(self):
        response = requests.post(url='url', headers=headers, data=json.dumps(data))
        
