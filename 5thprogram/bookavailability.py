class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book Issued")
        else:
            print("Not Available")

    def status(self):
        print("Available:", self.available)

b = Book("Java")
b.status()
b.issue()
b.status()