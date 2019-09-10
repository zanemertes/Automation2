from selenium.webdriver.remote.webelement import WebElement
from pages.Page import Page


class StartPage(Page):
    my_url = "/start"
    # TODO: Create other page classes and clean up in here! ????
    _url_tarif_finden = "/test"
    # _url_beitrag_berechnen = "/berechnen/berufsstatus"
    _url_krankenversicherung = "/lernen"
    _url_beratung = "/beratung"
    from pages.OnlineAssistent.Tab2_BerufsStatus import BerufsStatusPage

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
    def beitrag_berechnen_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['beitrag berechnen button'])

    @property
    def krankenversicherung_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['krankenversicherung button'])

    @property
    def beratung_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['beratung button'])
