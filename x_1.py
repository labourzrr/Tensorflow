#coding:utf-8
# -*- coding:utf-8 -*-
from database import q_db
from queue import Queue
from string import digits
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import warnings
import time
import rando


warnings.simplefilter("ignore", ResourceWarning)

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
# option.add_argument("--proxy-server=http://152.136.76.173:16819")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

db = q_db()
index = 972   # 当前读取位置索引
id_queue = Queue(10)  # id队列
link_queue = Queue(10)  # 链接队列

advertise = True

while index != -1:
    index = db.get_x_list(id_queue ,link_queue, index)
    while not id_queue.empty():
        id = id_queue.get()
        link = link_queue.get()
        # print(str(id) + link)

        driver.get(link)
        time.sleep(1 + random.random()*1)

        if advertise:
            # 关闭第一页广告
            driver.find_element_by_xpath('//a[@class="fl_wrap_close"]').click()
        advertise = False

        try:
            feature = driver.find_element_by_xpath('//div[@class="text"]').text.replace("\n", "")[:499]
        except:
            feature = ""
        try:
            score = driver.find_element_by_xpath('//p[@class="s_row"]/span[@class="score"]').text
        except:
            score = 0

        js = "var q=document.documentElement.scrollTop=6000"
        driver.execute_script(js)
        time.sleep(1 + random.random() * 1)

        information = driver.find_element_by_xpath('//div[@id="htlDes"]/p').text.replace("联系方式 住宿预订提供方", "")
        introduction = driver.find_element_by_xpath('//div[@id="htlDes"]//span[@itemprop="description"]').text.replace("\n", "")
        service_list = driver.find_elements_by_xpath('//tr[@data-init="1"]')
        service = ""
        for i in range(len(service_list)):
            service += service_list[i].text
            service = service.replace("\n", "")
        try:
            score_lfsh = driver.find_elements_by_xpath('//div[@class="bar_score"]/p/span')
            for i in range(4):
                score_location = score_lfsh[0].text
                score_facility = score_lfsh[1].text
                score_service = score_lfsh[2].text
                score_health = score_lfsh[3].text
        except:
            score_location, score_facility, score_service, score_health = 0, 0, 0, 0

        # print(feature + str(score) + information + introduction + service + str(score_location) + str(score_facility) + str(score_service) + str(score_health))
        db.complete_x_detail(id, feature, score, information, introduction, service, score_location, score_facility, score_service, score_health)

        try:
            driver.find_element_by_xpath('//select[@class="select_sort"]/option[@value="1"]').click()
            comment_scores = driver.find_elements_by_xpath('//p[@class="comment_title"]//span[@class="n"]')
            comment_texts = driver.find_elements_by_xpath('//div[@class="J_commentDetail"]')
            comment_dates = driver.find_elements_by_xpath('//span[@class="time"]')
            for i in range(len(comment_scores)):
                comment_score = comment_scores[i].text
                comment_text = comment_texts[i].text
                comment_date = comment_dates[i].text
                # print(comment_score + comment_text + comment_date)
                db.insert_x_comments(id, comment_score, comment_text, comment_date)
        except:
            pass






