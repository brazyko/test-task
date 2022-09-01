from main import Users, Expenses, Category
from functions import *


import unittest
from main import Users, Expenses, Category
from functions import *


class test_quit_program(unittest.TestCase):
    def setUp(self):
        self.quit_program = quit_program()

    def testQuitProgram(self):
        self.assertEqual(quit_program(), 'See you later!')

"""
class test_clear_data(unittest.TestCase):
    def setUp(self):
        self.clear_data = clear_data()

    def testClearData(self):
        self.assertEqual(db_session.query(Users).first(), None)
        self.assertEqual(db_session.query(Expenses).first(), None)
        self.assertEqual(db_session.query(Category).first(), None)
        self.assertEqual(clear_data(), 'All data have been deleted')


class test_add_category(unittest.TestCase):
    def setUp(self):
        self.category = Category()
        self.user = db_session.query(Users).filter_by(user_name='admin').first()
        self.add_category = add_category(self.user)

    def testAddCategory(self):
        self.add_category(user=self.user, category_name='test')
        self.assertEqual(db_session.query(Category).filter_by(category_name='test'), 'test')
"""