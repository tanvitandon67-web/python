class Library :
    def __init__(self):
        self.book = []

    def add(self,book):
        self.book.append(book)
        print("The book is added",book)

    
    def return1(self,book):
        self.book.append(book)
        print("The book is Returned",book)

    def borrow(self,book):
        if book in self.book :
            self.book.removed(book)
            print("Borrowed".book)

        else:
            print("not avalible")

Library = Library()

Library.add("Harry potter")
    
Library.borrow("Harry Potter")

Library.return1("Harry Potter")