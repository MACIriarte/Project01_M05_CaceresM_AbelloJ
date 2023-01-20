import random
import pymysql
import pymysql.cursors
from dictionaries import *
from functions import *

connection = pymysql.connect(
    host='13.69.10.32',
    user='alumno',
    password='123456789Abc',
    db='db_game',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cur = connection.cursor()

cur.execute(
    ""
)

mainprogram()