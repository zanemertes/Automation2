from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from pages.Page import Page
from selenium.webdriver.support.select import Select
from pages.Page import WeiterButtonPage
from copy import deepcopy
from selenium.webdriver.remote.webelement import WebElement
from elements.mywebelement import MyWebElement

class ResultPage(WeiterButtonPage):
    my_url = "/ergebnis"
    _OFFER_DESCRIPTION = "offer description"
    _FIRST_CLASS = "first class"
    _KLINIK_EINBETT = "klinik einbett"
    _EMPFEHLUNG = 'empfehlung per email'
    _ANGEBOT = 'angebot berechnen'
    _BOTH = 'both'

    locators = {_EMPFEHLUNG:
                #TODO:Labels
                './/div/button[@class="btn btn-lg btn-outline-success btn-sm-block mr-2 ng-tns-c26-5"]',
                _ANGEBOT:
                # TODO:Labels
                './/div/button[contains(text(), " Angebot berechnen ")]',
                _OFFER_DESCRIPTION:
                './/oa-consultation-result-recommendation[@ng-reflect-tag="statutory-coverage"]',
                _FIRST_CLASS:
                './/div/span[contains(.," First Class ")]',
                _KLINIK_EINBETT:
                './/div/span[contains(.,"Klinik Einbett")]',
                _BOTH:
                '//ngc-tariff-block//span[contains(@class,"tariff-name")]'
                }

    './/input[contains(text(), " Ab dem 64. Lebensjahr  ")]',

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def find_recomendation_button(self)-> WebElement:
        return self.body.find_element_by_xpath(self.locators[self._EMPFEHLUNG])

    @property
    def find_beste_absicherung_button(self)-> WebElement:
        return self.body.find_element_by_xpath(self.locators[self._ANGEBOT])

    @property
    def find_offer_description(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._OFFER_DESCRIPTION]))

    @property
    def find_first_class_description(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._FIRST_CLASS]))

    @property
    def find_klinik_einbett_description(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._KLINIK_EINBETT]))

    # @property
    # def both(self) -> [MyWebElement]:
    #     return [MyWebElement(_we=web_element) for web_element in
    #             self.body.find_elements_by_xpath(self.locators[self._BOTH])]

    #def asserting_if_OA_equals_Email(self):
        #description_OA = self.find_offer_description.good_text
        #print("OA description: " + description_OA)
        #first_class_OA = self.find_first_class_description.good_text
        #print("OA first: " + first_class_OA)
        #klinik_einbett_OA = self.find_klinik_einbett_description.good_text
        #print("OA klinik einbett: " + klinik_einbett_OA)


#TODO: EXAMPLE
        # name_expected = user.name
        # name_actual = self.name_field.good_text
        #
        # surname_expected = user.surname
        # surname_actual = self.surname_field.good_text
        #
        # email_expected = user.email
        # email_actual = self.email_field.good_text
        #
        # interest_expected = user.interested_in
        # interest_actual = self.interest_select.first_selected_option.text
        #
        # print("Checking if {} == {}".format(name_expected, name_actual))
        # assert name_expected == name_actual
        # print("Name correct!")



class ResultPageClinik(WeiterButtonPage):
    my_url = "/ergebnis"
    _ANGEBOT_EMAIL = 'angebot per E-Mail'
    _WEITER = 'empfehlung per email'
    _DEIN_BEITRAG = "beitrag"

    locators = {_WEITER:
                #TODO:Labels
                './/div/button/span[contains(text(), "Weiter")]',
                _ANGEBOT_EMAIL:
                # TODO:Labels
                './/div/button[span[contains(.,"Angebot per E-Mail erhalten")]]',
                _DEIN_BEITRAG:
                ''}

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def find_weiter_button(self)-> WebElement:
        return self.body.find_element_by_xpath(self.locators[self._WEITER])

    @property
    def find_angebot_per_email_button(self)-> WebElement:
        return self.body.find_element_by_xpath(self.locators[self._ANGEBOT_EMAIL])