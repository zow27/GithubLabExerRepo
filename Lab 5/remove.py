import sqlite3

db_path = r"C:\Users\Clems\OneDrive\Desktop\shared folder\sample.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("DELETE FROM students WHERE name = ?", ("Ella",))

conn.commit()
print("Student deleted successfully.")
conn.close()
