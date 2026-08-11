class Author:
    """Represents an author who can be connected to many books through contracts"""

    all = []

    """Create an Author with a name and track the instance."""
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return all contracts associated with this author"""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return all books connected to this author through contracts"""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new contract between this author and a book"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the total royalties earned from all of this author's contracts"""
        return sum([contract.royalties for contract in self.contracts()])

class Book:
    """Represents a book that can have many authors through contracts"""

    all = []

    def __init__(self, title):
        """Create a Book with a title and track the instance"""
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return all contracts associated with this book"""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return all authors connected to this book through contracts"""
        return [contract.author for contract in self.contracts()]

class Contract:
    """Represents the relationship between an Author and a Book
    A contract stores the author, book, contract date, and royalty amount"""

    all = []

    def __init__(self, author, book, date, royalties):
        """Create a Contract and track the instance"""
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

        # Validate that the contract is associated with an Author instance
        if not isinstance(author, Author):
            raise Exception("input is not an instance of Author")

        # Validate that the contract is associated with a Book instance
        if not isinstance(book, Book):
            raise Exception("input is not an instance of Book")
        
        # Contract dates must be stored as a string
        if not isinstance(date, str):
            raise Exception("input is not an instance of String")

        # Royalty values must be stored as an integer
        if not isinstance(royalties, int):
            raise Exception("input is not an instance of Integer")

    @property
    def author(self):
        """Return the author associated with this contract"""
        return self._author

    @author.setter
    def author(self, author):
        """Validate and assign the contract's author"""
        if not isinstance(author, Author):
            raise Exception(...)
        self._author = author

    @property
    def book(self):
        """Return the book associated with this contract"""
        return self._book

    @book.setter
    def book(self, book):
        """Validate and assign the contract's book"""
        if not isinstance(book, Book):
            raise Exception(...)
        self._book = book

    @property
    def date(self):
        """Return the date associated with this contract"""
        return self._date

    @date.setter
    def date(self, date):
        """Validate and assign the contract date"""
        if not isinstance(date, str):
            raise Exception(...)
        self._date = date

    @property
    def royalties(self):
        """Return the royalty amount associated with this contract"""
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        """Validate and assign the contract royalty amount"""
        if not isinstance(royalties, int):
            raise Exception(...)
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that match the specified date"""
        return [contract for contract in cls.all if contract.date == date]