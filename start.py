import json
from urllib.request import Request, urlopen
from twilio.rest import Client
import time
import requests
import socket

# zb网站获取数据Api
countryUrl = "https://ieltsindicator.britishcouncil.org/api/availabilities?CountryId="
# 定义全局变量国家id
YASHI_Url = "https://ieltsindicator.britishcouncil.org/"
# 英国得country-id 、阿富汗得140
CountryId = 140
# 包装头部
firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
countryId = "https://ieltsindicator.britishcouncil.org/api/countries"
speakExamUrl = "https://ieltsindicator.britishcouncil.org/api/availabilities/speaking?ExamId="
# 有效使用期限
maxUseTime = "2022-01-01T07:00:00Z"
signNum = '+86 159 6804 0165'
me ='+86 186 1683 2808'
fromNum ='+14158959062'
account_sid = "AC4e69a19f4c95be9cb45484d55c33bfeebb74"
# Your Auth Token from twilio.com/console
auth_token  = "e973cda16890eea93792474454402958251f3"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "a9477d0f-08ee-4960-b6f8-9fd85dc0d5cc,d376ec80-54e1-450a-8215-952ea91b01dd",
    'Host': "maker.ifttt.com",
    'accept-encoding': "gzip, deflate",
    'content-length': "63",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

def getExamDate(url):
    """
    传入country id 获取每个国家不同得考试时间
    :return:
    考试时间
    """
    request = Request(url, headers=firefox_headers)
    html = urlopen(request)
    # 获取数据
    data = html.read()
    # 转换成字符串
    # print(data)
    return str(data)

def getAllcountryId():
    allCountryId = getExamDate(countryId)
    s = allCountryId.replace('\\', '\\\\')
    d = json.loads(s[2:-1])
    dc = {}
    for i in d:
        dc[i["domainId"]] = i["name"]
    return dc


def getTestYMD(counId):
    Url = countryUrl + str(counId)
    return getExamDate(Url)


def getTestHMS(examId, module):
    Url = speakExamUrl + examId + '&Module=' + str(module)
    return getExamDate(Url)


def praseYMDDate(countryId):
    """
    数据处理,得到 Listening, Reading and Writing 考试时间 和examId
    :return:
    """
    YMD = getTestYMD(countryId)  # 阿富汗是140
    d = json.loads(YMD[2:-1])
    if len(d) == 0:
        return 1,[]
    module = d[0]['module']
    tests = d[0]['tests']  # [ ]map[string]string

    return module, tests


# module, tests = praseYMDDate(1)

def praseHMSDate(examId, module):
    """
    解析考试时间时分秒选择，speaking选择
    :return:
    """
    HMS = getTestHMS(examId, module)
    d = json.loads(HMS[2:-1])
    if len(d) == 0:
        return [],0
    avaibleCount = len(d[0]["tests"])
    avaibleTests = d[0]['tests']  # [ ]map[string]string
    return avaibleTests, avaibleCount

#
# avaibleTests, avaibleCount = praseHMSDate("08d94dcf-7616-b27d-000d-3aaa111e0000", 1)
# print(avaibleTests, avaibleCount)

def timeCompare(req):
    """
    传入得数据类型必须为 d[0]['tests'] 的类型
    :param req:
    :return:
    """
    closeTime =  ""
    examID = ""
    for item in req:
        if closeTime == "":
            closeTime = min(maxUseTime, item["startDateUtc"])
            examID = item["examId"]
        else:
            if closeTime > item["startDateUtc"]:

                closeTime =  item["startDateUtc"]
                examID = item["examId"]

    return closeTime,examID

# print(timeCompare(avaibleTests))
# exit()

def sendMessage(country,closeTime,SpeakingCloseTime):

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        # 这里中国的号码前面需要加86
        to=signNum,
        from_= fromNum,
        # body="监测到能报名的{}国家，Listen-Read-Writ 考试时间{}, speaking 考试时间{}" .format(country,closeTime,SpeakingCloseTime) )
        body= "测试信息")
    print("发送短信成功" ,message.sid)

    # call = client.calls.create(
    #     to=signNum,
    #     from_=fromNum,
    #     url = "http://demo.twilio.com/docs/voice.xml",
    #     method = "GET",
    #     status_callback="https://www.myapp.com/events",
    #     status_callback_method="POST",
    #     status_callback_event=["initiated", "ringing", "answered", "completed"]
    # )
    #
    #
    # print(call.sid)
# sendMessage(1,2,3)
# exit()

def send_notice(event_name, key, country,closeTime,SpeakingCloseTime):
    url = "https://maker.ifttt.com/trigger/"+event_name+"/with/key/"+key+""
    payload = "{\n    \"value1\": \""+country+" \",\"value2\": \""+closeTime+"\",\"value3\": \""+SpeakingCloseTime+"\"\n}"

    payload2 = "{\n    \"value1\": \""+closeTime+"\"\n}"
    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    print(response.text)
 

def choiceStrategyTestTime():
    """
    选择考试时间的策略，选第一个时间
    :return:
    """
    userId = input("请输入你的用户名/手机号: ")
    
    password = input("请输入你的密码: ")
    if password != userId[-6:] or len(userId) !=11 :
        print("密码或用户名输入错误")
        return
    
    dateChoice = input("请输入报名日期(1-31日任一数字日期):")
    if not dateChoice.isdigit():
        return
    dateChoice = int(dateChoice)    
    if dateChoice > 31 :
        return
    

    allCountryid = getAllcountryId()
    i=1
    while True:
        print("即将开启第{}轮监测...... " .format(i))
        for key,country in allCountryid.items():
            #选着听读写考试时间
            print("正在检查能报名的 {}  国家...{}" .format(country,key))
            module, tests = praseYMDDate(key)
            if len(tests)==0:
                time.sleep(0.85)
                continue
            else:
                closeTime,examID = timeCompare(tests)

                choiceDay = int(closeTime[8:10])
                if choiceDay != dateChoice:
                    continue

                #验证这些时间中可以选折使用的speaking考试时间
                time.sleep(0.012)

                avaibleTests, avaibleCount = praseHMSDate(examID, module)
                if avaibleCount==0:
                    time.sleep(0.25)
                    continue
                else:
                    SpeakingCloseTime,examID = timeCompare(avaibleTests)
                    print("监测到能报名的{}国家，Listening-Reading-Writing 考试时间{}, speaking 考试时间{}".format(country,closeTime,SpeakingCloseTime))
                    # send_notice('yashi', 'bGxjFVZ5WvKoQUBJnP_zsJ', country,closeTime,SpeakingCloseTime )
                    continue
        time.sleep(1.28)
        i+=1

choiceStrategyTestTime()


def offMutinitl():
    HOST='127.0.0.1'
    PORT=5555
    try:
        s = socket.socket()
        s.bind((HOST, PORT))
        # main()
        choiceStrategyTestTime()
        s.close()
    except KeyboardInterrupt:
        s.close()
    except:
        print(' 程序异常，已退出.')
        exit(0)
