import pymysql
import pymysql.cursors
import pymysql.connections

from app.database.config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("EEEEEEEEEEEEEE")
except Exception as ex:
    print("FFFFFFFFFFFFFFFFFFFFFFF")
    print(ex)
