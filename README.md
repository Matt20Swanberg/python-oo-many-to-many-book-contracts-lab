# Many-to-Many Book Contracts

## Description

This project demonstrates a many-to-many object relationship in Python.

The application models the relationship between authors and books using contracts. An author can be associated with many books, and a book can be associated with many authors. The `Contract` class acts as the intermediary that connects an `Author` to a `Book`.

## Relationship Structure

The application uses three classes:

- `Author`
- `Book`
- `Contract`

The relationship can be represented as:

```text
Author -> Contract <- Book
```

An `Author` can have many `Contract` objects, and a `Book` can also have many `Contract` objects. Each individual `Contract` connects one author with one book.

## Models

### Author

The `Author` class represents an author in the application.

Each author has:

- A `name`
- A collection of related contracts
- A collection of books accessed through contracts

Available methods include:

- `contracts()` - Returns all contracts associated with the author.
- `books()` - Returns all books associated with the author through contracts.
- `sign_contract(book, date, royalties)` - Creates a new contract between the author and a book.
- `total_royalties()` - Calculates the author's total royalties across all contracts.

### Book

The `Book` class represents a book in the application.

Each book has:

- A `title`
- A collection of related contracts
- A collection of authors accessed through contracts

Available methods include:

- `contracts()` - Returns all contracts associated with the book.
- `authors()` - Returns all authors associated with the book through contracts.

### Contract

The `Contract` class acts as the intermediary between an `Author` and a `Book`.

Each contract contains:

- `author`
- `book`
- `date`
- `royalties`

The Contract properties use validation to ensure:

- `author` is an instance of `Author`
- `book` is an instance of `Book`
- `date` is a string
- `royalties` is an integer

The class also provides:

- `contracts_by_date(date)` - Returns all contracts matching a specified date.

## Example

```python
author = Author("Alice")
book = Book("Example Book")

contract = author.sign_contract(
    book,
    "2026-08-11",
    500
)

author.books()
book.authors()
author.total_royalties()
```

In this example, the `Contract` connects the author and book. The relationship can then be accessed from either direction.

## Installation

1. Fork the repository to your GitHub account and clone your fork:

```bash
git clone <your-repository-url>
```

2. Navigate into the project directory:

```bash
cd python-oo-many-to-many-book-contracts-lab
```

3. Install project dependencies.

```bash
pipenv install
```

4. Activate the virtual environment.

```bash
pipenv shell
```

5. Run the test suite with:

```bash
pytest
```

## Testing

The project's tests verify the behavior of the `Author`, `Book`, and `Contract` models, including their many-to-many relationships and property validation.

## Screenshot

The screenshot below shows the completed project and successful test results.

![Test Suite Passed](/screenshots/screenshot.png)

## Technologies

- Python
- Pytest
- Object-Oriented Programming
- Many-to-Many Relationships

## Author

Created by Matthew Swanberg as part of  Course 7 Module 5 (Many-to-Many Relationships - Book Contracts)