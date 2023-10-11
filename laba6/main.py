import sqlite3

def insert_data_into_table(table_name, data_list):
    conn = sqlite3.connect(r"C:\Users\kalin\Desktop\sql.db")

    cursor = conn.cursor()

    for data in data_list:
        cursor.execute(f"INSERT INTO {table_name} (Имя, Фамилия, Место_жительства) VALUES ('{data[0]}', '{data[1]}', '{data[2]}')")

    conn.commit()

    conn.close()

table_name = 'Пользователи'
data_list = [["имя1", "фамилия1", "место1"], ["имя2", "фамилия2", "место2"], ["имя3", "фамилия3", "место3"]]
insert_data_into_table(table_name, data_list)