from flask import Flask
import pymysql

app = Flask(__name__)

pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="user_system",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def home():
    return 'deu bom'

if __name__ == '__main__':
    app.run(debug=True)