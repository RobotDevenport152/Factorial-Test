class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title, author)

    def display_details(self):
        # Only display existing attributes
        print(f"Book - Title: {self.title}, Author: {self.author}")

class Magazine(LibraryItem):
    def __init__(self, title, author, issue_frequency):
        super().__init__(title, author)
        self.issue_frequency = issue_frequency

    def display_details(self):
        print(f"Magazine - Title: {self.title}, Author: {self.author}, "
              f"Issue Frequency: {self.issue_frequency}")

class Library:
    """
    Represents the library.
    Encapsulates the list of items and provides methods to manage them.
    """
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)
        print(f"Item '{item.title}' added to the library.")

    def remove_item(self, title):
        for item in self._items:
            if item.title == title:
                self._items.remove(item)
                print(f"Item '{title}' removed from the library.")
                return
        print(f"Item '{title}' not found in the library.")

    def display_all_items(self):
        print("\nLibrary Catalog:")
        for item in self._items:
            item.display_details()
        print()

# Example usage
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
mag1 = Magazine("National Geographic", "Various", "Monthly")
mag2 = Magazine("Time", "Various", "Weekly")

my_library = Library()
my_library.add_item(book1)
my_library.add_item(book2)
my_library.add_item(mag1)
my_library.add_item(mag2)

my_library.display_all_items()
my_library.remove_item("Time")
my_library.display_all_items()
