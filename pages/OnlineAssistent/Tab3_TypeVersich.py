from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from pages.Page import Page
from pages.Page import WeiterButtonPage
import random

class TypeVersicherung(WeiterButtonPage):
    my_url = "/berechnen/tarif-auswahl"
    FULL_INSURANCE = 'voll button'
    DENTAL_INSURANCE = 'zahn button'
    CLINIK_INSURANCE = 'clinik button'

    locators = {FULL_INSURANCE:
                './/ngc-product-card/div[@ng-reflect-klass="card mx-0 mx-sm-2"]',
                DENTAL_INSURANCE:
                './/ngc-product-card/div[@class="card mx-0 mx-sm-2 scooter"]',
                CLINIK_INSURANCE:
                './/ngc-product-card/div[@class="card mx-0 mx-sm-2 gossip"]'}

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def find_vollversicherung_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self.FULL_INSURANCE])

    @property
    def find_dental_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self.DENTAL_INSURANCE])

    @property
    def find_clinik_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self.CLINIK_INSURANCE])

    OA_ALLOWED_INSURANCES = [find_vollversicherung_button,
                             find_dental_button,
                             find_clinik_button]

    randomly_chosing_insurance_type = random.choice(OA_ALLOWED_INSURANCES)


