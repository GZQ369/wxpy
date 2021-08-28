import json
from threadPool import mutilThread
from urllib.request import Request, urlopen
from twilio.rest import Client
import time
import requests
import socket
from useChrome import get_token
import datetime
from check import checkInput
import threading

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

service_numUrl = "https://result.eolinker.com/Y6AuFCEa6d001e6c7fbf838f0c238278fa84e809bee6457?uri=/use_service/number"

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
    return data

# jsonData = getExamDate(service_numUrl)
# #{'status': False, 'number': 5}
# text = json.loads(jsonData)

# print(text)
# exit(0)

def getAllcountryId():
    allCountryId = getExamDate(countryId)
    # s = allCountryId.replace('\\', '\\\\')
    d = json.loads(allCountryId)
    dc = {}
    for i in d:
        dc[i["domainId"]] = i["name"]
    return dc

# print(getAllcountryId())

def getTestYMD(counId):
    Url = countryUrl + str(counId)
    return getExamDate(Url)
# YMD = getTestYMD(140)
# d = json.loads(YMD)
# print(d[0]["module"])
# exit()

def getTestHMS(examId, module):
    Url = speakExamUrl + examId + '&Module=' + str(module)
    return getExamDate(Url)


def praseYMDDate(countryId):
    """
    数据处理,得到 Listening, Reading and Writing 考试时间 和examId
    :return:
    """
    YMD = getTestYMD(countryId)  # 阿富汗是140
    # print(YMD)

    d = json.loads(YMD)
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
    d = json.loads(HMS)
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
def inputId():
    userId = input("请输入护照号:")

    if len(userId) > 18:
        print("输入错误!!!")
        inputId()
    else:
        print('请确认护照号号是否正确:' , userId)
        Isright = input('y-正确, n-错误')
        if Isright != 'y':
            inputId()
    return userId
# print(inputId())
# exit()      
import csv
def readUserData(ls):
    userList = []
    csv_reader = csv.reader(open(ls))
    for line in csv_reader:
        userList.append(line)
        print(line)
    

    return userList[1:]

# readUserData("./dns1.CSV")
# exit(0)
def send_notice(event_name, key, country,closeTime,SpeakingCloseTime):
    url = "https://maker.ifttt.com/trigger/"+event_name+"/with/key/"+key+""
    payload = "{\n    \"value1\": \""+country+" \",\"value2\": \""+closeTime+"\",\"value3\": \""+SpeakingCloseTime+"\"\n}"

    payload2 = "{\n    \"value1\": \""+closeTime+"\"\n}"
    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    print(response.text)

def tanresChainTime(clonstime):
    fd = datetime.datetime.strptime(clonstime, "%Y-%m-%dT%H:%M:%SZ")
    return (fd + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
                
allCountryid = getAllcountryId()

def choiceStrategyTestTime(userData):
    """
    选择考试时间的策略，选第一个时间
    :return:
    """
    username, password, dateChoice, userId, gender= userData[0],userData[1],userData[3],userData[2],userData[4]
    
    thread_name = threading.current_thread().name

    #护照id
    # userId = inputId()

    # gender = input("请输入性别(0-女性,1-男性):")
    # if gender != '0' and  gender != '1':
    #     print("输入错误!!!")
    #     return
    # mkdir(userId)
    # IdFile = input("请将上传的文件放入{}文件夹内!放入完毕请输入: y 继续" .format(userId))
    # if IdFile != 'y' :
    #     print("输入错误!!!")
    #     return
    # fileList = getFileName(userId[-6:])
    # print("这是即将上传的文件:",fileList)

    # username = input("请输入报名账号: ")
    # password = input("请输入报名密码: ")

    # dateChoice = input("请输入报名日期(1-31日任一数字日期):")
    # if not dateChoice.isdigit():
    #     return
    # dateChoice = int(dateChoice)    
    # if dateChoice > 31 :
    #     return
    

    i=1  #开启第巨轮监测
    while True:
        print("开启第{}轮监测...... " .format(i))
        for key,country in allCountryid.items():
            #选着听读写考试时间
            print("{}正在检查能报名的 {}  国家...{}" .format(thread_name, country,key))
            module, tests = praseYMDDate(key)
            if len(tests)==0:
                time.sleep(0.85)
                continue
            else:
                closeTime,examID = timeCompare(tests)

                choiceDay = closeTime[8:10]
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
                    print("{}监测到能报名的{}国家，Listening-Reading-Writing 考试时间{}, speaking 考试时间{}".format(thread_name, country,closeTime,SpeakingCloseTime))
                        
                    closeTime = tanresChainTime(closeTime)
                    SpeakingCloseTime = tanresChainTime(SpeakingCloseTime)

                    try:

                        payid = get_token(username, password, userId, country , gender, closeTime, SpeakingCloseTime)
                        #通知支付成功
                        send_notice('yasi_pay', 'bGxjFVZ5WvKoQUBJnP_zsJ', country + "报名成功", userId + "报名成功:" + payid , closeTime+"口语考试时间：" + SpeakingCloseTime + "，倒计时75min报名时间截止，快去付款吧！" )
                        return
                    except:
                        #通知失败
                        send_notice('yasi_pay', 'bGxjFVZ5WvKoQUBJnP_zsJ', country + "报名失败", userId + "报名失败，请继续观察，正在努力重试······", closeTime+"口语考试时间："+SpeakingCloseTime )
                        print("{}正在加入重试队列重试{}......".format(thread_name, userData))
                         #任务失败加入重试队列
                        userls.append()
                        # send_notice('yasi', 'bGxjFVZ5WvKoQUBJnP_zsJ', country,closeTime,SpeakingCloseTime )
                        
        time.sleep(1.28)
        i+=1

# choiceStrategyTestTime()

def startTask():

    # userId = input("请输入你的用户名/手机号: ")
    
    # password = input("请输入你的密码: ")
    # if password != userId[-6:] or len(userId) !=11 :
    #     print("密码或用户名输入错误")
    #     return
    global userls
    userls = readUserData("./dns1.CSV")
    startTotal = len(userls)

    checkInput(userls)
    text = json.loads(getExamDate(service_numUrl))
    core, status = text["number"], text["status"]
    print("开启{}核服务线程......".format(core))

    if not status:
        print("环境配置错误")
        return
    
    mutilThread(core, choiceStrategyTestTime, userls)
    print("本次成功报名{}个".format(startTotal - len(userls)))


# startTask()


def offMutinitl():
    HOST='127.0.0.1'
    PORT=5555
    try:
        s = socket.socket()
        s.bind((HOST, PORT))
        # main()
        startTask()
        s.close()
    except KeyboardInterrupt:
        s.close()
    except:
        print(' 程序异常，已退出.')
        return 
        exit(0)

offMutinitl()