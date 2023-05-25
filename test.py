import time

from library import *

menu_prompt ="""**************************

Welcome to the Library Program!

Operations:

1.Show Books

2.Search Book

3.Add Book

4.Remove Book

Press 'q' to quit.

**************************"""

library = Library()


while True:
    print(menu_prompt)
    operation = input("Enter your operation: ")

    if (operation == "q"):
        print("Exiting the program...")
        library.close_connection()
        break


    elif (operation == "1"):
        print("\n")
        library.show_books()
        input("Press any key to continue..")


    elif (operation == "2"):
        name = input("Which book are you looking for ?: ")
        print("Searching for the book..")
        time.sleep(1.5)

        library.search_book(name)
        input("Press any key to continue..")


    elif (operation == "3"):
        name = input("Name: ")
        author = input("Author: ")
        publisher = input("Publisher: ")

        # to prevent ValueError
        while True:
            try:
                number_of_pages = int(input("Number of Pages: "))
                year = int(input("Year: "))
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            else:
                break

        genre = input("Genre: ")

        new_book = Book(name,author,publisher,number_of_pages,year,genre)

        print("Adding the book..")
        time.sleep(1.5)

        library.add_book(new_book)
        print("Book added.")


    elif (operation == "4"):
        name = input("Which book do you want to remove ?: ")
        
        answer = input("Are you sure ? (Y/N): ")
        if(answer=="Y"):
            print("Removing the book...")
            time.sleep(2)
            library.remove_book(name)
            print("Book removed.")


    else:
        print("Invalid Operation!\n")
    
