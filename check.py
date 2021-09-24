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

allCountryMap = {'Afghanistan': 140, 'Albania': 1, 'Algeria': 128, 'Angola': 129, 'Argentina': 2, 'Armenia': 3, 'Austria': 4, 'Azerbaijan': 5, 'Bahrain': 6, 'Bangladesh': 7, 'Belarus (UKVI only)': 254, 'Belgium': 8, 'Benin Republic': 
142, 'Bhutan': 130, 'Bosnia and Herzegovina': 10, 'Botswana': 115, 'Brazil': 11, 'Brunei Darussalam': 12, 'Bulgaria': 13, 'Burundi': 171, 'Cambodia': 149, 'Cameroon': 14, 'Canada': 15, 'Chile': 16, 'China': 17, 'Colombia': 18, 'Congo, the Democratic Republic of the': 179, "Cote d'Ivoire": 181, 'Croatia': 20, 'Cuba': 21, 'Cyprus': 22, 'Czech Republic': 95, 'Denmark': 23, 'Djibouti': 134, 'Dominican Republic': 184, 'Ecuador': 125, 'Egypt': 24, 'El Salvador': 143, 'Ethiopia': 27, 'Faroe Islands': 187, 'Finland': 28, 'France': 29, 'Georgia': 30, 'Germany': 31, 'Ghana': 32, 'Greece': 33, 'Guernsey': 252, 'Hong Kong': 34, 'Hungary': 35, 'India': 36, 'Indonesia': 37, 'Iraq': 118, 'Ireland': 75, 'Isle of Man': 251, 'Israel': 39, 'Italy': 40, 'Jamaica': 41, 'Japan': 42, 'Jersey': 253, 'Jordan': 43, 'Kazakhstan': 44, 'Kenya': 45, 'Kosovo': 109, 'Kuwait': 47, 'Latvia': 48, 'Lebanon': 49, 'Lesotho': 207, 'Liberia': 208, 'Lithuania': 51, 'Luxembourg': 111, 'Macao': 209, 'Madagascar': 121, 'Malawi': 119, 'Malaysia': 53, 'Maldives': 151, 'Malta': 54, 'Mauritania': 213, 'Mauritius': 55, 'Mexico': 56, 'Mongolia': 57, 'Montenegro': 110, 'Morocco': 58, 'Mozambique': 108, 'Myanmar': 59, 'Namibia': 60, 'Nepal': 61, 'Netherlands': 62, 'New Zealand': 63, 'Nigeria': 64, 'North Macedonia': 52, 'Norway': 65, 'Oman': 66, 'Pakistan': 67, 'Panama': 126, 'Paraguay': 69, 'Peru': 70, 'Poland': 72, 'Portugal': 73, 'Qatar': 74, 'Romania': 77, 'Rwanda': 120, 'Saudi Arabia': 79, 'Serbia': 81, 'Singapore': 82, 'Slovakia': 83, 'Slovenia': 84, 'Somalia': 237, 'South Africa': 85, 'South Korea': 46, 'Spain': 86, 'Sri Lanka': 87, 'Swaziland': 240, 'Sweden': 89, 'Switzerland': 90, 'Tajikistan': 131, 'Tanzania': 93, 'Thailand': 94, 'Trinidad and Tobago': 127, 'Turkey': 97, 'Turkmenistan': 132, 'Uganda': 98, 'Ukraine': 99, 'United Arab Emirates': 100, 'United Kingdom': 101, 'United States of America': 136, 'Uzbekistan': 103, 'Venezuela': 104, 'Vietnam': 105, 'Zambia': 106, 'Zimbabwe': 107}
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

        if item[6] not in allCountryMap :
            print("考试国家输入错误!!!")
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