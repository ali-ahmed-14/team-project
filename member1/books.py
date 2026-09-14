import json

FILE = "books_data.json"


def load_books():
    with open(FILE, "r") as file:
        return json.load(file)


def save_books(books):
    with open(FILE, "w") as file:
        json.dump(books, file, indent=4)


def add_book():
    books = load_books()

    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author
    }

    books.append(book)
    save_books(books)

    print("Book added successfully.")


def view_books():
    books = load_books()

    if not books:
        print("No books found.")
        return

    for book in books:
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print("-" * 30)


def search_book():
    books = load_books()
    keyword = input("Enter book title to search: ").lower()

    found = False

    for book in books:
        if keyword in book["title"].lower():
            print(book)
            found = True

    if not found:
        print("Book not found.")


def delete_book():
    books = load_books()
    book_id = input("Enter book ID to delete: ")

    new_books = [book for book in books if book["id"] != book_id]

    if len(new_books) == len(books):
        print("Book not found.")
    else:
        save_books(new_books)
        print("Book deleted successfully.")
