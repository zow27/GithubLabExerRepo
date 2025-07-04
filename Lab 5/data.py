import sqlite3

db_path = r"C:\Users\Clems\OneDrive\Desktop\shared folder\sample.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

conn.close()
