# Q3. Library Record System
# Stores: ISBN -> {"title": title, "author": author,
#                  "copies": available copies, "issued_to": [member IDs]}

books = {
    "B1": {"title": "Python Basics", "author": "Rao", "copies": 2, "issued_to": [], "ever_issued": False},
    "B2": {"title": "Data Structures", "author": "Iyer", "copies": 1, "issued_to": [], "ever_issued": False},
    "B3": {"title": "Algorithms", "author": "Rao", "copies": 1, "issued_to": [], "ever_issued": False}
}


def add_book():
    isbn = input("Enter ISBN/book ID: ").strip()
    if isbn in books:
        try:
            extra = int(input("Book already exists. How many copies to add? "))
            if extra <= 0:
                print("Number of copies must be positive.")
                return
            books[isbn]["copies"] += extra
            print("Copies added successfully.")
        except ValueError:
            print("Please enter a valid whole number.")
        return

    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    try:
        copies = int(input("Enter number of copies: "))
        if copies <= 0:
            print("Copies must be positive.")
            return
    except ValueError:
        print("Please enter a valid whole number.")
        return

    books[isbn] = {"title": title, "author": author,
                   "copies": copies, "issued_to": [], "ever_issued": False}
    print("Book added successfully.")


def issue_book():
    isbn = input("Enter book ID: ").strip()
    member = input("Enter member ID: ").strip()

    if isbn not in books:
        print("Book not found.")
        return
    book = books[isbn]

    if member in book["issued_to"]:
        print("This member already holds this book.")
        return
    if book["copies"] <= 0:
        print("No copies are currently available.")
        return

    # Count all books currently held by this member.
    held_count = sum(member in item["issued_to"] for item in books.values())
    if held_count >= 2:
        print("Issue rejected: a member may hold at most 2 books.")
        return

    book["copies"] -= 1
    book["issued_to"].append(member)
    book["ever_issued"] = True
    print("Book issued successfully. Available copies:", book["copies"])


def return_book():
    isbn = input("Enter book ID: ").strip()
    member = input("Enter member ID: ").strip()

    if isbn not in books:
        print("Book not found.")
        return
    book = books[isbn]
    if member not in book["issued_to"]:
        print("Return rejected: this member does not hold this book.")
        return

    book["issued_to"].remove(member)
    book["copies"] += 1
    print("Book returned successfully. Available copies:", book["copies"])


def search_book():
    isbn = input("Enter book ID: ").strip()
    if isbn in books:
        print(isbn, ":", books[isbn])
    else:
        # Also allow searching by title or author.
        term = isbn.lower()
        matches = {
            code: data for code, data in books.items()
            if term in data["title"].lower() or term in data["author"].lower()
        }
        if matches:
            for code, data in matches.items():
                print(code, ":", data)
        else:
            print("Book not found.")


def show_reports():
    author = input("Enter author name for author report: ").strip().lower()
    by_author = {
        isbn: data["title"] for isbn, data in books.items()
        if data["author"].lower() == author
    }
    print("\nBooks by", author or "(blank author)", ":", by_author)

    # Invert book -> member list into member -> list of book titles.
    member_books = {}
    for isbn, data in books.items():
        for member in data["issued_to"]:
            member_books.setdefault(member, []).append(data["title"])

    multiple_books = {
        member: titles for member, titles in member_books.items() if len(titles) > 1
    }
    print("\nMembers currently holding more than one book:", multiple_books)

    unavailable = {
        isbn: data["title"] for isbn, data in books.items() if data["copies"] == 0
    }
    print("\nBooks currently unavailable (0 copies):", unavailable)

    never_issued = {
        isbn: data["title"] for isbn, data in books.items()
        if not data["ever_issued"]
    }
    print("\nBooks that have never been issued:", never_issued)


def main():
    while True:
        print("\n===== LIBRARY RECORD SYSTEM =====")
        print("1. Add book")
        print("2. Issue book")
        print("3. Return book")
        print("4. Search book")
        print("5. Reports")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            show_reports()
        elif choice == "6":
            print("Exiting Library Record System.")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
