#coding:utf-8
# -*- coding:utf-8 -*-
import pymysql  # 供python3使用

class q_db:
    def __init__(self):
        # 数据库配置信息
        self.DATABASE = {
            "host": "127.0.0.1",
            "database": "hotel",
            "user": "root",
            "password": "8627139"
        }

        self.db = pymysql.connect(**self.DATABASE)


    def close_q(self):
        self.db.close()


    def insert_q_list(self, hotel_name , link):
        cursor = self.db.cursor()  # 游标
        sql = "insert into q_list VALUES ('"+ hotel_name +"','"+ link +"')"
        cursor.execute(sql)
        self.db.commit()


    def insert_q_detail(self, new_id, hotel_name, location, price):
        cursor = self.db.cursor()
        sql = "insert into q_detail (id, hotel_name, location, price) VALUES ("+ str(new_id) + ", '"+ hotel_name + "', '" + location + "', " +  str(price) + ")"
        # print(sql + ";")
        cursor.execute(sql)
        self.db.commit()


    def max_id(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT LAST_INSERT_ID()")
        result = cursor.fetchall()
        max_id = 0
        if result[0][0] != None:
            max_id = result[0][0]
        return max_id


    def complete_q_detail(self, id, feature, score, picture_link, phone, information, introduction, service, comments_good, comments_medium, comments_bad):
        cursor = self.db.cursor()
        sql = "update q_detail set feature = '" + feature + "', score = " + str(score) + ", picture_link = '" + picture_link + "', phone = '" + phone + "', information =  '" + information + "', introduction = '" + introduction + "', service = '" + service + "', comments_good = " + str(comments_good) + ", comments_medium =  " + str(comments_medium )+ ", comments_bad = " + str(comments_bad) +" where id = " + str(id)

        cursor.execute(sql)
        self.db.commit()


    def insert_q_comments(self, hotel_id, comment_title, comment_score, comment_text):
        cursor = self.db.cursor()
        sql = "insert into q_comments values (" + str(hotel_id) + ", '"+ comment_title + "', " + str(comment_score) + ", '" + comment_text +"')"

        cursor.execute(sql)
        self.db.commit()


    def get_q_list(self, id_queue, link_queue, index):
        cursor = self.db.cursor()
        sql = "select id, link from q_list limit " + str(index) + ",10"

        rows_count = cursor.execute(sql)
        results = cursor.fetchall()
        if rows_count > 0:
            for result in results:
                id_queue.put(result[0])
                link_queue.put(result[1])
            return index + 10
        else:
            return -1


    def insert_x_list(self, hotel_name, link):
        cursor = self.db.cursor()  # 游标
        sql = "insert into x_list VALUES ('" + hotel_name + "','" + link + "')"

        cursor.execute(sql)
        self.db.commit()


    def insert_x_detail(self, hotel_name, location, picture_link, price):
        cursor = self.db.cursor()
        sql = "insert into x_detail (hotel_name, location, picture_link, price) VALUES ('" + hotel_name + "', '" + location + "', '" + picture_link + "', " + str(price) + ")"

        cursor.execute(sql)#执行sql语句
        self.db.commit()


    def get_x_list(self, id_queue, link_queue, index):
        cursor = self.db.cursor()
        sql = "select id, link from x_list limit " + str(index) + ",10"

        rows_count = cursor.execute(sql)
        results = cursor.fetchall()
        if rows_count > 0:
            for result in results:
                id_queue.put(result[0])
                link_queue.put(result[1])
            return index + 10
        else:
            return -1


    def complete_x_detail(self, id, feature, score, information, introduction, service, score_location, score_facility, score_service, score_health):
        cursor = self.db.cursor()
        sql = "update x_detail set feature = '" + feature + "', score = " + str(score) + ", information =  '" + information + "', introduction = '" + introduction + "', service = '" + service + "', score_location = " + str(score_location) + ", score_facility =  " + str(score_facility)+ ", score_service = " + str(score_service) + ", score_health = " + str(score_health) + " where id = " + str(id)
        print(sql)
        cursor.execute(sql)
        self.db.commit()


    def insert_x_comments(self, hotel_id, comment_score, comment_text, comment_date):
        cursor = self.db.cursor()
        sql = "insert into x_comments values (" + str(hotel_id) + ", "+ str(comment_score) + ", '" + comment_text + "', '" + comment_date +"')"
        # print(sql)
        cursor.execute(sql)
        self.db.commit()
