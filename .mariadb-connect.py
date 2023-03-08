import pymysql.cursors
 
# Connect to the database
connection = pymysql.connect(
        host='localhost',
        user='root',
        password='hoge',
        db='pengin',
        port = 3307,
        charset='utf8mb4'
        )


with connection.cursor() as cursor:
        sql = "INSERT INTO drink (id, name) VALUES (%s, %s)"
        r = cursor.execute(sql, (4, "soda"))
        print(r) # -> 1
        # autocommitではないので、明示的にコミットする
        connection.commit()

connection.commit()



connection.close()
print("PythonからMariaDBに接続できました。")