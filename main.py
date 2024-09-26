import sqlite3

class BookManager:
    def __init__(self, db_name='theBookList.db'):
        """Initializes the SQLite database and creates the books table if it doesn't exist."""
        self.db_name = db_name
        self.initialize_db()

    def initialize_db(self):
        """Creates the books table if it doesn't exist."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT,
                           author TEXT,
                           pages INTEGER)''')
        conn.commit()
        conn.close()

    def add_book(self, nBook, nAuthor, nPages):
        """Adds a new book to the database."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, pages) VALUES (?, ?, ?)", (nBook, nAuthor, nPages))
        conn.commit()
        conn.close()

    def lookup_book(self, keyword):
        """Looks up a book by title."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + keyword + '%',))
        result = cursor.fetchall()
        conn.close()
        return result

    def update_book(self, book_id, field, new_value):
        """Updates a book in the database based on its ID."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = f"UPDATE books SET {field} = ? WHERE id = ?"
        cursor.execute(query, (new_value, book_id))
        conn.commit()
        conn.close()

    def delete_book(self, book_id):
        """Deletes a book from the database by ID."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()

    def display_books(self):
        """Displays all books in the database."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books


class BookApp:
    def __init__(self):
        self.manager = BookManager()

    def main_menu(self):
        """Main menu loop."""
        choice = 0
        while choice != 6:
            print("**** Book Manager ****")
            print("1) Add a book")
            print("2) Lookup a book")
            print("3) Display books")
            print("4) Update a book")
            print("5) Delete a book")
            print("6) Exit")
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.lookup_book()
            elif choice == 3:
                self.display_books()
            elif choice == 4:
                self.update_book()
            elif choice == 5:
                self.delete_book()
            elif choice == 6:
                print("Exiting program...")

        print("Program Terminated!")

    def add_book(self):
        """Prompts user to add a book."""
        print("Adding a book...")
        nBook = input("Enter book name: ")
        nAuthor = input("Enter author name: ")
        nPages = input("Enter number of pages: ")

        if not nPages.isdigit():
            print("Invalid input for number of pages. Please enter a valid number.")
        else:
            self.manager.add_book(nBook, nAuthor, nPages)

    def lookup_book(self):
        """Prompts user to lookup a book."""
        print("Looking up a book...")
        keyword = input("Enter book name to search >>>")
        result = self.manager.lookup_book(keyword)
        if result:
            for book in result:
                print(f"ID: {book[0]}, Book: {book[1]}, Author: {book[2]}, Pages: {book[3]}")
        else:
            print("Book not found!")

    def display_books(self):
        """Displays all books."""
        print("Displaying all books...")
        books = self.manager.display_books()
        if not books:
            print("No books in the list.")
        else:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Pages: {book[3]}")

    def update_book(self):
        """Prompts user to update a book."""
        print("Updating a book...")
        book_id = int(input("Enter the ID of the book to update >>>"))
        field_to_update = int(input("Enter the number of the field you want to update (1=Title, 2=Author, 3=Pages): "))

        if field_to_update == 1:
            new_title = input("Enter new title: ")
            self.manager.update_book(book_id, "title", new_title)
        elif field_to_update == 2:
            new_author = input("Enter new author: ")
            self.manager.update_book(book_id, "author", new_author)
        elif field_to_update == 3:
            new_pages = input("Enter new number of pages: ")
            if new_pages.isdigit():
                self.manager.update_book(book_id, "pages", new_pages)
            else:
                print("Invalid input for number of pages. Please enter a valid number.")
        else:
            print("Invalid option.")

    def delete_book(self):
        """Prompts user to delete a book."""
        print("Deleting a book...")
        book_id = int(input("Enter the ID of the book to delete >>>"))
        self.manager.delete_book(book_id)
        print("Book deleted successfully!")


if __name__ == "__main__":
    app = BookApp()
    app.main_menu()

