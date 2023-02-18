import mysql.connector as conn

class mysqlconnection:
    def __init__(self,username,password,db_name,table_name):
        self.name = username 
        self.password = password
        self.db_name = db_name
        self.table_name = table_name
        self.mydb = conn.connect(host = 'localhost',user = 'root' ,password = "mysql@123" )
        self.cursor = self.mydb.cursor()
        
    def create_db(self):
        db_query = self.cursor(f"Create database {self.db_name} if not exist")
        return db_query
    
    def create_table(self,table_):
        self.create_db()
        table_query = self.cursor(f"create table {self.table_name}.{self.db_name}"+{self.table})
        return table_query

    def insert_data(self,data):
        self.create_table()
        insert_query = self.cursor(f"insert into {self.table_name}.{self.db_name} values"+{self.data})
        return insert_query