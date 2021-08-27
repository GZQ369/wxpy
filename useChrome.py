from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

def choiceGendor(elements,nnum):
    # 0-famale  1-male
    for i in range(len(elements)):
        if i==int(nnum):
            elements[i].click()
            return
def checkSize(file):
    fsize = os.path.getsize(file)
    f_Mb = fsize/float(1024)/float(1024)
    if f_Mb<=3.0:
        return True
    return False
# print(checkSize("./123.png"))
def getFileName(path):
    for root, dirs, files in os.walk(path):  
        # print(root) #当前目录路径  
        # print(dirs) #当前路径下所有子目录  
        print(files) #当前路径下所有非目录子文件  
        ls = os.getcwd()
        if '\\' in ls:
            ls = ls.replace('\\', '/')
        if len(files) >2:
            print("身份信息文件不正确!!!")
            exit()
        resp = []
        for i in files:
            i = ls + '/'+ path + '/' + i
            if checkSize(i):
                resp.append(i)
            else:
                print("error：文件大小小于3Mb")
                exit()
        if resp==[]:

            print("上传文件夹为空,退出程序...")
            exit(0)

        return resp

# print(getFileName("345678"))

def mkdir(path):
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
    
        os.makedirs(path) 
        print (path+' 创建成功')
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在',)

# mkdir("21345")
# exit()
mouth = ["January","February","March","April","May","June","July","August","September", "October","November","December"]

def getFmtDate(date):
    a = mouth[int(date[5:7])-1] +' '+ date[8:10]+',' +' '+date[:4]
    return a, date[8:10] ,date[11:16]


# a,d,_ = getFmtDate('2021-09-15T16:00:00Z')
# exit()


def get_token(username, password,  userId, country, gendor, writeTime, speakTime ):

    chrome_options=Options()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
    #不自动关闭浏览器
    chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument('--headless')
    """最终的效果：不会弹出浏览器窗口"""

    chrome_options.add_argument('--disable-gpu')
    global  driver
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # seed = [i*60+20 for i in range(1,15)]
    # idf = random.choice(seed)  #随机返回列表a中的一个元素

    idf = random.randint(100,900)
    driver.set_window_position(idf, idf*1.2)
    url = "https://eamidentity.britishcouncil.org/account/login?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dieltsindicator.b2c.app%26redirect_uri%3Dhttps%253A%252F%252Fieltsindicator.britishcouncil.org%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520email%2520ieltsindicator.b2c.api%2520registrantid%2520offline_access%26state%3D24dfa24d12514ac0b5bc0e0de3d0774d%26code_challenge%3DO-hwSD9dU0mEyPwG43vnBkxZjWBiblXxbNm5GfY3Z0c%26code_challenge_method%3DS256%26response_mode%3Dquery"
    driver.implicitly_wait(5) # seconds

# 　　操作浏览器，打开url，用户名密码登陆
    driver.get(url)
    driver.find_element_by_id("Username").send_keys(username)
    driver.find_element_by_id("password_login").send_keys(password)
    driver.find_element_by_id("password_login").submit()
    # time.sleep(1)
# 　　#获取token的方法：
# 　　''' 
#    1、要从Local Storage中获取还是要从Session Storage中获取，具体看目标系统存到哪个中-----开发者模式查看
#    2、window.SessionStorage和直接写SessionStorage是等效的
#    3、一定要使用return，不然获取到的一直是None
#    4、get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中
# 　　'''
    # token = driver.execute_script('return localStorage.getItem("client_id");')
    # print("token::",token)
    driver.get("https://ieltsindicator.britishcouncil.org/")
    driver.find_element_by_class_name("css-19bqh2r").click()
    e = driver.find_element_by_id("react-select-2-input")
#1.选择国家
    e.send_keys(country)
    e.send_keys(Keys.ENTER)
    #选择时间
    # c = driver.find_element_by_tag_name('abbr')
    # c = driver.find_element_by_css_selector('button.react-calendar__tile react-calendar__month-view__days__day available-day')
    # print(c)
    time.sleep(1.5)
#test data  2.笔试时间
    a,b,c = getFmtDate(writeTime)
    driver.find_element_by_xpath("//abbr[@aria-label='{}'][text()='{}']" .format(a,b)).click()
    time.sleep(1)

#3.口语考试时间
    a,b,c = getFmtDate(speakTime)
    # elements =  driver.find_elements_by_xpath("//abbr[@aria-label='September 14, 2021'][text()='14']")
    elements =  driver.find_elements_by_xpath("//abbr[@aria-label='{}'][text()='{}']" .format(a,b))


    
    # driver.find_elements_by_xpath("//div[@class='react-calendar__tile react-calendar__month-view__days__day available-day']/abbr[@aria-label='September 15, 2021'][text()='15']")
    # c = driver.find_element_by_css_selector('button.react-calendar__tile react-calendar__month-view__days__day available-day').click()
    # aria_label = driver.find_element_by_class_name('react-calendar__tile react-calendar__month-view__days__day available-day').click()

    # elements = driver.find_elements('abbr', 'button')
    for i in elements:
                print("34325325",type(i))
                # print(i.get_attribute("aria-label"))
                i.click()
    time.sleep(1.5)
    # s1 = Select(driver.find_element_by_id('bc-select-wrapper css-2b097c-container'))
    # s1.select_by_index(1)
    
    e = driver.find_element_by_id("react-select-3-input")
#3.1 口语小时
    e.send_keys(c)
    e.send_keys(Keys.ENTER)
    # driver.find_element_by_tag_name("button.react-calendar__tile react-calendar__month-view__days__day available-day").click()
    # driver.get("https://ieltsindicator.britishcouncil.org/personal-details")
    
    # return token
    time.sleep(1)

    driver.find_element_by_xpath("//button[@class='btn btn-link'][text()='I already have an account']").click()
    time.sleep(1)
    token = driver.execute_script('return localStorage.getItem("persist:root");')
    print(token)


    WebDriverWait(driver, 15, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'uppy-FileInput-input')))

    driver.find_element_by_xpath("//button[@class='uppy-FileInput-btn btn btn-primary'][text()='Choose files']")
    e = driver.find_element_by_class_name("uppy-FileInput-input")
#4.省份证正反面
    for i in getFileName(userId):

        e.send_keys(i)
    # e.send_keys(Keys.ENTER)

    # e.send_keys("C:\\Users\\gongzhiqiang\\Videos\\Captures\\123.pdf")
    # e.send_keys(Keys.ENTER)
    time.sleep(0.8)

    # e = driver.find_element_by_name("mobileNumber")
    # e.send_keys('1234567890')
    # e.send_keys(Keys.ENTER)
#5.省份证号
    e = driver.find_element_by_name("idNumber")
    e.send_keys(userId)
    e.send_keys(Keys.ENTER)
    time.sleep(0.8)
   

    # driver.find_element_by_xpath("//input[@name='gender'][text()='Female']").send_keys(Keys.SPACE)
    time.sleep(0.8)
#6.性别
    elements = driver.find_elements_by_name('gender')
    choiceGendor(elements, gendor)
    # for i in elements:
    #     if i==0:
    #         print("34325325",type(i))
    #         # print(i.get_attribute("aria-label"))
    #         i.click()
    # driver.find_element_by_xpath("//input[@name='idType'][text()='Passport']").click()
    time.sleep(0.8)
#选择护照
    driver.find_element_by_name('idType').click()

    time.sleep(0.8)
    driver.find_element_by_name('acceptIeltsTermsAndConditions').click()
    time.sleep(0.8)
    driver.find_element_by_xpath("//button[@class='btn btn-primary'][text()='Pay Now']").click()
    WebDriverWait(driver, 15, 0.5).until(EC.presence_of_element_located((By.ID, 'btn-pay-by-paypal')))
    payId = driver.current_url
    print(payId)
    return payId[-46:]





    # driver.close()
# get_token("intilrx@163.com","Yasi12345678", '345678','123456789012345678','Afghanistan','1','2021-09-15T07:00:00Z','2021-09-13T17:20:00Z')

# 获取sessionid
def get_sessionid(self):
    # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
    # window.sessionStorage和直接写sessionStorage是等效的
    # 一定要使用return，不然获取到的一直是None
    # get的Item不一定就叫sessionId，得具体看目标系统把sessionid存到哪个变量中
    sessionid = self.browser.execute_script('return sessionStorage.getItem("sessionId");')
    # 另外sessionid一般都直接通过返回Set-Cookies头设置到Cookie中，所以也可以从Cookie读取
    # 获取浏览器所有Set-Cookie，返回对象是字典列表
    # cookies = self.browser.get_cookies()
    # 获取单项Cookie，是不是叫sessionId取决于系统存成什么变量，单项Cookie是字典
    # cookie = self.browser.get_cookie("sessionId")
    # cookie = cookie["value"]
    # print(f"{cookies}")
    return sessionid

# 获取token
def get_tokens(self):
    # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
    # window.sessionStorage和直接写sessionStorage是等效的
    # 一定要使用return，不然获取到的一直是None
    # get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中
    token = self.browser.execute_script('return localStorage.getItem("persist:root");')
    # print(f"{token}")
    return token

