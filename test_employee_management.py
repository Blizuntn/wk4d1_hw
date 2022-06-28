import unittest
from employee_management import Role, Manager, Employee, Supervisor, Post


class TestEmployeeManagement(unittest.TestCase):

    def test_email(self):
        emp1 = Employee(first_name="mike",last_name="booz",role_id=3)
        self.assertEqual(emp1.email, "mikeb@codingtemple.com")
    def test_if_employee_was_added(self):
        emp2 = Employee(first_name="mister", last_name="wiley", role_id=3)
        self.assertIn(emp2,emp2.all_)
    def test_employees_length(self):
        mng1 = Manager(first_name="floss", last_name="carter",role_id=2,employees=[])
        emp1 = Employee(first_name="mike",last_name="booz",role_id=3)
        emp2 = Employee(first_name="mister", last_name="wiley", role_id=3)
        mng1.add_employee(emp1)
        mng1.add_employee(emp2)
        self.assertIn(emp1,mng1.employees)
        self.assertNotEqual(len(mng1.employees), 1)
    def test_erased_employees(self):
        sup = Supervisor(first_name="James", last_name="Scott",role_id=1,employees=[])
        mng1 = Manager(first_name="floss", last_name="carter",role_id=2,employees=[])
        emp1 = Employee(first_name="mike",last_name="booz",role_id=3)
        emp2 = Employee(first_name="mister", last_name="wiley", role_id=3)
        sup.add_employee(mng1)
        sup.add_employee(emp1)
        sup.add_employee(emp2)
        sup.remove_employee(mng1.email)
        self.assertNotEqual(len(sup.employees),3)
        self.assertNotIn(mng1, sup.employees)

    def test_in_the_body(self):

        mng1 = Manager(first_name="floss", last_name="carter",role_id=2,employees=[])

        post1 = Post("this is supposed to be a secret but i dont know can i tell you",mng1.email)
        self.assertTrue((len(post1.body) > 1),"the secret is that its not empty")

if __name__ == '__main__':
    unittest.main()
