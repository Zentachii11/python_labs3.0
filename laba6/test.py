import sqlite3

conn = sqlite3.connect(r"C:\Users\kalin\Desktop\sql.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM Пользователи")
users = cursor.fetchall()

print("Пользователи:")

for user in users:
    print(user)

conn.close()