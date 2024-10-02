from fastapi import FastAPI
from database.db_connect import create_dbconnec, DB_CONFIG 
from database.table import TABLES
from database.sql import SQL
from datetime import datetime

app = FastAPI()



db = create_dbconnec(DB_CONFIG)

cursor = db.cursor()

sql_str = """
SELECT * from users WHERE user_name = "{username}" AND password = "{password}";
"""
print(sql_str.format(username= 'wkh', password= '19980906aB'))

cursor.execute(sql_str.format(username= 'wkh', password= '19980906aB'))
user = cursor.fetchone()
print(user)

cursor.close()
db.close()