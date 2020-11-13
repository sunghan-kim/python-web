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
        UPDATE test_table
           SET name='%s',
               nick='%s'
         WHERE name='%s'
        """ % ('new_test', 'new_nick', 'test_name')

        cursor.execute(sql)
        db.commit()
finally:
    db.close()