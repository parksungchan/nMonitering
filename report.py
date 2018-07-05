# pip install PyMySQL
import pymysql

# Connect to the database
conn = pymysql.connect(host='211.177.122',
                             user='hee',
                             password='!',
                             db='',
                             charset='utf8mb4')

curs = conn.cursor(pymysql.cursors.DictCursor)

# ==== select example ====
sql = " SELECT * from flybeach.keyword "
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
print(rows)

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

# 1. 제어판->보안 ->방화벽-> 방화벽 활성화 체크 하고 좌측 아래 규칙편집 -> 생성 클릭ㅜ 내장ㅣㄴ응용 프로램목록에서 선택 하고 선택 ->
#    MySQL 데이베이스 선택하고확인
# 2. 외부엑세스->라우터구성->커스텀->TCP, 3306, 3306 적용
