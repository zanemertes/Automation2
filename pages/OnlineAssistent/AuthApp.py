from pages.Page import WeiterButtonPage
from copy import deepcopy
from selenium.webdriver.remote.webelement import WebElement
from elements.mywebelement import MyWebElement

class AuthAppPage(WeiterButtonPage):
    my_url = "/auth-app"

    def __init__(self, driver):
        super().__init__(driver)