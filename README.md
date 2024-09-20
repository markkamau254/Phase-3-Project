# Book Manager with SQLite
This is a simple command-line application for managing a list of books using SQLite as a database. The application allows users to perform the following operations:

- Add a new book
- Look up a book by title
- Display all books
- Update book details
- Delete a book

The books are stored in a SQLite database `(theBookList.db)`, making it easier to store and manage book records compared to using text files.

## Features
1. **Add a Book**: Add a book with its title, author, and number of pages.
2. **Look Up a Book**: Search for a book by title (case-insensitive).
3. **Display All Books**: Display the entire list of books stored in the database.
4. **Update a Book**: Update a book's title, author, or number of pages based on its unique ID.
5. **Delete a Book**: Remove a book from the database by its ID.

## Installation
**Clone the repository:**
bash
Copy code
`git clone https://github.com/your-username/book-manager-sqlite.git
cd book-manager-sqlite`

2. **Install Python (if not already installed):**
    - Download and install Python from [python.org].
    - This project is compatible with Python 3.x.

3. **Run the project:**
    - Open a terminal or command prompt.
    - Navigate to the project directory.
    - Run the Python file:
bash
Copy code
`python book_manager.py`

## Usage
After running the program, you'll see a menu with the following options:

css
Copy code
` **** Book Manager ****`
`1) Add a book
2) Lookup a book
3) Display books
4) Update a book
5) Delete a book
6) Exit`
Choose an option by entering its number and follow the on-screen instructions.

## Example
- To add a book, choose option `1` and provide the book's title, author, and number of pages.
- To look up a book, choose option `2` and enter a keyword from the book's title.
- To update a book, choose option `4`, then provide the book's ID and the field you'd like to update.
- To delete a book, choose option `5` and provide the ID of the book to be deleted.

## Dependencies
- Python 3.x
- SQLite3 (included with Python by default)

## Database
The database file `theBookList.db` will be automatically created when you run the program. It contains a `books` table with the following fields:

- `id` (INTEGER, Primary Key)
- `title` (TEXT)
- `author` (TEXT)
- `pages` (INTEGER)

## Author
   **Mark Kamau**
