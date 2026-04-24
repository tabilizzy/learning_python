from datetime import datetime, timedelta


# ========================
# Book Class
# ========================
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._is_available = True  # private-like

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, value):
        if not isinstance(value, bool):
            raise ValueError("Availability must be True or False")
        self._is_available = value

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {status}"

    def __eq__(self, other):
        return isinstance(other, Book) and self.isbn == other.isbn


# ========================
# Member Class
# ========================
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # list of dicts {book, due_date}

    def borrow_book(self, book):
        if not book.is_available:
            raise ValueError("Book is not available")

        due_date = datetime.now() + timedelta(days=7)

        self.borrowed_books.append({
            "book": book,
            "due_date": due_date
        })

        book.is_available = False

    def return_book(self, book):
        for record in self.borrowed_books:
            if record["book"] == book:
                self.borrowed_books.remove(record)
                book.is_available = True
                return

        raise ValueError("This member did not borrow this book")

    def __str__(self):
        return f"{self.member_id} - {self.name}"


# ========================
# Library Class (Composition)
# ========================
class Library:
    def __init__(self):
        self.books = {}      # isbn -> Book
        self.members = {}    # member_id -> Member

    def add_book(self, book):
        if book.isbn in self.books:
            raise ValueError("Book already exists")
        self.books[book.isbn] = book

    def register_member(self, member):
        if member.member_id in self.members:
            raise ValueError("Member already exists")
        self.members[member.member_id] = member

    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if isbn not in self.books:
            raise ValueError("Book not found")

        member = self.members[member_id]
        book = self.books[isbn]

        member.borrow_book(book)

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if isbn not in self.books:
            raise ValueError("Book not found")

        member = self.members[member_id]
        book = self.books[isbn]

        member.return_book(book)

    def show_available_books(self):
        print("\n--- Available Books ---")
        for book in self.books.values():
            if book.is_available:
                print(book)

    def show_member_books(self, member_id):
        if member_id not in self.members:
            raise ValueError("Member not found")

        member = self.members[member_id]

        print(f"\n--- {member.name}'s Books ---")
        for record in member.borrowed_books:
            book = record["book"]
            due = record["due_date"]
            print(f"{book.title} | Due: {due.strftime('%Y-%m-%d')}")

    def show_overdue_books(self):
        print("\n--- Overdue Books ---")
        now = datetime.now()
        found = False

        for member in self.members.values():
            for record in member.borrowed_books:
                if record["due_date"] < now:
                    print(f"{record['book'].title} (Borrowed by {member.name})")
                    found = True

        if not found:
            print("No overdue books.")


# ========================
# Main Program
# ========================
library = Library()

while True:
    print("\n=== Library Menu ===")
    print("1. Add book")
    print("2. Register member")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Show available books")
    print("6. Show member's borrowed books")
    print("7. Show overdue books")
    print("8. Exit")

    try:
        choice = input("Choose an option: ")

        match choice:
            case "1":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")

                library.add_book(Book(title, author, isbn))
                print("Book added!")

            case "2":
                member_id = input("Member ID: ")
                name = input("Name: ")

                library.register_member(Member(member_id, name))
                print("Member registered!")

            case "3":
                member_id = input("Member ID: ")
                isbn = input("ISBN: ")

                library.borrow_book(member_id, isbn)
                print("Book borrowed!")

            case "4":
                member_id = input("Member ID: ")
                isbn = input("ISBN: ")

                library.return_book(member_id, isbn)
                print("Book returned!")

            case "5":
                library.show_available_books()

            case "6":
                member_id = input("Member ID: ")
                library.show_member_books(member_id)

            case "7":
                library.show_overdue_books()

            case "8":
                print("Goodbye!")
                break

            case _:
                print("Invalid option!")

    except ValueError as e:
        print("Error:", e)