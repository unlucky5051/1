import pymysql
from pymysql.cursors import DictCursor

def connection():
    return pymysql.connect(
        host = '10.11.13.118',
        port = 3306,
        user = 'VikV1234_unlucky',
        password = '111111',
        database = 'VikV1234_smartoffice',
        cursorclass = DictCursor
    )