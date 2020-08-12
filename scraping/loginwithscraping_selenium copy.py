from pymongo import MongoClient
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

path = '/home/sundooedu/Downloads/chromedriver_linux64/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(path, chrome_options=chrome_options)

# login
driver.get('http://sdacademy.maniaro.com/teacher/index.php')
driver.implicitly_wait(5)
username = 'otter35'
userpw = '!otter35'
driver.find_element_by_name('strUid').send_keys(username)
driver.find_element_by_name('strPassword').send_keys(userpw)
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.implicitly_wait(5)

# 비즈니스 모델을 활용한 빅데이터 분석 전문가 양성과정 (1회차)
driver.get(
    'http://sdacademy.maniaro.com/teacher/curri/ver5/lecture/index.php?Pcode=1')
driver.implicitly_wait(5)
trs = driver.find_elements_by_xpath("//tr[@class='link_yellow text-c']")

# source = driver.page_source
# soup = BeautifulSoup(source, 'html.parser')
# trs = soup.find_all('tr',class_='link_yellow text-c')

client = MongoClient('mongodb://172.17.0.2:27017/')
mydb = client.mydb						# get Database
for i in range(len(trs)-1):     # without final project
    # charters page
    charterlist = driver.find_elements_by_xpath(
        "//tr[@class='link_yellow text-c']")[i]
    # print(charterlist.get_attribute('innerHTML'))
    source = charterlist.get_attribute('innerHTML')
    soup = BeautifulSoup(source, 'html.parser')
    charter = soup.find_all('td')
    data = {'charter': charter[0].text, 'evaluteway': charter[1].text, 'lecturer': charter[2].text, 'startdate': charter[3].text,
            'enddate': charter[4].text, 'evaldate': charter[5].text, 'missdate': charter[6].text, 'reevaldate': charter[7].text, 'mean': charter[9].text}
    charters_infor = mydb.charters.insert(data)

    charter_click = driver.find_elements_by_xpath(
        "//a[@class='button button-blue']")[i].click()
    driver.implicitly_wait(5)

    # evaluate main page
    # todo

    # 분석회의록 page
    driver.find_elements_by_xpath("//li[@class='floatL tab_off']")[0].click()
    driver.implicitly_wait(5)
    els = driver.find_elements_by_xpath(
        "//td[@class='body_center']/table/tbody/tr[@class='b_fff']/td")
    # print(meeting[1].text)
    data = {'meetdate': els[1].text,
            'content': els[3].text, 'detail': els[5].text}
    meeting_infor = mydb.meeting.insert(data)
    driver.back()   # evaluate main page

    # evaluate list page
    evaluate_list = driver.find_elements_by_xpath(
        "//li[@class='floatL tab_off']")[1]
    # print(evaluate_list.text)
    comparedstr = evaluate_list.text
    evaluate_list.click()
    driver.implicitly_wait(5)

    if comparedstr != '구두발표':
        # evaluate question page
        driver.find_element_by_xpath(
            "//a[@class='button button-blue']").click()
        driver.implicitly_wait(5)
        # questions
        # questionlist = driver.find_elements_by_xpath(
        #     "//tr[@class='link_yellow text-c cur']")
        # for question in questionlist:
        #     els = question.find_elements_by_tag_name("td")
        #     data = {'number': els[1].text,
        #             'question': els[2].text, 'score': els[3].text}
        #     question_infor = mydb.questions.insert(data)

        # print(questions[1].text)
        # currect answers
        answerlist = driver.find_elements_by_xpath("//tr[@class='b_darkgray']/td/div")
        for answer in answerlist:
            source = answer.get_attribute('innerHTML')
            soup = BeautifulSoup(source, 'html.parser')
            subels = soup.select('tr.b_fff.text-l>td')
            # subels = answer.find_elements_by_css_selector('tr.b_fff.text-l td')
            data = {'question': subels[1].text,
                    'answer': subels[3].text, 'standard': subels[5].text}
            answer_infor = mydb.answers.insert(data)
        # print(answerlist.text)

    # driver.back()       # evaluate list page

    # driver.back()   # charters page
    driver.find_elements_by_xpath(
        "//a[@class='button button-black']")[1].click()
    driver.implicitly_wait(5)
    print('charter End!')

client.close()
print('The End!')
