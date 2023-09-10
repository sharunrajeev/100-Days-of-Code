import sqlite3

db = sqlite3.connect('book-collection.db')

cursor = db.cursor()

cursor.execute('CREATE TABLE Books (id INTEGER PRIMARY KEY, title VARCHAR(100) NOT NULL UNIQUE, author VARCHAR(100) NOT NULL, rating FLOAT NOT NULL)')

cursor.execute('INSERT INTO Books VALUES (1, "Harry Potter", "J.K Rowling", "9.3")')

db.commit()
