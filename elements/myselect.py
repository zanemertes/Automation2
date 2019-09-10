from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement
from elements.mywebelement import MyWebElement


class MySelect(Select, MyWebElement):
    def __init__(self, _we: WebElement):
        MyWebElement.__init__(self, _we=_we)
        Select.__init__(self, webelement=_we)

