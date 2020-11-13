import pymysql

# database 접근
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='shkim',
    passwd='ksh1004',
    db='python-db',
    charset='utf8'
)

# database를 사용하기 위한 cursor 세팅
cursor = db.cursor()

# SQL query 작성
sql = """
CREATE TABLE test_table (
idx INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL,
nick VARCHAR(256) NOT NULL
);
"""

# SQL query 실행
cursor.execute(sql)

# query가 잘 실행됬는 지 확인
cursor.execute("show tables")

db.commit()

db.close()