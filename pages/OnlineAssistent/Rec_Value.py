from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from pages.Page import Page
from selenium.webdriver.support.select import Select
from pages.Page import WeiterButtonPage
from copy import deepcopy
from selenium.webdriver.remote.webelement import WebElement
from elements.mywebelement import MyWebElement
from DataObjects.Users import OnlineAssistanceUsers


class ValuePage(WeiterButtonPage):
    my_url = "test/faktor"
    GRUNDVERSICHERUNG = "grundversicherung"
    PREIS = 'preis leistung'
    ABSICHERUNG = 'beste absicherung'

    BUTTONS = [PREIS,
               ABSICHERUNG,
               GRUNDVERSICHERUNG]

    locators = {PREIS:
                #TODO:Labels!!!!!!
                './/div/oa-tile[.//p[contains(text(),"Preis")]]',
                ABSICHERUNG:
                './/oa-tile[.//p[contains(text(),"Absicherung")]]',
                GRUNDVERSICHERUNG:
                './/oa-tile[.//p[contains(text(),"Grundsicherung")]]'
                }

    def __init__(self, driver, user: OnlineAssistanceUsers):
        super().__init__(driver)
        if user.occupation in [OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT_APPLICANT,
                               OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT] or \
                (user.occupation == OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE and user.is_user_rich):
            self.BUTTONS = [self.PREIS,
                            self.ABSICHERUNG,
                            self.GRUNDVERSICHERUNG]
        else:
            self.BUTTONS = [self.PREIS,
                            self.ABSICHERUNG]

    @property
    def find_preis_leistung_button(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self.PREIS]))

    @property
    def find_beste_absicherung_button(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self.ABSICHERUNG]))

    @property
    def find_grundversicherung_button(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self.GRUNDVERSICHERUNG]))

    def click_a_value(self, button_locator_name: str):
        # TODO: MyWebElement would need to store locators to enable this check
        # TODO: check if the button.locator is in the accepted list
        # if button.locator in _BUTTON_LOCATORS:
        #   button.click()
        # else:
        #   report problems, raise errors
        if button_locator_name in self.BUTTONS:
            button = MyWebElement(_we=self.body.find_element_by_xpath(self.locators[button_locator_name]))
        else:
            print("Button name '{0}' not supported".format(button_locator_name))
            raise ValueError
        print("clicking value = {}".format(button_locator_name))
        button.click()
