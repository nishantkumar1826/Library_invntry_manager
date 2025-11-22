# -------------------------------------------
#  Library Inventory Manager - Lab Assingment 03
# Name :- Nishant Kumar 
# Roll no:- 2501420046
# Btech CSE Data Science
# -------------------------------------------

class Book:
    def __init__(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display(self):
        print("\n--- Book Details ---")
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN  : {self.isbn}")
        print(f"Status: {self.status}")
        print("---------------------")

    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print("✔ Book has been issued.")
        else:
            print("✖ Book is already issued.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print("✔ Book has been returned.")
        else:
            print("✖ Book was not issued.")


# File Handling

FILE_NAME = "library.txt"


def load_books():
    """Load all books from library.txt into a list of Book objects."""
    books = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                title, author, isbn, status = line.split(",")
                books.append(Book(title, author, isbn, status))
    except FileNotFoundError:
        # File will be created when we save for the first time
        pass
    return books


def save_all_books(books):
    """Save the entire books list to library.txt."""
    try:
        with open(FILE_NAME, "w") as f:
            for b in books:
                f.write(f"{b.title},{b.author},{b.isbn},{b.status}\n")
        # for libraray updation
    except Exception as e:
        print("Error while saving file:", e)


#  Main Program for Library

def main():
    books = load_books()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("✖ Invalid input! Enter numbers only.")
            continue

        #  To add New Book
        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN number: ")

            book = Book(title, author, isbn)
            books.append(book)
            save_all_books(books)
            print("✔ Book added to library.")
            book.display()

        #   To view All Books
        elif choice == 2:
            if not books:
                print("✖ No books in library. Add a book first.")
            else:
                print("\n--- All Books in Library ---")
                for b in books:
                    b.display()

        #  To issue a Book
        elif choice == 3:
            if not books:
                print("✖ No books in library to issue.")
                continue

            isbn = input("Enter ISBN of book to issue: ")
            for b in books:
                if b.isbn == isbn:
                    b.issue_book()
                    save_all_books(books)
                    break
            else:
                print("✖ Book not found with that ISBN.")

        #   To return a Book
        elif choice == 4:
            if not books:
                print("✖ No books in library to return.")
                continue

            isbn = input("Enter ISBN of book to return: ")
            for b in books:
                if b.isbn == isbn:
                    b.return_book()
                    save_all_books(books)
                    break
            else:
                print("✖ Book not found with that ISBN.")

        #  Exit the program
        elif choice == 5:
            print("Exiting program... Goodbye!")
            break

        else:
            print("✖ Invalid choice! Please choose between 1–5.")


if __name__ == "__main__":
    main()
