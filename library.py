import sqlite3

class Book():

    def __init__(self,name,author,publisher,number_of_pages,year,genre):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.number_of_pages = number_of_pages
        self.year = year
        self.genre = genre

    def __str__(self):
        bookDetails = f"""
        Book Name: {self.name}
        Author: {self.author}
        Publisher: {self.publisher}
        Number of Pages: {self.number_of_pages}
        Year: {self.year}
        Genre: {self.genre}
        """
        return bookDetails.rstrip()

# Querries for library database
libraryCreateQuery = "CREATE TABLE IF NOT EXISTS Books (Name TEXT,Author TEXT,Publisher TEXT,Number of Pages INT,Year INT,Genre TEXT)"

selectAllBooksQuery = "SELECT * FROM Books"

selectSpecificBookQuery = "SELECT * FROM Books WHERE Name = ?"

insertBookQuery = "INSERT INTO Books VALUES (?,?,?,?,?,?)"

deleteBookQuery = "DELETE FROM Books WHERE Name = ?"

class Library():

    def __init__(self):
        self.create_connection()


    def create_connection(self):
        self.connection=sqlite3.connect("Library.db")

        self.cursor = self.connection.cursor()

        query = libraryCreateQuery

        self.cursor.execute(query)

        self.connection.commit()


    def close_connection(self):
        self.connection.close()


    def show_books(self):

        query = selectAllBooksQuery

        self.cursor.execute(query)

        books = self.cursor.fetchall()

        if (len(books)==0):
            print("No books in the library.")

        else:
            for details in books:
                book = Book(name= details[0],author= details[1],
                            publisher= details[2],number_of_pages= details[3],
                            year= details[4],genre= details[5])
                print(str(book)+"\n")


    def search_book(self,name):

        query = selectSpecificBookQuery

        
        details  = self.cursor.execute(query,(name,)).fetchone() # fetchone() returns a tuple

        if details is None:
            print("No such book in the library.")

        else:
            
            book = Book(name= details[0],author= details[1],
                        publisher= details[2],number_of_pages= details[3],
                        year= details[4],genre= details[5])

            print(str(book)+"\n")


    def add_book(self,book):

        query = insertBookQuery

        self.cursor.execute(query,(book.name,book.author,book.publisher,book.number_of_pages,book.year,book.genre))

        self.connection.commit()


    def remove_book(self,name):

        query = deleteBookQuery

        self.cursor.execute(query,(name,))

        self.connection.commit()