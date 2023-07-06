import sqlite3

conn = sqlite3.connect('base.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, avg_score REAL)''')
students = [('Иванов', 18, 4.1), ('Антонов', 20, 3.5), ('Васильев', 19, 4.4), ('Ильин', 41, 4.9), ('Петров', 22, 3.8)]
cursor.executemany('INSERT INTO students VALUES (?, ?, ?)', students)
conn.commit()

cursor.execute('SELECT * FROM students')
all_students = cursor.fetchall()

for student in all_students:
    print(f'имя: {student[0]}, возраст: {student[1]}, средняя оценка: {student[2]}')

conn.close()