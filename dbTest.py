import unittest
from pyTOsql.py import *

class TestUM(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect('Data.db')
        self.cursor = self.con.cursor()
        init_db(self.cursor)
        self.con.commit()

    def tearDown(self):
        self.con.commit()
        self.con.close()

    def test_request1(self):
        self.assertEqual(task1(self.cursor), "Kristina")

if __name__ == "__main__":
    unittest.main(failfast=True)

