import pymysql as connector
class DBHelper:
    def __init__(self):
        self.conn=connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='microservices')
        query='create table if not exists user(userId int primary key,name varchar(200))'
        
        self.cursor=self.conn.cursor()
        self.cursor.execute(query)
        # alterQuery='ALTER TABLE USER ADD COLUMN department_id int'
        # self.cursor.execute(alterQuery)

        print("created")
    def insert_user(self,userId,name):
        query="insert into user(userId,name) values('{}','{}')".format(userId,name)
        self.cursor.execute(query)
        self.conn.commit()
    def get_user(self):
        # query="select * from user"
        query1="select u.userId,u.name,d.department_name from user u INNER JOIN department d on u.department_id=d.department_id"
        # self.cursor.execute(query)
        self.cursor.execute(query1)
        print(self.cursor)
        for row in self.cursor:
            print(row[0],row[1],row[2])

    def delete_user(self,userId):
        query="delete from user where userId={}".format(userId)
        self.cursor.execute(query)
        self.conn.commit()
        print("deleted successfully")

    def update_user(self,id,name):
        query="update user set name='{}' where userId={}".format(name,id)
        self.cursor.execute(query)
        self.conn.commit()
        print("updated successfully")
            
dbhelper=DBHelper()
# dbhelper.insert_user(1,"Rahul")
# dbhelper.insert_user(2,"Ram")

dbhelper.get_user()
# dbhelper.delete_user(2)
# dbhelper.update_user(1,"Rahul2")
