class Library:
    def __init__(self):
        self.books = ["Python", "Java", "C++"]

    def show_books(self):
        print("Available Books:")
        for b in self.books:
            print(b)

    def issue_book(self, name):
        if name in self.books:
            self.books.remove(name)
            print(name, "issued.")
        else:
            print("Book not available.")

lib = Library()
lib.show_books()
lib.issue_book("Python")
lib.show_books()