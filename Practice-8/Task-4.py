import sqlite3

conn = sqlite3.connect('employees.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (name TEXT, function TEXT, salary INTEGER)''')
employees = [('Васильев', 'менеджер', 60000),
         ('Иванов', 'продавец', 50000),
         ('Андреев', 'бухгалтер', 45000),
         ('Сергеев', 'менеджер', 75000),
         ('Пашин', 'консультант', 48000)]
cursor.executemany('INSERT INTO employees VALUES (?, ?, ?)', employees)
conn.commit()

cursor.execute('SELECT * FROM employees WHERE function = "менеджер"')
selection = cursor.fetchall()

for employee in selection:
    print(f'имя: {employee[0]}, должность: {employee[1]}, зарплата: {employee[2]}')

conn.close()