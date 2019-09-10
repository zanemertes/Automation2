from selenium.webdriver.support.select import Select
from pages.Page import WeiterButtonPage
from copy import deepcopy
from elements.mywebelement import MyWebElement
from DataObjects.Users import OnlineAssistanceUsers
import random


class BerufsStatusPage(WeiterButtonPage):
    my_url = "/berechnen/berufsstatus"
    _BERUFSTATUS = "berufsstatus select"
    _INCOME = "bruttoeinkommen"

    locators = deepcopy(WeiterButtonPage.locators)
    locators.update({_BERUFSTATUS:
                     './/select',
                     _INCOME:
                     './/input'
                     })

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def berufstatus_select(self) -> Select:
        return Select(webelement=self.body.find_element_by_xpath(xpath=self.locators[self._BERUFSTATUS]))

    @property
    def income_input(self) -> MyWebElement:
        return self.body.find_element_by_xpath(xpath=self.locators[self._INCOME])

    def randomly_selecting_employment_status(self):
        random_user = random.choice(OnlineAssistanceUsers.OA_ALLOWED_OCCUPATIONS)
        self.berufstatus_select.select_by_visible_text(random_user)
        if random_user == OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE:
            self.income_input.send_keys(OnlineAssistanceUsers.generate_random_income(rich=True))



    # @property
    # def weiter_button(self) -> WebElement:
    #     return self.body.find_element_by_xpath(self.locators['weiter button'])
    #
    # def check_weiter_button_is_disabled(self):
    #     assert not self.weiter_button.is_enabled()
    #     print("Weiter button disabled!")
    #
    # def check_weiter_button_is_enabled(self):
    #     assert self.weiter_button.is_enabled()
    #     print("Weiter button enabled!")
