from datetime import datetime
from zoneinfo import ZoneInfo

class Book:

    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age(self):
        current_year = datetime.now(ZoneInfo("Asia/Tokyo")).year

        #Ensure the publication year is not in the future
        if self.publication_year > current_year:
            raise ValueError("Publication year cannot be in the future.")
        
        return current_year - self.publication_year


if __name__ == "__main__":
    book1 = Book("Python Basics", "John Doe", 2015)
    print(f"Book age is:{book1.get_age()} years")


    book2 = Book("Java Basics", "Herbert Shield", 2026)
    print(f"Book age is:{book2.get_age()} years")