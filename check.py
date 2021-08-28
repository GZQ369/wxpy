from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from useChrome import mkdir,getFileName
import threading



def openChrome(idf):

    thread_name = threading.current_thread().name

    print(thread_name)
    chrome_options=Options()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
    chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_window_position(idf, idf*1.2)
    url = "https://eamidentity.britishcouncil.org/account/login?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dieltsindicator.b2c.app%26redirect_uri%3Dhttps%253A%252F%252Fieltsindicator.britishcouncil.org%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520email%2520ieltsindicator.b2c.api%2520registrantid%2520offline_access%26state%3D24dfa24d12514ac0b5bc0e0de3d0774d%26code_challenge%3DO-hwSD9dU0mEyPwG43vnBkxZjWBiblXxbNm5GfY3Z0c%26code_challenge_method%3DS256%26response_mode%3Dquery"
    driver.implicitly_wait(5) # seconds
    driver.get(url)
    driver.find_element_by_id("Username").send_keys("123")
    driver.find_element_by_id("password_login").send_keys("123")

def checkInput(userList):

    for item in userList:
        if len(item[2]) > 18:
            print("护照号输入错误!!!")
            exit(0)

        mkdir(item[2])
        if not item[3].isdigit():

            print("考试日期选择输入错误!!!")

            exit(0)

        if int(item[3]) > 31 :
            print("考试日期选择输入错误!!!")
            exit(0)

    
        if item[4] != '0' and  item[4] != '1':
            print("性别输入错误!!!")
            exit(0)

        
        IdFile = input("请将上传的文件放入{}文件夹内!放入完毕请输入: y 确认继续:" .format(item[2]))
        
        if IdFile != 'y' :
            print("输入错误!!!")
            return
        fileList = getFileName(item[2])
        print("这是即将上传的文件{},请确认文件路径和护照号正确" .format(fileList))

    return True



def chane():
    ls =[]
    for i in range(5):    
        ls.append(i)

    while ls:
        s = ls.pop(0)
        if s==1:
            ls.append(9)


        print(ls,s)
    print(ls)
# chane()