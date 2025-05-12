class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        return False

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            return True
        return False

    def display_info(self):
        status = "Checked Out" if self.checked_out else "Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {status}")
        print("-" * 30)


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.checked_out_books = []

    def check_out_book(self, book):
        if book not in self.checked_out_books:
            self.checked_out_books.append(book)
            return True
        return False

    def check_in_book(self, book):
        if book in self.checked_out_books:
            self.checked_out_books.remove(book)
            return True
        return False

    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer ID: {self.customer_id}")
        print("Checked Out Books:")
        if not self.checked_out_books:
            print("  None")
        else:
            for book in self.checked_out_books:
                print(f"  - {book.title} (ISBN: {book.isbn})")
        print("=" * 30)


class Library:
    def __init__(self):
        self.books = []
        self.customers = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            return True
        return False

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)
            return True
        return False

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def check_out_book(self, customer_id, isbn):
        customer = self.find_customer(customer_id)
        book = self.find_book(isbn)

        if not customer:
            print(f"Error: Customer with ID {customer_id} not found.")
            return False

        if not book:
            print(f"Error: Book with ISBN {isbn} not found.")
            return False

        if book.checked_out:
            print(f"Error: Book '{book.title}' is already checked out.")
            return False

        if book.check_out():
            customer.check_out_book(book)
            print(f"Book '{book.title}' checked out to {customer.name}.")
            return True

        return False

    def check_in_book(self, customer_id, isbn):
        customer = self.find_customer(customer_id)
        book = self.find_book(isbn)

        if not customer:
            print(f"Error: Customer with ID {customer_id} not found.")
            return False

        if not book:
            print(f"Error: Book with ISBN {isbn} not found.")
            return False

        if not book.checked_out:
            print(f"Error: Book '{book.title}' is not checked out.")
            return False

        if book not in customer.checked_out_books:
            print(f"Error: Book '{book.title}' was not checked out by {customer.name}.")
            return False

        if book.check_in():
            customer.check_in_book(book)
            print(f"Book '{book.title}' checked in from {customer.name}.")
            return True

        return False

    def display_books(self):
        print("\nLibrary Book Collection:")
        if not self.books:
            print("  No books in collection.")
        else:
            for book in self.books:
                book.display_info()

    def display_customers(self):
        print("\nLibrary Customers:")
        if not self.customers:
            print("  No customers registered.")
        else:
            for customer in self.customers:
                customer.display_info()


# Test the system
if __name__ == "__main__":
    # Create books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("1984", "George Orwell", "9780451524935")

    # Create customers
    customer1 = Customer("Alice Smith", "C001")
    customer2 = Customer("Bob Johnson", "C002")

    # Create library
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_customer(customer1)
    library.add_customer(customer2)

    # Perform check-outs
    library.check_out_book("C001", "9780743273565")  # Alice checks out The Great Gatsby
    library.check_out_book("C001", "9780451524935")  # Alice checks out 1984
    library.check_out_book("C002", "9780743273565")  # Bob tries to check out an already checked-out book

    # Display info
    library.display_books()
    library.display_customers()

    # Perform check-ins
    library.check_in_book("C001", "9780743273565")  # Alice returns The Great Gatsby
    library.check_in_book("C002", "9780743273565")  # Bob tries to return a book he didn't check out

    # Display updated info
    library.display_books()