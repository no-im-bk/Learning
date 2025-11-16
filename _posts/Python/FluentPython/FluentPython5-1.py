

from dataclasses import dataclass, field


@dataclass
class Book():
    name: str = ""
    author: str = ""
    number_pages: int = 0
    topics: list[str] = field(default_factory=list)


# Used AI to generate a list of 10 books
books = [
    Book(
        name="To Kill a Mockingbird",
        author="Harper Lee",
        number_pages=324,
        topics=["Fiction", "Classic", "Legal Drama", "Coming of Age"]
    ),
    Book(
        name="1984",
        author="George Orwell",
        number_pages=328,
        topics=["Dystopian", "Science Fiction", "Political Fiction"]
    ),
    Book(
        name="The Great Gatsby",
        author="F. Scott Fitzgerald",
        number_pages=180,
        topics=["Fiction", "Classic", "Romance", "American Dream"]
    ),
    Book(
        name="Pride and Prejudice",
        author="Jane Austen",
        number_pages=432,
        topics=["Romance", "Classic", "Social Commentary"]
    ),
    Book(
        name="The Catcher in the Rye",
        author="J.D. Salinger",
        topics=["Fiction", "Coming of Age", "Classic"]
    ),
    Book(
        name="Sapiens",
        number_pages=443,
        topics=["Non-fiction", "History", "Anthropology", "Science"]
    ),
    Book(
        name="The Hobbit",
        author="J.R.R. Tolkien",
        number_pages=310,
        topics=["Fantasy", "Adventure", "Classic"]
    ),
    Book(
        name="Educated",
        author="Tara Westover",
        number_pages=334,
    ),
    Book(
        name="The Alchemist",
        author="Paulo Coelho",
        number_pages=208,
        topics=["Fiction", "Philosophy", "Adventure", "Spirituality"]
    ),
    Book(
        name="Atomic Habits",
        author="James Clear",
        number_pages=320,
        topics=["Self-help", "Psychology", "Productivity", "Non-fiction"]
    )
]

for book in books:
    match book:
        case Book(topics=t, name=n) if "Classic" in t:
            print(f"{n} is a Classic.")
    