"""Unit tests for the CRUD operations in main.py."""

import unittest
import main

class TestDatabaseOperations(unittest.TestCase):
    """ Test cases for the CRUD operations in main.py """

    def setUp(self):
        """ Set up a new database before each test """
        self.conn = main.connect_to_db(":memory:")
        main.create_table(self.conn)

    def tearDown(self):
        """ Close the connection after each test """
        self.conn.close()

    def test_insert_user(self):
        """ Test inserting a new user """
        main.insert_user(self.conn, "Test User", 25)
        users = main.get_users(self.conn)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], "Test User")
        self.assertEqual(users[0][2], 25)

    def test_update_user(self):
        """ Test updating an existing user """
        main.insert_user(self.conn, "Test User", 25)
        main.update_user(self.conn, 1, 30)
        users = main.get_users(self.conn)
        self.assertEqual(users[0][2], 30)

    def test_delete_user(self):
        """ Test deleting a user """
        main.insert_user(self.conn, "Test User", 25)
        main.delete_user(self.conn, 1)
        users = main.get_users(self.conn)
        self.assertEqual(len(users), 0)

if __name__ == "__main__":
    unittest.main()
