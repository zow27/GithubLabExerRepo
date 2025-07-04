import sqlite3

db_path = r"C:\Users\Clems\OneDrive\Desktop\shared folder\sample.db"


conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("INSERT INTO students (name, course) VALUES (?, ?)", ("Ella", "Data Science"))

conn.commit()
print("Student added successfully.")
conn.close()
