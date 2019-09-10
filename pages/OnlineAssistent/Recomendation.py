
# TODO:Fix email

from pages.Page import WeiterButtonPage
from elements.mywebelement import MyWebElement
from selenium.webdriver.remote.webelement import WebElement
from DataObjects import Users


class RecomendationPage(WeiterButtonPage):
    my_url = "/abschicken"
    _NAME = 'name'
    _SURNAME = 'surname'
    _EMAIL = 'email'
    _SEND = 'send email'

    locators = {_NAME:
                './/div/div/input[@formcontrolname="firstName"]',
                _SURNAME:
                './/div/div/input[@formcontrolname="lastName"]',
                _EMAIL:
                './/div/div/input[@formcontrolname="email"]',
                _SEND:
                './/div/button[contains(text(), "Senden")]'
                }

    @property
    def name_field(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._NAME]))

    @property
    def surname_field(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._SURNAME]))

    @property
    def email_field(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._EMAIL]))

    @property
    def find_send_button(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._SEND]))

    def input_data_from_user_for_recommendation(self, user: Users):
        self.name_field.send_keys(user.name)
        self.surname_field.send_keys(user.surname)
        self.email_field.send_keys(user.email)

    # def input_data_to_get_recomendation(self, name: str, surname: str, email: str)-> str:
    #     self.name_field.send_keys(name)
    #     self.surname_field.send_keys(surname)
    #     self.email_field.send_keys(email)



