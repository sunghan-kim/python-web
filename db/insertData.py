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
        INSERT INTO test_table
        (name, nick)
        VALUES
        ('test_name', 'test_nickname');
        """
        cursor.execute(sql)
        db.commit()
finally:
    db.close()
