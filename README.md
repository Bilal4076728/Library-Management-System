# Library Management System (Python)

A command-line application to manage a library's book inventory — built in Python to practice inheritance and type-aware data handling.

## Features
- Add books as either eBooks or Physical Books (using inheritance)
- Issue and return books, tracking availability status
- View all books in the library
- Persistent data storage using JSON, correctly restoring each book's original type on load
- Menu-driven interface for easy navigation

## Concepts Used
- Object-Oriented Programming with Inheritance (`Book` base class, `EBook` and `PhysicalBook` subclasses)
- `isinstance()`-based type checking for saving/loading mixed object types from JSON
- File Handling (reading/writing JSON)
- Exception Handling (input validation)

## How to Run
```bash
python library_management.py
```

## Tech Stack
- Python 3
- JSON (for data persistence)
