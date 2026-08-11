# OOP / Encapsulation / multi classes
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, book_title):
        book = library.find_book(book_title)
        if book is None:
            print(f"Book '{book_title}' not found in library.")
            return
        if book.is_borrowed:
            print(f"Book '{book_title}' is already borrowed.")
            return
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'.")
        return

    def return_book(self, library, book_title):
        for book in self.borrowed_books:
            if book.title == book_title:
                book.is_borrowed = False
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book_title}'.")
                return
        print(f"{self.name} does not have '{book_title}'.")


class Library:
    def __init__(self, name):
        self.name = name
        self.__books = []  # private list

    def add_book(self, book):
        self.__books.append(book)
        print(f"Added '{book.title}' to library.")

    def find_book(self, title):
        for book in self.__books:
            if book.title == title:
                return book
        return None

    def report(self):
        print(f"Library report for {self.name}:")
        for book in self.__books:
            print(" -", book)


if __name__ == "__main__":
    lib = Library("City Library")
    b1 = Book("Deep Learning", "Ian Goodfellow")
    b2 = Book("Clean Code", "Robert C. Martin")

    lib.add_book(b1)
    lib.add_book(b2)

    m1 = Member("Nahal")
    m2 = Member("Yadi")
    m1.borrow_book(lib, "Deep Learning")
    m2.borrow_book(lib, "Deep Learning")
    m1.borrow_book(lib, "Clean Code")

    lib.report()

    m1.return_book(lib, "Deep Learning")
    lib.report()