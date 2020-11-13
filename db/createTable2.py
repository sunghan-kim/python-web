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
        sql = """
        CREATE TABLE test_table2 (
        idx INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(256) NOT NULL,
        nick VARCHAR(256) NOT NULL
        );
        """
        cursor.execute(sql)
        db.commit()
finally:
    db.close()
