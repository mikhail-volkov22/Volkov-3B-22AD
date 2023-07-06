import sqlite3

conn = sqlite3.connect('movies.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies (name TEXT, genre TEXT, rating INTEGER)''')
movies = [('Криминальное чтиво', 'драма', 8.0),
         ('Герой', 'драма', 7.5),
         ('Поезд Джоу Ю', 'драма', 7.8),
         ('Стражи галактики', 'комедия', 8.1),
         ('Интерстеллар', 'фантастика', 8.0)]
cursor.executemany('INSERT INTO movies VALUES (?, ?, ?)', movies)
conn.commit()

cursor.execute('SELECT * FROM movies WHERE genre = "драма"')
selection = cursor.fetchall()

for movie in selection:
    print(f'название: {movie[0]}, жанр: {movie[1]}, рейтинг: {movie[2]}')

conn.close()