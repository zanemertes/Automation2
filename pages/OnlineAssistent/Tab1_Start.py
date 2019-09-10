from selenium.webdriver.remote.webelement import WebElement
from pages.Page import Page
from pages.OnlineAssistent.Tab2_BerufsStatus import BerufsStatusPage

class StartPage(Page):
    my_url = "/start"
    _url_tarif_finden = "/test"
    _url_krankenversicherung = "/lernen"
    _url_beratung = "/beratung"


    locators = {'tarif finden button':
                './/oa-tile[contains(@ng-reflect-navigate-to,"' + _url_tarif_finden + '")]',
                'beitrag berechnen button':
                './/oa-tile[contains(@ng-reflect-navigate-to,"' + BerufsStatusPage.my_url + '")]',
                'krankenversicherung button':
                './/oa-tile[contains(@ng-reflect-navigate-to,"' + _url_krankenversicherung + '")]',
                'beratung button':
                './/oa-tile[contains(@ng-reflect-navigate-to,"' + _url_beratung + '")]'}

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def find_tariff_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['tarif finden button'])

    @property
    def find_beitrag_berechnen_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['beitrag berechnen button'])

    @property
    def find_krankenversicherung_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['krankenversicherung button'])

    @property
    def find_beratung_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['beratung button'])


