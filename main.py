from dictionaries import *
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='12345678',
    db='db_game',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

mainprogram()