import sqlite3

def initialize_db():
    """Initializes the SQLite database and creates the books table if it doesn't exist."""
    conn = sqlite3.connect('theBookList.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT,
                       author TEXT,
                       pages INTEGER)''')
    conn.commit()
    conn.close()

def add_book(nBook, nAuthor, nPages):
    """Adds a new book to the database."""
    conn = sqlite3.connect('theBookList.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, pages) VALUES (?, ?, ?)", (nBook, nAuthor, nPages))
    conn.commit()
    conn.close()

def lookup_book(keyword):
    """Looks up a book by title."""
    conn = sqlite3.connect('theBookList.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + keyword + '%',))
    result = cursor.fetchall()
    conn.close()
    return result

def update_book(book_id, field, new_value):
    """Updates a book in the database based on its ID."""
    conn = sqlite3.connect('theBookList.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE books SET {field} = ? WHERE id = ?", (new_value, book_id))
    conn.commit()
    conn.close()

def delete_book(book_id):
    """Deletes a book from the database by ID."""
    conn = sqlite3.connect('theBookList.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

def display_books():
    """Displays all books in the database."""
    conn = sqlite3.connect('theBookList.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

def main():
    initialize_db()

    choice = 0
    while choice != 6:  # Update the exit condition to 6 since we're adding a new option
        print("**** Book Manager ****")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Update a book")
        print("5) Delete a book")
        print("6) Exit")
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter book name: ")
            nAuthor = input("Enter author name: ")
            nPages = input("Enter number of pages: ")
            
            if not nPages.isdigit():
                print("Invalid input for number of pages. Please enter a valid number.")
            else:
                add_book(nBook, nAuthor, nPages)

        elif choice == 2:
            print("Looking up a book...")
            keyword = input("Enter book name to search >>>")
            result = lookup_book(keyword)
            if result:
                for book in result:
                    print(f"ID: {book[0]}, Book: {book[1]}, Author: {book[2]}, Pages: {book[3]}")
            else:
                print("Book not found!")

        elif choice == 3:
            print("Displaying all books...")
            books = display_books()
            if not books:
                print("No books in the list.")
            else:
                for book in books:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Pages: {book[3]}")

        elif choice == 4:
            print("Updating a book...")
            book_id = int(input("Enter the ID of the book to update >>>"))
            field_to_update = int(input("Enter the number of the field you want to update (1=Title, 2=Author, 3=Pages): "))
            
            if field_to_update == 1:
                new_title = input("Enter new title: ")
                update_book(book_id, "title", new_title)
            elif field_to_update == 2:
                new_author = input("Enter new author: ")
                update_book(book_id, "author", new_author)
            elif field_to_update == 3:
                new_pages = input("Enter new number of pages: ")
                if new_pages.isdigit():
                    update_book(book_id, "pages", new_pages)
                else:
                    print("Invalid input for number of pages. Please enter a valid number.")
            else:
                print("Invalid option.")

        elif choice == 5:
            print("Deleting a book...")
            book_id = int(input("Enter the ID of the book to delete >>>"))
            delete_book(book_id)
            print("Book deleted successfully!")

        elif choice == 6:
            print("Exiting program...")

    print("Program Terminated!")


if __name__ == "__main__":
    main()
