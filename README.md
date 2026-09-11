# Journal Management System

A simple Python-based Journal Management System developed using Object-Oriented Programming (OOP). This application allows users to add, view, search, and delete journal entries through a simple menu-driven interface.

## Features

- Add new journal entries
- PIN-based authentication
- View all journal entries
- Search entries by keyword or date
- Delete all journal entries
- Automatic date and time for each entry
- Exception handling
- User input validation
- Automatic creation of journal file
- Menu-driven interface

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- File Handling
- Exception Handling
- Datetime Module

## File Handling

The project uses `journal.txt` to store journal entries.

Different file handling modes are used:

- `x` - Creates the journal file if it does not exist
- `a` - Adds new entries to the existing file
- `r` - Reads journal entries
- `w` - Clears all entries from the file

## OOP Concepts Used

- Class
- Object
- Constructor
- Instance Methods
- Encapsulation
- Exception Handling

## Main Menu

The application provides the following options:

1. Add Entry
2. View All Entries
3. Search Entry
4. Delete All Entries
5. Exit

## PIN Authentication

A PIN is required before adding a journal entry.

Default PIN: `1234`

## Exception Handling

The application handles different types of errors, including:

- Invalid PIN
- Invalid numeric input
- File not found errors
- Permission errors
- Unexpected errors

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code or any Python IDE.
4. Run the Python file.
5. Select an option from the menu.
6. Follow the instructions displayed on the screen.

## Project Structure

Journal-Management-System/
- journal.py
- README.md

## Project Objective

The main objective of this project is to practice Python Object-Oriented Programming, file handling, exception handling, user input validation, and menu-driven programming by developing a simple real-world journal application.

## Author

NILANCHAL BEHERA

