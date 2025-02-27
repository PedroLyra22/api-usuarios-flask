import pymysql

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "user_system",
}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)