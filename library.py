import sqlite3

import time

class Book():

    def __init__(self,name,author,publisher,number_of_pages,year,genre):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.number_of_pages = number_of_pages
        self.year = year
        self.genre = genre

    def __str__(self):
        return "Book Name: {}\nAuthor: {}\nPublisher: {}\nNumber of Pages: {}\nYear: {}\nGenre: {}".format(self.name,self.author,self.publisher,self.number_of_pages,self.year,self.genre)



class Library():

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection=sqlite3.connect("Library.db")

        self.cursor = self.connection.cursor()

        query = "Create table if not exists Books (Name TEXT,Author TEXT,Publisher TEXT,Number of Pages INT,Year INT,Genre TEXT)"

        self.cursor.execute(query)

        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def show_books(self):

        query = "Select * from Books"

        self.cursor.execute(query)

        books = self.cursor.fetchall()

        if (len(books)==0):
            print("No books in the library.")

        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4],i[5])
                print(book)
                print("\n")

    def search_book(self,name):

        query = "Select * from Books where name = ?"

        self.cursor.execute(query,(name,))

        books  = self.cursor.fetchall()

        if(len(books)==0):
            print("No such book found...")

        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4],books[0][5])

            print(book)
    def add_book(self,book):

        query = "insert into Books values(?,?,?,?,?,?)"

        self.cursor.execute(query,(book.name,book.author,book.publisher,book.number_of_pages,book.year,book.genre))

        self.connection.commit()

    def remove_book(self,name):

        query = "Delete from Books where name = ?"

        self.cursor.execute(query,(name,))

        self.connection.commit()
