from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from pages.Page import Page


class BerufsStatusPage(Page):
    my_url = "/berechnen/berufsstatus"

    locators = {'berufsstatus select':
                './/select',
                'weiter button':
                './/button[contains(text(), "Weiter")]'}

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def berufstatus_select(self) -> Select:
        return Select(webelement=self.body.find_element_by_xpath(xpath=self.locators['berufsstatus select']))

    @property
    def weiter_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['weiter button'])

    def check_weiter_button_is_disabled(self):
        assert not self.weiter_button.is_enabled()
        print("Weiter button disabled!")

    def check_weiter_button_is_enabled(self):
        assert self.weiter_button.is_enabled()
        print("Weiter button enabled!")
