from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from pages.Page import Page

class TypeVersicherung(Page):
    my_url = "/berechnen/tarif-auswahl"
    VOLL_VERSICH = 'voll button'
    ZAHN_VERSICH = 'zahn button'
    CLINIK_VERSICH = 'clinik button'


    locators = {VOLL_VERSICH:
                './/ngc-product-card/div[@class="card mx-0 mx-sm-2"]',
                ZAHN_VERSICH:
                './/ngc-product-card/div[@class="card mx-0 mx-sm-2 scooter"]',
                CLINIK_VERSICH:
                './/ngc-product-card/div[@class="card mx-0 mx-sm-2 gossip"]'
                }

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def vollversicherung_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['voll button'])
