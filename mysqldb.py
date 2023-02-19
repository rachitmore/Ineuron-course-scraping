import mysql.connector
from mysql.connector.constants import ClientFlag

#This class will be used for MySQL database operations
class mysqlconnection:
    """
    This class will be used for MySql database operations 
    and it will take database name and table name
    and will establish connection to Mysql database
    """
    def __init__(self,db_name,table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.mydb = conn.connect({
    'user': 'uebmxkeuemkpvpuc',
    'password': '1qRaxNJll4KA7XzmNbef',
    'host': 'bedtdss1qgi0ejulmur0-mysql.services.clever-cloud.com',
    "database" : "bedtdss1qgi0ejulmur0",
    "port" : "3306",
})
        self.cursor = self.mydb.cursor()
        
    def create_db(self):
        """This function will create database"""
        db_query = self.cursor(f"Create database {self.db_name} if not exist")
        return db_query
    
    def create_table(self,table_):
        """This function will takes one agrument as table schema and create table"""
        self.create_db()
        table_query = self.cursor(f"create table {self.table_name}.{self.db_name}"+{self.table_})
        return table_query

    def insert_data(self,data):
        """This function will takes one argument as data schema and insert value into table"""
        self.create_table()
        insert_query = self.cursor(f"insert into {self.table_name}.{self.db_name} values"+{self.data})
        return insert_query
    
