class LibrarySystem:
    def __init__(self):
        self.book_id_counter = 1
        self.books = []

    def add_book(self, title, author):
        book = {
            "id": self.book_id_counter,
            "title": title,
            "author": author,
            "status": "available"
        }
        self.books.append(book)
        self.book_id_counter += 1

    def checkout_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id and book["status"] == "available":
                book["status"] = "checked out"
                return True
        return False

    def return_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id and book["status"] == "checked out":
                book["status"] = "available"
                return True
        return False

    def display_books(self):
        for book in self.books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")

def main():
    library_system = LibrarySystem()

    while True:
        print("1. Add Book")
        print("2. Checkout Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library_system.add_book(title, author)
            print("Book added successfully!")

        elif choice == "2":
            book_id = int(input("Enter book ID to checkout: "))
            if library_system.checkout_book(book_id):
                print("Book checked out successfully!")
            else:
                print("Book not available or ID not found.")

        elif choice == "3":
            book_id = int(input("Enter book ID to return: "))
            if library_system.return_book(book_id):
                print("Book returned successfully!")
            else:
                print("Book not checked out or ID not found.")

        elif choice == "4":
            library_system.display_books()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()