
#coding:utf-8
# -*- coding:utf-8 -*-

from database import q_db
from string import digits
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import warnings
import time
import random

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
# option.add_argument("--proxy-server=http://39.137.77.66:8080")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

driver.get("https://hotels.ctrip.com/hotel/nanchang376")
advertise = True

db = q_db()

# 爬前40面
for times in range(39):
    time.sleep(1 + random.random()*1)
    js="var q=document.documentElement.scrollTop=6000"
    driver.execute_script(js)
    time.sleep(1 + random.random()*2)

    if advertise:
        # 关闭第一页广告
        driver.find_element_by_xpath('//a[@class="fl_wrap_close"]').click()
        advertise = False

    driver.find_element_by_class_name('c_down').send_keys(Keys.ENTER)

    hotel_names = driver.find_elements_by_xpath('//h2[@class="hotel_name"]/a')
    links = driver.find_elements_by_xpath('//h2[@class="hotel_name"]/a')
    locations = driver.find_elements_by_xpath('//p[@class="hotel_item_htladdress"]')
    picture_links = driver.find_elements_by_xpath('//div[@class="dpic J_as_bottom"]/img')
    prices = driver.find_elements_by_xpath('//span[@class="J_price_lowList"]')

    for i in range(len(hotel_names)):
        hotel_name = hotel_names[i].text.replace("精选 ", "")
        remove_digits = str.maketrans('', '', digits)
        hotel_name = hotel_name.translate(remove_digits)
        print(hotel_name)

        link = links[i].get_attribute("href")
        print(link)

        location = locations[i].text.replace("地图", "").replace("街景", "")
        print(location)

        picture_link = picture_links[i].get_attribute("src")
        print(picture_link)

        price = prices[i].text
        print(price)

        # db.insert_x_list(hotel_name, link)
        # db.insert_x_detail(hotel_name, location, picture_link, price)


# 52qgasn3
