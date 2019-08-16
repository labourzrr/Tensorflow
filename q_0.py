#coding:utf-8
#-*- coding:utf-8 -*-
from database import q_db
from selenium import webdriver
import warnings
import time
import ran

warnings.simplefilter("ignore", ResourceWarning)
# 39.137.77.66:8080

option = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' : {
        'images' : 2
    }
}
option.add_experimental_option('prefs',prefs)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("--start-maximized")
option.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
# option.add_argument("--proxy-server=http://127.0.0.1:8080")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(30)

driver.get("http://hotel.qunar.com/city/nanchang/#fromDate=2019-03-16&cityurl=nanchang&from=qunarHotel&toDate=2019-03-17")

# driver.find_element_by_xpath('//a[@id="__headerInfo_login__"]').click()
# driver.find_element_by_xpath('//a[@class="pwd-login"]').click()
#
# # 登录
# driver.find_element_by_xpath('//input[@name="username"]').send_keys("13576108120")
# driver.find_element_by_xpath('//input[@name="password"]').send_keys("y0000000")
# check = input("验证码：")
# driver.find_element_by_xpath('//input[@name="vcode"]').send_keys(check)
# driver.find_element_by_xpath('//input[@class="new-login-btn"]').click()
# time.sleep(2)

time.sleep(2)
driver.find_element_by_xpath('//input[@title="只看有房"]').click()
time.sleep(2)

db = q_db()
max_id = db.max_id()

while True:
    #滚动条下拉到底部
    js="var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)
    js="var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)

    names = driver.find_elements_by_xpath('//a[@class="e_title js_list_name"]')
    links = driver.find_elements_by_xpath('//a[@class="e_title js_list_name"]')
    locations = driver.find_elements_by_xpath('//span[@class="area_contair"]')
    prices = driver.find_elements_by_xpath('//p[@class="item_price js_hasprice"]//b')

    for i in range(len(names)):
        max_id += 1

        # print(names[i].text + " " + links[i].get_attribute('href') + " " + locations[i].text.strip().replace("\n", "") + " " + prices[i].text)
        # try:
        #     db.insert_q_list(names[i].text, links[i].get_attribute('href'))
        #     db.insert_q_detail(max_id, names[i].text, locations[i].text.strip().replace("\n", ""), prices[i].text)
        # except:
        #     continuetry:
        #     db.insert_q_list(names[i].text, links[i].get_attribute('href'))
        #     db.insert_q_detail(max_id, names[i].text, locations[i].text.strip().replace("\n", ""), prices[i].text)
        # except:
        #     continue

    try:
        driver.find_element_by_xpath('//a[@class="num icon-tag"]').click()
        time.sleep(3)
    except:
        break;

db.close_q()

