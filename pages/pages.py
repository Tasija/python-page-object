from pages.base_page import Page
from pages.locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class LoginPage(Page):
    def __init__(self, driver, base_url):
        self.locator = LoginPageLocatars
        super(LoginPage, self).__init__(driver, base_url)

    def enter_username(self, username):
        self.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def logout(self):
        self.find_element(*self.locator.WELCOME_MENU).click()
        logout = self.wait.until(EC.visibility_of_element_located(self.locator.LOGOUT_BUTTON))
        logout.click()
        self.wait.until(EC.visibility_of_element_located(self.locator.USERNAME))

    def get_current_tab_name(self):
        return self.find_element(*self.locator.CURRENT_TAB).text

class AdminPage(Page):
    def __init__(self, driver, base_url):
        self.locator = AdminPageLocator
        super(AdminPage, self).__init__(driver, base_url)

    def navigate_to_admin_tab(self):
        self.find_element(*self.locator.ADMIN_TAB).click()
        self.wait.until(EC.element_to_be_clickable(self.locator.ADD_USER_BUTTON))

    def click_add_new_user_button(self):
        self.find_element(*self.locator.ADD_USER_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(self.locator.EMPLOYEE_NAME))

    def set_employee_name(self, employee_name):
        self.find_element(*self.locator.EMPLOYEE_NAME).send_keys(employee_name)

    def select_user_role(self, role):
        Select(self.find_element(*self.locator.USER_ROLE)).select_by_visible_text(role)

    def set_user_name(self, user_name):
        self.find_element(*self.locator.EMPLOYEE_USERNAME).send_keys(user_name)

    def set_user_status(self, status):
        Select(self.find_element(*self.locator.EMPLOYEE_STATUS)).select_by_visible_text(status)

    def set_password(self, password):
        self.find_element(*self.locator.EMPLOYEE_PASSWORD).send_keys(password)

    def confirm_password(self, password):
        self.find_element(*self.locator.EMPLOYEE_CONFIRM_PASSWORD).send_keys(password)

    def click_save_employee_button(self):
        self.find_element(*self.locator.SAVE_EMPLOYEE).click()

    def add_new_user(self, user_role, name, user_name, status, password):
        self.click_add_new_user_button()
        self.select_user_role(role=user_role)
        self.set_employee_name(employee_name=name)
        self.set_user_name(user_name=user_name)
        self.set_user_status(status=status)
        self.set_password(password=password)
        self.confirm_password(password=password)
        self.click_save_employee_button()
        self.wait.until(EC.visibility_of_element_located(self.locator.ADD_USER_BUTTON))

