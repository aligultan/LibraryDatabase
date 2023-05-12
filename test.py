import time

from library import *

print("""**************************

Welcome to the Library Program!

Operations:

1.Show Books

2.Search Book

3.Add Book

4.Remove Book

Press 'q' to quit.

**************************""")

library = Library()


while True:
    operation = input("Enter your operation:")

    if (operation == "q"):
        print("Exiting the program...")
        library.close_connection()
        break

        break
    elif (operation == "1"):
        print("\n")
        library.show_books()



    elif (operation == "2"):
        name = input("Which book are you looking for ?:")
        print("Searching for the book..")
        time.sleep(2)

        library.search_book(name)

    elif (operation == "3"):
        name = input("Name:")
        author = input("Author:")
        publisher = input("Publisher:")
        number_of_pages = int(input("Number of Pages:"))
        year = int(input("Year:"))
        genre = input("Genre:")

        new_book = Book(name,author,publisher,number_of_pages,year,genre)

        print("Adding the book..")
        time.sleep(2)

        library.add_book(new_book)
        print("Book added.")



    elif (operation == "4"):
        name = input("Which book do you want to remove ?:")
        answer = input("Are you sure ? (Y/N):")

        if(answer=="Y"):
            print("Removing the book...")
            time.sleep(2)
            library.remove_book(name)
            print("Book removed.")


    else:
        print("Invalid Operation!")
