from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#浏览器模式设置
chrome_options=Options()
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
    # time.sleep(5)
# 　　#获取token的方法：
# 　　''' 
#    1、要从Local Storage中获取还是要从Session Storage中获取，具体看目标系统存到哪个中-----开发者模式查看
#    2、window.SessionStorage和直接写SessionStorage是等效的
#    3、一定要使用return，不然获取到的一直是None
#    4、get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中
# 　　'''
    token = driver.execute_script('return localStorage.getItem("client_id");')
    print("token::",token)
    # driver.close()
    return token

get_token("intilrx@163.com","Yasi12345678")