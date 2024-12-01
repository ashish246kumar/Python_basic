import pymysql as connector

class Department:
    def __init__(self):
        query='create table if not exists department(department_id int primary key,department_name varchar(200))'
        self.conn=connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='microservices')
        self.cursor=self.conn.cursor()
        self.cursor.execute(query)
        print("created")

    def insertValue(self,departmentId,department_name):
        query="insert into department(department_id,department_name)values('{}','{}')".format(departmentId,department_name)
        self.cursor.execute(query)
        self.conn.commit()



department=Department()
department.insertValue(2,"cse")
