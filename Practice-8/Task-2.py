import sqlite3

conn = sqlite3.connect('books.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT, year INTEGER)''')
books = [('Онегин', 'Пушкин', 1960),
         ('Герой', 'Лермонтов', 1981),
         ('Собрание', 'Блок', 2001),
         ('На дне', 'Горький', 2010),
         ('Гроза', 'Островский', 2015)]
cursor.executemany('INSERT INTO books VALUES (?, ?, ?)', books)
conn.commit()

cursor.execute('SELECT * FROM books WHERE year > 2000')
selection = cursor.fetchall()

for book in selection:
    print(f'название: {book[0]}, автор: {book[1]}, год издания: {book[2]}')

conn.close()