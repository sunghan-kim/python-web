import pymysql

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='shkim',
    passwd='ksh1004',
    db='python-db',
    charset='utf8'
)

try:
    with db.cursor() as cursor:
        sql = """SELECT * FROM test_table"""
        cursor.execute(sql)
        # SQL query 실행 결과를 가져옴
        # 데이터가 여러 개일 경우 fetchall() 사용
        result = cursor.fetchall()
        # 데이터가 한 개일 경우 fetchone() 사용
        # result = cursor.fetchone()
        print(result)
finally:
    db.close()