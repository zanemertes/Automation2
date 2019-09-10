from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from dateutil.relativedelta import relativedelta
from datetime import date
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from copy import deepcopy
from pages.Page import WeiterButtonPage


class Eingabe(WeiterButtonPage):
    RANDOM = "RANDOM"
    my_url = "/berechnen/krankenversicherung/eingabe"
    locators = deepcopy(WeiterButtonPage.locators)
    locators.update({'day':
                     './/div/input[@formcontrolname="day"]',
                     'month':
                     './/div/input[@formcontrolname="month"]',
                     'year':
                     './/div/input[@formcontrolname="year"]',
                     'previous insurance':
                     './/div/select[@formcontrolname="previous_insurance"]',
                     'versicherungsbeginn':
                     './/div/select[@formcontrolname="ingress_date"]',
                     'validation':
                     './/div[@class="validation-message-text text-danger ng-star-inserted"]'
                     })



    def __init__(self, driver):
        super().__init__(driver)

    @property
    def day_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['day'])

    @property
    def month_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['month'])

    @property
    def year_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['year'])

    @property
    def previous_insurance_select(self) -> Select:
        return self.body.find_element_by_xpath(self.locators['previous insurance'])

    @property
    def versicherungsbeginn_select(self) -> Select:
        return self.body.find_element_by_xpath(self.locators['versicherungsbeginn'])

    @property
    def validation(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['validation'])

    def input_date_of_birth_and_assert_validations(self, age_in_years: int, difference_in_days: int) \
            -> bool:
        d = date.today()
        _rd = relativedelta(years=age_in_years) + relativedelta(days=difference_in_days)
        nd = d - _rd

        self.day_field.clear()
        self.day_field.send_keys(nd.day)

        self.month_field.clear()
        self.month_field.send_keys(nd.month)

        self.year_field.clear()
        self.year_field.send_keys(nd.year)

        # WTH are you doing??
        condition_future = nd > d - relativedelta(days=0)
        condition_too_young = d - relativedelta(days=0) >= nd > d - relativedelta(years=18)
        condition_ok = d - relativedelta(years=18) >= nd > d - relativedelta(years=38)
        condition_too_old = d - relativedelta(years=38) >= nd > d - relativedelta(years=99)
        condition_archaeology = d - relativedelta(years=99) > nd

        if condition_future:
            print("Age test: future")
            self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, self.locators['validation'])))
            assert self.validation.text == "Du kannst dich erst ab 18 allein versichern!"
            # TODO: log messages upon success
            print("SUCCESS")
            return False
            self.check_weiter_button_is_disabled

        # Too young
        elif condition_too_young:
            print("Age test: too young")
            self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, self.locators['validation'])))
            assert self.validation.text == "Du kannst dich erst ab 18 allein versichern!"
            print("SUCCESS")
            return False
            self.check_weiter_button_is_disabled
        # OK
        elif condition_ok:
            print("Age test: correct age")
            print("No validation messages are even expected")
            return True
            self.check_weiter_button_is_enabled
        # Too old
        elif condition_too_old:
            print("Age test: too old")
            self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, self.locators['validation'])))
            assert self.validation.text == "Du kannst bis 38 als Student versichert sein!"
            print("SUCCESS")
            return False
            self.check_weiter_button_is_disabled
        # Dude!  STAHP!!!
        elif condition_archaeology:
            print("Age test: WAY too old")
            self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, self.locators['validation'])))
            assert self.validation.text == "Du kannst dich nur bis 99 bei uns versichern."
            print("SUCCESS")
            return False
            self.check_weiter_button_is_disabled

    def input_previous_insurance(self, value: str):
        if value == self.RANDOM:
            self.select_random_previous_insurance()
        else:
            self.previous_insurance_select.select_by_visible_text(value)

    def select_random_previous_insurance(self):
        import random

        _options = ['Privat', 'Gesetzlich', 'Im Ausland']
        _random_option = random.choice(_options)
        print("Selecting '{0}'".format(_random_option))
        self.previous_insurance_select.select_by_visible_text(_random_option)

    def input_insurance_start_date(self, insurance_date: date):
        # TODO: can you assert that the 'insurance_date' is > begin of next month and < begin of next month + 6mo?
        start_date=self.versicherungsbeginn_select.select_by_visible_text(insurance_date.strftime("%d.%m.%Y"))
        d = date.today()
        assert start_date




    def input_all_data(self,
                       age_in_years: int, difference_in_days: int,
                       previous_insurance_type: str,
                       insurance_start_date: date):
        self.input_date_of_birth_and_assert_validations(age_in_years=age_in_years,
                                                        difference_in_days=difference_in_days)
        self.select_random_previous_insurance(previous_insurance_type)
        self.input_insurance_start_date(insurance_start_date)

        self.check_weiter_button_is_enabled()
        self.weiter_button.click()

    #def check_weiter_button_according_to_the_necessity(self):
        #if self.condition


    # initial
    # framework - pages
    # generic
    # page
    #
    # class
    #     page
    #     classes
    #     for the 'Start' and 'Berufsstatus'
    #         properties
    #     for buttons and other page elements
    #
    # __init__
    # method
    # super.__init__
    # method
    # relativedelta
    # from dateutil package
    # adjusting
    # the
    # 'Age = 18y - 1d'
    # case
    # to
    # use
    # new
    # framework