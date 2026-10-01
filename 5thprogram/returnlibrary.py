class Book:
    def __init__(self, title):
        self.title = title
        self.issued = False

    def issue_book(self):
        if not self.issued:
            self.issued = True
            print(self.title, "issued successfully.")
        else:
            print("Book already issued.")

    def return_book(self):
        if self.issued:
            self.issued = False
            print(self.title, "returned successfully.")
        else:
            print("Book was not issued.")

book = Book("Python Programming")

book.issue_book()
book.return_book()