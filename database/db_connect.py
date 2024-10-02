import mysql.connector
from mysql.connector import errorcode


DB_NAME='TradeNotes'

DB_CONFIG = {
    'user': 'root',
    'password': 'P@55word',
    'host': 'localhost',
    'database': 'TradeNotes'
}

def create_dbconnec(DB_CONFIG):
    try :
        db = mysql.connector.connect(**DB_CONFIG)

        return db

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something wrong with username or password")
            return
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("DB does not exist")
        else:
            print(err)

    else:
        db.close()





