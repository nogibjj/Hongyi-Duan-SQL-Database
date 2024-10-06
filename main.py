"""This module performs CRUD operations on a SQLite database."""

import sqlite3

def connect_to_db(db_name="test.db"):
    """ Connect to SQLite database or create a new one """
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    """ Create a sample table in the database """
    query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    );
    '''
    conn.execute(query)
    conn.commit()

def insert_user(conn, name, age):
    """ Insert a new user into the users table """
    query = "INSERT INTO users (name, age) VALUES (?, ?);"
    conn.execute(query, (name, age))
    conn.commit()

def get_users(conn):
    """ Retrieve all users from the users table """
    query = "SELECT * FROM users;"
    cursor = conn.execute(query)
    return cursor.fetchall()

def update_user(conn, user_id, new_age):
    """ Update the age of an existing user """
    query = "UPDATE users SET age = ? WHERE id = ?;"
    conn.execute(query, (new_age, user_id))
    conn.commit()

def delete_user(conn, user_id):
    """ Delete a user from the users table """
    query = "DELETE FROM users WHERE id = ?;"
    conn.execute(query, (user_id,))
    conn.commit()

def main():
    """ Main function to execute database operations """
    conn = connect_to_db()
    create_table(conn)

    # Example operations
    insert_user(conn, "Alice", 30)
    insert_user(conn, "Bob", 24)

    print("Users after insertion:")
    users = get_users(conn)
    for user in users:
        print(user)

    update_user(conn, 1, 31)
    print("\nUsers after update:")
    users = get_users(conn)
    for user in users:
        print(user)

    delete_user(conn, 2)
    print("\nUsers after deletion:")
    users = get_users(conn)
    for user in users:
        print(user)

    conn.close()

if __name__ == "__main__":
    main()
