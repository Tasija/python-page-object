from selenium.webdriver.common.by import By


class LoginPageLocatars(object):
    USERNAME = (By.ID, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.ID, "btnLogin")
    WELCOME_MENU = (By.ID, "welcome")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/index.php/auth/logout']")
    CURRENT_TAB = (By.CSS_SELECTOR, "li.current")


class AdminPageLocator(object):
    ADMIN_TAB = (By.ID, "menu_admin_viewAdminModule")
    ADD_USER_BUTTON = (By.ID, "btnAdd")
    EMPLOYEE_NAME = (By.ID, "systemUser_employeeName_empName")
    USER_ROLE = (By.ID, "systemUser_userType")
    EMPLOYEE_USERNAME = (By.ID, "systemUser_userName")
    EMPLOYEE_STATUS = (By.ID, "systemUser_status")
    EMPLOYEE_PASSWORD = (By.ID, "systemUser_password")
    EMPLOYEE_CONFIRM_PASSWORD = (By.ID, "systemUser_confirmPassword")
    SAVE_EMPLOYEE = (By.ID, "btnSave")