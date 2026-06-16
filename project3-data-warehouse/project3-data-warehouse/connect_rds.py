import pymysql

conn = pymysql.connect(
    host    = 'YOUR-RDS-ENDPOINT',
    user    = 'admin',
    password= 'YOUR-PASSWORD',
    database= 'decodelabs'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM Interns")
rows = cursor.fetchall()

print("--- Interns Table ---")
for row in rows:
    print(row)

conn.close()
