# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options=Options()
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
# chrome_options.add_experimental_option("detach", True)
# # chrome_options.add_argument('--headless')

# driver = webdriver.Chrome(chrome_options=chrome_options)
# url = "https://eamidentity.britishcouncil.org/account/login?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dieltsindicator.b2c.app%26redirect_uri%3Dhttps%253A%252F%252Fieltsindicator.britishcouncil.org%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520email%2520ieltsindicator.b2c.api%2520registrantid%2520offline_access%26state%3D24dfa24d12514ac0b5bc0e0de3d0774d%26code_challenge%3DO-hwSD9dU0mEyPwG43vnBkxZjWBiblXxbNm5GfY3Z0c%26code_challenge_method%3DS256%26response_mode%3Dquery"
# driver.implicitly_wait(5) # seconds
# driver.get(url)
# driver.find_element_by_id("Username").send_keys("123")
# driver.find_element_by_id("password_login").send_keys("123")

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
chane()