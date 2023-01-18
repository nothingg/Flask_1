import psycopg2

conn = psycopg2.connect(
            database = "studentdb",
            user = "postgres",
            password = "password",
            host = "localhost",
            port = "5432")

cur = conn.cursor()
cur.execute("SELECT * FROM student")
rows = cur.fetchall()

for row in rows:
    print("fName :", row[1])

conn.close()