# pip install PyMySQL
import pymysql, os
import crolling
common_path = crolling.common_path
key_value_file = common_path + '/' + 'key_value.py'
if not os.path.exists(key_value_file):
    with open(key_value_file, 'w') as f:
        f.write("host='0.0.0.0'\n")
        f.write("port=3307\n")
        f.write("user='hee'\n")
        f.write("password=''\n")
        f.write("db=''\n")
        f.write("charset='utf8mb4'\n")
from common import key_value as key_value
print(key_value.host)
print(key_value.port)
print(key_value.user)
print(key_value.password)
print(key_value.db)
print(key_value.charset)

print(key_value.host)

import urllib
import pymysql
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Open database connection
db = pymysql.connect(host=key_value.host
                     , port=key_value.port
                     , user=key_value.user
                     , passwd=key_value.password
                     , db=key_value.db
                     , charset=key_value.charset
                     , autocommit=True)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Database version : %s " % data)

# disconnect from server
db.close()

# # Connect to the database
# conn = pymysql.connect(host=key_value.host,
#                              user=key_value.user,
#                              password=key_value.password,
#                              db=key_value.db,
#                              charset=key_value.charset)
#
# None
# curs = conn.cursor(pymysql.cursors.DictCursor)
#
# # ==== select example ====
# sql = " SELECT * from flybeach.keyword "
# curs.execute(sql)
#
# # 데이타 Fetch
# rows = curs.fetchall()
# print(rows)

# # ==== insert example ====
# sql = """insert into customer(name,category,region)
#          values (%s, %s, %s)"""
# curs.execute(sql, ('홍길동', 1, '서울'))
# curs.execute(sql, ('이연수', 2, '서울'))
# conn.commit()
#
# # ==== update OR delete example ====
# sql = """update customer
#          set region = '서울특별시'
#          where region = '서울'"""
# curs.execute(sql)
#
# sql = "delete from customer where id=%s"
# curs.execute(sql, 6)
#
# conn.commit()

# 1. 제어판->보안 ->방화벽-> 방화벽 활성화 체크 하고 좌측 아래 규칙편집 -> 생성 클릭 내장응용 프로램목록에서 선택 하고 선택 ->
#    MySQL 데이베이스 선택하고확인
# 2. 외부엑세스->라우터구성->커스텀->TCP, 3306, 3306 적용
