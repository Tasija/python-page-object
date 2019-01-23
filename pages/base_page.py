from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    def __init__(self, driver, base_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        self.wait = WebDriverWait(driver, self.timeout)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
