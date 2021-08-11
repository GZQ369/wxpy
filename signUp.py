import json
import requests


class signUp:
    def __init__(self) -> None:
        
        self.tokenUrl =  "https://eamidentity.britishcouncil.org/connect/token"
        self.userInfo = "https://eamidentity.britishcouncil.org/connect/userinfo"
        self.headers = {'Content-Type': 'application/json',
            :authority: eamidentity.britishcouncil.org
'method: POST
'path: /connect/token
'scheme: https
'accept: */*
'accept-encoding: gzip, deflate, br
'accept-language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'content-length':'294',
'content-type':'application/x-www-form-urlencoded',
'origin':'https://ieltsindicator.britishcouncil.org',
'referer':'https://ieltsindicator.britishcouncil.org/',
    'sec-fetch-site': 'same-site',
    'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
        
        
        
        }
        self.fromDate = {'client_id': 'ieltsindicator.b2c.app',
            'code': 'c25UEey0EPX1TtQk9q4HnOenmoj0BTXJvBduXC1rZqg',
            'redirect_uri': 'https://ieltsindicator.britishcouncil.org/callback',
            'code_verifier': '7697d7a8fbae49189473dfaa5b449e36ec1a5bd54d8a4f9ea43f0342ad960742da536a3c863740ab8067efa6276b3e55',
            'grant_type': 'authorization_code'}



    def login(self):
        response = requests.post(url='url', headers=headers, data=json.dumps(data))
        
