# Hongyi-Duan-SQL-Database

[![Python CI](https://github.com/nogibjj/Hongyi-Duan-SQL-Database/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Hongyi-Duan-SQL-Database/actions/workflows/hello.yml)

Here's a detailed `README.md` file that you can copy and use for your GitHub project based on your `main.py` and `test_main.py` files, which perform CRUD operations on a SQLite database.

### README.md

```markdown
# SQL Database CRUD Operations using Python

This project demonstrates how to interact with a SQLite database using Python. The operations include creating a table, inserting data, reading the data, updating records, and deleting records. It also includes unit tests to ensure that the CRUD operations are working as expected.

## Project Structure

- `main.py`: This file contains the core functionality for interacting with the SQLite database. It performs Create, Read, Update, and Delete (CRUD) operations on a `users` table.
- `test_main.py`: This file contains unit tests using Python's `unittest` framework to test the CRUD operations defined in `main.py`.
- `requirements.txt`: A list of required packages to run and test the project.

## How to Run the Project

### 1. Install Dependencies

Before running the project, ensure you have Python 3.x installed. You'll also need `pylint` for linting purposes. To install the dependencies, use the following command:

```bash
pip install -r requirements.txt
```

### 2. Running the Main Script

The `main.py` script performs the following actions:
1. Connects to the SQLite database (creating it if it doesn't exist).
2. Creates a `users` table (if not already created).
3. Inserts two users into the table.
4. Updates the age of one user.
5. Deletes one user.
6. Prints the state of the table after each operation.

To run the script, use the following command:

```bash
python main.py
```

### 3. Running the Tests

The `test_main.py` file contains unit tests to verify that the CRUD operations work as expected. The tests are run using Python's built-in `unittest` module. The tests include:
- Inserting a user and verifying the insertion.
- Updating a user's age and verifying the update.
- Deleting a user and verifying the deletion.

To run the tests, use the following command:

```bash
python -m unittest test_main.py
```

### Example Output

When you run `main.py`, you should see an output similar to the following:

```bash
Users after insertion:
(1, 'Alice', 30)
(2, 'Bob', 24)

Users after update:
(1, 'Alice', 31)
(2, 'Bob', 24)

Users after deletion:
(1, 'Alice', 31)
```

### 4. Linting the Code

To ensure code quality, you can use `pylint` to lint both `main.py` and `test_main.py`. Run the following command to check for any coding issues:

```bash
pylint main.py test_main.py
```

## Folder Structure

```bash
├── main.py             # Contains the core CRUD operations
├── test_main.py        # Unit tests for CRUD operations
├── requirements.txt    # Dependencies for the project
└── README.md           # Project documentation
```

## Project Requirements

- **Python**: Version 3.8 or higher.
- **SQLite**: This project uses SQLite, which is included with Python by default.

### Dependencies

The following dependency is listed in `requirements.txt`:
- `pylint`: For linting purposes.

