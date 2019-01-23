import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.pages import *
import time
import json


class TestUsers(unittest.TestCase):

    timestamp = str(int(time.time()))
    base_url = "http://opensource.demo.orangehrmlive.com"
    username = "Admin"
    password = "admin"
    new_user_dict = {"user_role":"ESS",
                     "name": "John Smith",
                     "user_name": timestamp,
                     "status": "Enabled",
                     "password": "test_pass" + timestamp}

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_create_user(self):

        pageLogin = LoginPage(self.driver, self.base_url)
        pageAdmin = AdminPage(self.driver, self.base_url)
        pageLogin.open(self.base_url)
        pageLogin.login(username=self.username, password=self.password)
        pageAdmin.navigate_to_admin_tab()
        pageAdmin.add_new_user(user_role=self.new_user_dict["user_role"],
                               name=self.new_user_dict["name"],
                               user_name=self.new_user_dict["user_name"],
                               status=self.new_user_dict["status"],
                               password=self.new_user_dict["password"])
        with open("new_user" + self.timestamp + ".txt", "w") as file:
            file.write(json.dumps(self.new_user_dict))
        pageLogin.logout()

        # login by new user
        pageLogin.login(username=self.new_user_dict["user_name"],
                        password=self.new_user_dict["password"])
        self.assertEqual("Dashboard", pageLogin.get_current_tab_name())


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUsers)
    unittest.TextTestRunner(verbosity=2).run(suite)