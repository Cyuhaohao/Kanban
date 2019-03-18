import os
import unittest
from Kanban import app, db

TEST_DB='test.db'

class BasicTests(unittest.TestCase):
    # Set up the initial conditions for the unit tests
    def setUp(self):
        app.config['TESTING']=True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        # Randomly generate test data
        self.title1="d89ed838eeui3"
        self.description1="3heuh3eiu2h23k"
        self.title2 = "d32oiuo389uj"
        self.description2 = "8dh9238h3r32r"
        self.title3 = "90du9033d"
        self.description3 = "93u9djofh233je"

    def tearDown(self):
        pass

    # Test entering the home page
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Test new event creating
    def test_create_doing(self):
        response = self.app.get('/add1', data = dict(title1=self.title1,description1=self.description1),follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_create_todo(self):
        response = self.app.get('/add2', data = dict(title2=self.title2,description2=self.description2),follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_create_done(self):
        response = self.app.get('/add3', data = dict(title3=self.title3,description3=self.description3), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    # Test all nine possible buttons to edit an event on the page
    def test_doing_to_done(self):
        response = self.app.get('/change1', data = dict(doing="Done",title=self.title1,description=self.description1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_todo_to_doing(self):
        response = self.app.get('/change2', data = dict(todo="Doing",title=self.title2,description=self.description2), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_done_to_todo(self):
        response = self.app.get('/change3', data = dict(done="Todo",title=self.title3,description=self.description3), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_doing_to_todo(self):
        response = self.app.get('/change1', data = dict(doing="Todo",title=self.title2,description=self.description2), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_todo_to_done(self):
        response = self.app.get('/change2', data = dict(todo="Done",title=self.title3,description=self.description3), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_done_to_doing(self):
        response = self.app.get('/change3', data = dict(done="Doing",title=self.title1,description=self.description1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_doing_delete(self):
        response = self.app.get('/change1', data = dict(doing="Delete"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_todo_delete(self):
        response = self.app.get('/change2', data = dict(todo="Delete"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_done_delete(self):
        response = self.app.get('/change3', data = dict(done="Delete"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__=='__main__':
    unittest.main()