import sqlite3
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str = "available"


@dataclass
class Reader:
    id: int
    name: str
    age: int


class Library:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                author TEXT,
                                year INTEGER,
                                status TEXT CHECK(status IN ('available', 'borrowed'))
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS readers (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                age INTEGER
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS borrowed_books (
                                reader_id INTEGER,
                                book_id INTEGER,
                                borrow_date TEXT,
                                FOREIGN KEY(reader_id) REFERENCES readers(id),
                                FOREIGN KEY(book_id) REFERENCES books(id)
                            )''')
        self.conn.commit()

    def add_book(self, title, author, year):
        self.cursor.execute("INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, 'available')",
                            (title, author, year))
        self.conn.commit()

    def add_reader(self, name, age):
        self.cursor.execute("INSERT INTO readers (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    def borrow_book(self, reader_id, book_id):
        self.cursor.execute("SELECT status FROM books WHERE id = ?", (book_id,))
        book = self.cursor.fetchone()
        if book and book[0] == "available":
            self.cursor.execute("UPDATE books SET status = 'borrowed' WHERE id = ?", (book_id,))
            self.cursor.execute("INSERT INTO borrowed_books (reader_id, book_id, borrow_date) VALUES (?, ?, ?)",
                                (reader_id, book_id, datetime.now().strftime('%Y-%m-%d')))
            self.conn.commit()
        else:
            print("Книга недоступна")

    def return_book(self, book_id):
        self.cursor.execute("UPDATE books SET status = 'available' WHERE id = ?", (book_id,))
        self.cursor.execute("DELETE FROM borrowed_books WHERE book_id = ?", (book_id,))
        self.conn.commit()

    def search_books(self, keyword):
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
        return self.cursor.fetchall()

    def get_borrowed_books(self):
        self.cursor.execute("SELECT * FROM borrowed_books")
        return self.cursor.fetchall()

    def get_statistics(self):
        self.cursor.execute("SELECT COUNT(*) FROM books WHERE status = 'available'")
        available = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT COUNT(*) FROM books WHERE status = 'borrowed'")
        borrowed = self.cursor.fetchone()[0]
        return {"available": available, "borrowed": borrowed}


# Демонстрация работы библиотеки
lib = Library()
lib.add_book("1984", "Джордж Оруэлл", 1949)
lib.add_book("Преступление и наказание", "Ф.М. Достоевский", 1866)
lib.add_reader("Иван Иванов", 25)
lib.borrow_book(1, 1)
print("Выданные книги:", lib.get_borrowed_books())
lib.return_book(1)
print("Статистика книг:", lib.get_statistics())
