from selenium.webdriver.remote.webelement import WebElement
from elements.waitable import Waitable
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class KindForm(Waitable):
    _KID_DAY = "Kid day field"
    _KID_MONTH = "Kid month field"
    _KID_YEAR = "Kid year field"

    locators = {_KID_DAY:
                './/input[@ng-reflect-name="day"]',
                _KID_MONTH:
                './/input[@ng-reflect-name="month"]',
                _KID_YEAR:
                './/input[@ng-reflect-name="year"]'
                }

    def __init__(self, _we: WebElement):
        super().__init__(_we=_we)
        self.wait.until(EC.presence_of_element_located(locator=(By.XPATH, self.locators[self._KID_DAY])))
        # TODO: other elements

    @property
    def kid_field_day(self) -> WebElement:
        return self.find_element_by_xpath(self.locators[self._KID_DAY])

    @property
    def kid_field_month(self) -> WebElement:
        return self.find_element_by_xpath(self.locators[self._KID_MONTH])

    @property
    def kid_field_year(self) -> WebElement:
        return self.find_element_by_xpath(self.locators[self._KID_YEAR])
