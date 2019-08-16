#coding:utf-8
# -*- coding:utf-8 -*-

from database import q_db
from queue import Queue
from selenium import webdriver
import warnings
import time
import random

warnings.simplefilter("ignore", ResourceWarning)
# 39.137.77.66:8080
# 62.234.122.142:16819

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

option.add_argument("--proxy-server=http://62.234.122.142:16819")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(15)

with open("q_cookies.txt") as f:
    text = f.read()
    cc = text.replace(" ","").split(";")

driver.get("http://hotel.qunar.com/city/nanchang/")
for c in cc:
    cookie = {
        "domian": "hotel.qunar.com",
        "name": c.split("=")[0],
        "value": c.split("=")[1],
        "expires": "",
        "path": "/",
        "httpOnly": False,
        "HostOnly": False,
        "Secure": False
    }
    driver.add_cookie(cookie)

# driver.find_element_by_xpath('//input[@title="只看有房"]').click()
time.sleep(random.random()*2)

db = q_db()
index = 495  # 当前读取位置索引
id_queue = Queue(10)  # id队列
link_queue = Queue(10)  # 链接队列

while index != -1:
    index = db.get_q_list(id_queue, link_queue, index)
    while not id_queue.empty():
        id = id_queue.get()
        link = link_queue.get()
        # print(str(id) + link)
        try:
            driver.get(link)
        except:
            driver.refresh()
            driver.get(link)
        finally:
            driver.refresh()
            driver.get(link)

        time.sleep(1 + random.random()*2)
        js="var q=document.documentElement.scrollTop=1500"
        driver.execute_script(js)
        time.sleep(random.random()*1)
        js = "var q=document.documentElement.scrollTop=1500"
        driver.execute_script(js)
        time.sleep(random.random()*1)

        try:
            score = driver.find_element_by_xpath('//div[@id="headerUgc"]/div/p[@class="score"]/span[@class="num"]/em').text
        except:
            score = 0

        try:
            feature = driver.find_element_by_xpath('//div[@id="headerUgc"]/div/div[contains(@class,"comment")]/p').text.split("\n")[1]
        except:
            feature = driver.find_element_by_xpath('//div[@id="headerUgc"]/div/div[contains(@class,"comment")]').text.strip()

        try:
            picture_link = driver.find_element_by_xpath('//div[@id="headImage"]//div[@class="img-head"]/img').get_attribute('src')
        except:
            picture_link = ""

        phone = driver.find_elements_by_xpath('//div[@class="dt-module"]/dl/dd')[0].text
        information = driver.find_elements_by_xpath('//div[@class="dt-module"]/dl/dd')[1].text
        introduction = driver.find_elements_by_xpath('//div[@class="dt-module"]/dl/dd')[2].text
        service = driver.find_element_by_xpath('//div[@class="dt-module dt-module-last"]').text.replace("\n", "")
        comments = driver.find_element_by_xpath('//span[@class="num js_commentCount"]').text.replace("（", "").replace("）", "")

        if comments != str(0):
            comments_good = driver.find_element_by_xpath('//span[@class="count js_positiveCount"]').text.replace("(", "").replace(")", "")
            comments_medium = driver.find_element_by_xpath('//span[@class="count js_neutralCount"]').text.replace("(", "").replace(")", "")
            comments_bad = driver.find_element_by_xpath('//span[@class="count js_negativeCount"]').text.replace("(", "").replace(")", "")

            comments_titles = driver.find_elements_by_xpath('//p[@class="ct-title"]')
            comments_scores = driver.find_elements_by_xpath('//p[@class="num"]')
            comments_texts = driver.find_elements_by_xpath('//p[@class="js_contentAll"]')

            # for i in range(len(comments_titles)):
            #     try:
            #         db.insert_q_comments(id, comments_titles[i].text, comments_scores[i].text, comments_texts[i].text[:500])
            #     except:
            #         continue

        else:
            comments_bad, comments_medium, comments_good = 0, 0, 0

        try:
            db.complete_q_detail(id, feature, score, picture_link, phone, information, introduction[:500], service, comments_good, comments_medium, comments_bad)
        except:
            continue

