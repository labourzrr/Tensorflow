import pymysql #供python3调用mysql函数

class q_db:
    def __init__(self):
        #数据库配置信息
        self.DATABASE = {
            "host" : "localhost",
            "database" : "hotel",
            "user" : "root",
            "password" : "8627139"
        }
        self.db = pymysql.connect(**self.DATABASE)


    def close_q(self):
        self.db.close()

    def insert_q_list(self,hotel_name,link):
        cursor = self.db.cursor() #游标
        sql = "insert into q_list VALUES('" + hotel_name +"','" + link +"')"
        cursor.execute(sql) #cursor执行sql语句
        self.db.commit() #提交数据

    def insert_q_detail(self,new_id,hotel_name,location,price):
        cursor = self.db.cursor() #游标
        sql = "insert into q_detail(id,hotel_name,location,price) VALUES(" + str(new_id) +",'"+ hotel_name +"','"+ location +"'," + str(price) +")"
        cursor.execute(sql) #cursor执行sql语句
        self.db.commit() #提交数据

    def max_id(self):
        cursor = self.db.cursor() #游标
        cursor.execute("SELECT LAST_INSERT_ID()")#cursor执行语句
        result = cursor.fetchall()
        max_id = 0
        if result[0][0] != None:
            max_id = result[0][0]
        return max_id

    def complet_q_detail(self,id,feature,score,picture_link,phone,information,introduction,service,comments_good,comments_medium,comments_bad):
        cursor = self.db.cursor() #游标
        sql = "updata q_detail set feature = '"+ feature +"', score = " +str(score) +",picture_link = '"+ picture_link +"',phone = "+ str(phone) +",information = '"+ information +"',introduction = '"+ introduction +"',service = '"+ service +"',"
        cursor.execute(sql) #cursor执行sql语句
        self.db.commit() #提交数据

    def insert_q_comments(self,hotel_id,comment_title,comment_score,comment_text):
        cursor = self.db.cursor() #游标
        sql = "insert into q_comments values ("+ str(hotel_id)+",'"+ comment_title +"', '"+ comment_score +"','"+ comment_text +"' )"
        cursor.execute(sql)#cursor执行sql语句
        self.db.commit() #提交数据

    def get_q_list(self,id_queue,link_queue,index):
        cursor = self.db.cursor() #游标
        sql = "select id, link from q_list limit" + str(index) +",10"

        rows_count = cursor.execute(sql)
        results = cursor.fetchall() #fetchall()返回值是多个元组,即返回多个行记录,如果没有结果,返回的是()
        if rows_count > 0:
            for result in results:
                id_queue.put(result[0])
                link_queue.put(result[1])
            return index + 10
        else:
            return -1

    def insert_x_list(self, hotel_name, link):
        cursor = self.db.cursor()  # 游标
        sql = "insert into x_list VALUES('" + hotel_name + "','" + link + "')"
        cursor.execute(sql)  # cursor执行sql语句
        self.db.commit()  # 提交数据

    def insert_x_detail(self, new_id, hotel_name, location, price):
        cursor = self.db.cursor()  # 游标
        sql = "insert into x_detail(id,hotel_name,location,price) VALUES(" + str(
            new_id) + ",'" + hotel_name + "','" + location + "'," + str(price) + ")"
        cursor.execute(sql)  # cursor执行sql语句
        self.db.commit()  # 提交数据


    def complet_x_detail(self, id, feature, score, picture_link, phone, information, introduction, service,
                         comments_good, comments_medium, comments_bad):
        cursor = self.db.cursor()  # 游标
        sql = "updata x_detail set feature = '" + feature + "', score = " + str(
            score) + ",picture_link = '" + picture_link + "',phone = " + str(
            phone) + ",information = '" + information + "',introduction = '" + introduction + "',service = '" + service + "',"
        cursor.execute(sql)  # cursor执行sql语句
        self.db.commit()  # 提交数据

    def insert_x_comments(self, hotel_id, comment_title, comment_score, comment_text):
        cursor = self.db.cursor()  # 游标
        sql = "insert into x_comments values (" + str(
            hotel_id) + ",'" + comment_title + "', '" + comment_score + "','" + comment_text + "' )"
        cursor.execute(sql)  # cursor执行sql语句
        self.db.commit()  # 提交数据

    def get_x_list(self, id_queue, link_queue, index):
        cursor = self.db.cursor()  # 游标
        sql = "select id, link from x_list limit" + str(index) + ",10"

        rows_count = cursor.execute(sql)
        results = cursor.fetchall()  # fetchall()返回值是多个元组,即返回多个行记录,如果没有结果,返回的是()
        if rows_count > 0:
            for result in results:
                id_queue.put(result[0])
                link_queue.put(result[1])
            return index + 10
        else:
            return -1






