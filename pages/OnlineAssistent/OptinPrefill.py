from copy import deepcopy
from pages.OnlineAssistent.Recomendation import RecomendationPage
from pages.Page import WeiterButtonPage
from selenium.webdriver.remote.webelement import WebElement
from elements.mywebelement import MyWebElement


class OptinPrefillPage(WeiterButtonPage):
    my_url = "/optin-prefill"
    _GEBURTSDATUM = 'geburtsdatum'
    _BESCHAEFTIGUNG = 'beschäftigungsstatus'
    _VERSICHERUNGSBEGINN = "versicherungsbeginn"
    _TARIF = 'tarif'
    _BEIHILFESATZ = 'beihilfesatz'
    _BEIHILFETRAEGER = "beihilfetraeger"

    locators = {_GEBURTSDATUM:
                './/div[contains(text(), "Geburtsdatum")]',
                _BESCHAEFTIGUNG:
                './/div[contains(text(), " Beschäftigungsstatus ")]',
                _VERSICHERUNGSBEGINN:
                './/div[contains(text(), " Versicherungsbeginn ")]',
                _TARIF:
                './/div[contains(text(), " Tarif ")]',
                _BEIHILFESATZ:
                './/div[contains(text(), " Beihilfesatz ")]',
                _BEIHILFETRAEGER:
                './/div[contains(text(), " Beihilfetraeger ")]'
                }

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def find_geburtsdatum_button(self)-> WebElement:
        return self.body.find_element_by_xpath(self.locators[self._GEBURTSDATUM])

    @property
    def find_beschaeftigungsstatus_button(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._BESCHAEFTIGUNG]))

    @property
    def find_versicherungsbeginn_button(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._VERSICHERUNGSBEGINN]))

    @property
    def find_tarif_button(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._TARIF]))

    @property
    def find_beihilfesatz_button(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._BEIHILFESATZ]))

    @property
    def find_beihilfetraeger_button(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._BEIHILFETRAEGER]))

    #def asserting_prefill_fields(self):
     #    text = self.find_geburtsdatum_button.goo
     #    t=self.