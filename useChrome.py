from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


import time
#浏览器模式设置
chrome_options=Options()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

# chrome_options.add_argument('--headless')
"""最终的效果：不会弹出浏览器窗口"""

driver = webdriver.Chrome(chrome_options=chrome_options)
url = "https://eamidentity.britishcouncil.org/account/login?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dieltsindicator.b2c.app%26redirect_uri%3Dhttps%253A%252F%252Fieltsindicator.britishcouncil.org%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520email%2520ieltsindicator.b2c.api%2520registrantid%2520offline_access%26state%3D24dfa24d12514ac0b5bc0e0de3d0774d%26code_challenge%3DO-hwSD9dU0mEyPwG43vnBkxZjWBiblXxbNm5GfY3Z0c%26code_challenge_method%3DS256%26response_mode%3Dquery"


def get_token(username, password):
# 　　操作浏览器，打开url，用户名密码登陆
    driver.get(url)
    driver.find_element_by_id("Username").send_keys(username)
    driver.find_element_by_id("password_login").send_keys(password)
    driver.find_element_by_id("password_login").submit()
    time.sleep(1)
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
    e.send_keys("Afghanistan")
    e.send_keys(Keys.ENTER)
    #选择时间
    # c = driver.find_element_by_tag_name('abbr')
    # c = driver.find_element_by_css_selector('button.react-calendar__tile react-calendar__month-view__days__day available-day')
    # print(c)
    time.sleep(1.5)
    #test data
    driver.find_element_by_xpath("//abbr[@aria-label='September 15, 2021'][text()='15']").click()
    time.sleep(1)


    elements =  driver.find_elements_by_xpath("//abbr[@aria-label='September 14, 2021'][text()='14']")

    
    driver.find_elements_by_xpath("//div[@class='react-calendar__tile react-calendar__month-view__days__day available-day']/abbr[@aria-label='September 15, 2021'][text()='15']")
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
    e.send_keys("17:20")
    e.send_keys(Keys.ENTER)
    # driver.find_element_by_tag_name("button.react-calendar__tile react-calendar__month-view__days__day available-day").click()
    # driver.get("https://ieltsindicator.britishcouncil.org/personal-details")
    
    # return token
    time.sleep(1)

    driver.find_element_by_xpath("//button[@class='btn btn-link'][text()='I already have an account']").click()
    time.sleep(1)
    token = driver.execute_script('return localStorage.getItem("persist:root");')
    print(token)
    return





    # driver.close()
get_token("intilrx@163.com","Yasi12345678")

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
def get_token(self):
    # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
    # window.sessionStorage和直接写sessionStorage是等效的
    # 一定要使用return，不然获取到的一直是None
    # get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中
    token = self.browser.execute_script('return sessionStorage.getItem("token");')
    # print(f"{token}")
    return token
