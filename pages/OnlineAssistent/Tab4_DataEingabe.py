from selenium.webdriver.remote.webelement import WebElement
from elements.mywebelement import MyWebElement
from elements.myselect import MySelect
from selenium.webdriver.support.select import Select
from dateutil.relativedelta import relativedelta
from datetime import date
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from copy import deepcopy
from pages.Page import WeiterButtonPage
import random
from time import sleep
from selenium import webdriver
from DataObjects import Users


class Eingabe(WeiterButtonPage):
    RANDOM = "RANDOM"
    my_url = "/eingabe"
    DAY = 'day'
    MONTH = 'month'
    YEAR = 'year'
    PREVIOUS_INSUR = 'previous insurance'
    INSURANCE_START = 'versicherungsbeginn'
    EMPLOYEES = 'anzahl mitarbeiter'
    NEW_INSURANCE_START_DATE = "start date"
    BEIHILFE_STATE = "beihilfetraeger"
    BEIHILFE_SATZ = "beihilfesatz"
    BEIHILFE_START_DAY = "beihilfe start day"
    BEIHILFE_START_MONTH = "beihilfe start month"
    VALIDATION = 'validation'

    locators = deepcopy(WeiterButtonPage.locators)
    locators.update({DAY:
                     './/div/input[@formcontrolname="day"]',
                     MONTH:
                     './/div/input[@formcontrolname="month"]',
                     YEAR:
                     './/div/input[@formcontrolname="year"]',
                     PREVIOUS_INSUR:
                     './/div/select[@formcontrolname="previous_insurance"]',
                     INSURANCE_START:
                     './/div/select[@formcontrolname="ingress_date"]',
                     EMPLOYEES:
                     './/div/input[@formcontrolname="employees"]',
                     VALIDATION:
                     './/div[@class="validation-message-text text-danger ng-star-inserted"]',
                     NEW_INSURANCE_START_DATE:
                    './/div/select[@formcontrolname="ingress_date"]',
                     BEIHILFE_STATE: #17
                     './/div/select[@formcontrolname="state"]',
                     BEIHILFE_SATZ:
                     './/div/select[@formcontrolname="beihilfesatz"]',
                     BEIHILFE_START_DAY:
                    './/div[@class="d-flex"]/div/input[@formcontrolname="day"]',
                     BEIHILFE_START_MONTH:
                    './/div/select[@formcontrolname="month"]',
                     })

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def day_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self.DAY])

    @property
    def month_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self.MONTH])

    @property
    def year_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self.YEAR])

    @property
    def previous_insurance_select(self) -> MySelect:
        return MySelect(_we=self.body.find_element_by_xpath(self.locators[self.PREVIOUS_INSUR]))

    @property
    def insurance_start_date_select(self) -> MySelect:
        return MySelect(_we=self.body.find_element_by_xpath(self.locators[self.INSURANCE_START]))

    @property
    def select_state_for_beihilfe(self) -> MySelect:
        return MySelect(_we=self.body.find_element_by_xpath(self.locators[self.BEIHILFE_STATE]))

    @property
    def select_satz_for_beihilfe(self) -> MySelect:
        return MySelect(_we=self.body.find_element_by_xpath(self.locators[self.BEIHILFE_SATZ]))

    @property
    def beihilfe_day(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self.BEIHILFE_START_DAY])

    @property
    def beihilfe_month(self) -> MySelect:
        return MySelect(_we=self.body.find_element_by_xpath(self.locators[self.BEIHILFE_START_MONTH]))

    #@property
    #def interest_select(self) -> MySelect:
     #   return MySelect(_we=self.body.find_element_by_xpath(self.locators[self._INTEREST]))

    @property
    def employees_input(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self.EMPLOYEES])

    @property
    def validation(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['validation'])

    def input_30yo(self):
        self.day_field.clear()
        self.day_field.send_keys(datetime.now().day)

        self.month_field.clear()
        self.month_field.send_keys(datetime.now().month)

        self.year_field.clear()
        self.year_field.send_keys(datetime.now().year-30)

    def randomly_choosing_worker_amount_selbstandig(self):
        mitarbeiter_anzahl = random.randint(1, 100)
        self.employees_input.send_keys(mitarbeiter_anzahl)

    def select_previous_insurance_by_text(self):
        import random

        _ui_options = ['Gesetzlich','Privat', 'Im Ausland']
        previous_insurance = random.choice(_ui_options)
        # log info
        print("Selecting previous insurance'{0}'".format(previous_insurance))
        # do the selection
        self.previous_insurance_select.select_by_visible_text(previous_insurance)
        return previous_insurance

    def select_randomly_beihilfe_state(self):
        import random
        index = range(1,18)
        beihilfe_state = random.choice(index)
        self.select_state_for_beihilfe.select_by_index(beihilfe_state)
        sleep(2)
        beihilfe_state = self.select_state_for_beihilfe.good_text
        print("Selecting beihilhe state'{0}'".format(beihilfe_state))


    def select_randomly_beihilfe_satz(self):

        index = range(1,4)
        beihilfe_satz = random.choice(index)
        print("Selecting beihilhe satz'{0}'".format(beihilfe_satz))
        self.select_satz_for_beihilfe.select_by_index(beihilfe_satz)

    def input_beihilfe_start(self):
        self.beihilfe_day.clear()
        self.beihilfe_day.send_keys(1)

    def select_randomly_beihilfe_start(self):
        import random
        index = range(1,7)
        beihilfe_start = random.choice(index)
        print("Selecting beihilfe sart'{0}'".format(beihilfe_start))
        self.beihilfe_month.select_by_index(beihilfe_start)


    def input_birthdate_clinik (self, user: Users):
        self.day_field.clear()
        self.day_field.send_keys(user.date_of_birth.day)

        self.month_field.clear()
        self.month_field.send_keys(user.date_of_birth.month)

        self.year_field.clear()
        self.year_field.send_keys(user.date_of_birth.year)

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
        condition_ok = d - relativedelta(years=18) >= nd > d - relativedelta(years=39)
        condition_too_old = d - relativedelta(years=39) >= nd > d - relativedelta(years=99)
        condition_archaeology = d - relativedelta(years=99) > nd

        if condition_future:
            print("Age test: future")
            self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, self.locators['validation'])))
            assert self.validation.text == "Du kannst dich erst ab 18 allein versichern!"
            print("SUCCESS")
            return False

        # Too young
        elif condition_too_young:
            print("Age test: too young")
            self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, self.locators['validation'])))
            assert self.validation.text == "Du kannst dich erst ab 18 allein versichern!"
            print("SUCCESS")
            return False

        # OK
        elif condition_ok:
            print("Age test: correct age")
            print("No validation messages are even expected")
            return True

        # Too old
        elif condition_too_old: #TODO: Fix in Jenkins
            print("Age test: too old")
            self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, self.locators['validation'])))
            assert self.validation.text == "Du kannst dich nur bis 39 bei uns versichern."
            print("SUCCESS")
            return False

        # Over hundred years old
        elif condition_archaeology: #TODO: Fix in Jenkins
            print("Age test: WAY too old")
            self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, self.locators['validation'])))
            assert self.validation.text == "Du kannst dich nur bis 39 bei uns versichern."
            print("SUCCESS")
            return False



    # def select_previous_insurance_by_text(self, previous_insurance: str):
    #     import random
    #
    #     #_options = ['Privat', 'Gesetzlich', 'Im Ausland', self.RANDOM]
    #     _ui_options = ['Privat', 'Gesetzlich', 'Im Ausland']
    #
    #     # handle the (un)expected problems
    #     if previous_insurance not in _options:
    #         print("Insurance type is not existent in the possible options.")
    #         raise ValueError
    #
    #     # handle the randomization
    #     if previous_insurance == self.RANDOM:
    #         previous_insurance = random.choice(_ui_options)
    #
    #     # log info
    #     print("Selecting '{0}'".format(previous_insurance))
    #     # do the selection
    #     self.previous_insurance_select.select_by_visible_text(previous_insurance)

# assert that the 'insurance_date' is > begin of next month and < begin of next month + 6mo?

    def assert_insurance_start_date(self):
        for index in range(1, 7):
            self.previous_insurance_select.select_by_index(index)
            start_date_str = self.previous_insurance_select.first_selected_option.text.strip()
            print(start_date_str)
            onemonth = date.today() + relativedelta(months=1, day=1)
            sixmonth = date.today() + relativedelta(months=6, day=1)
            insurance_date = datetime.strptime(start_date_str, '%d.%m.%Y').date()
            assert onemonth <= insurance_date <= sixmonth
            print("SUCCESS")

    def select_insurance_start_date(self):
        for x in range(1):
            ind = random.randint(1, 6)
            print(ind)
            print(self.insurance_start_date_select.all_selected_options)
            self.insurance_start_date_select.select_by_index(ind)
            # print(self.insurance_start_date_select.first_selected_option)
            # start_date_input = self.previous_insurance_select.first_selected_option.text.strip()
            # print(start_date_input)

    def input_all_data(self,
                       age_in_years: int,
                       difference_in_days: int):
        self.select_previous_insurance_by_text()
        self.select_insurance_start_date()
        self.assert_conditions_on_weiter_button(age_in_years=age_in_years,
                                                difference_in_days=difference_in_days)
        #if self.check_weiter_button_is_enabled():
            #self.weiter_button.click()

    # def input_all_data(self,
    #                    age_in_years: int, difference_in_days: int,
    #                    previous_insurance_type: str,
    #                    insurance_start_date: date):
    #     self.input_date_of_birth_and_assert_validations(age_in_years=age_in_years,
    #                                                     difference_in_days=difference_in_days)
    #     self.select_previous_insurance_by_text(previous_insurance=previous_insurance_type)
    #     self.assert_insurance_start_date(insurance_start_date)
    #
    #     # make sure the weiter button is enabled/disabled as expected
    #     self.assert_conditions_on_weiter_button()
    #
    #     # in case it is enabled - click it
    #     if self.check_weiter_button_is_enabled():
    #         self.weiter_button.click()

    def assert_conditions_on_weiter_button(self,
                                           age_in_years: int,
                                           difference_in_days: int):
        # in case validations appear - button should be disabled
        if not self.input_date_of_birth_and_assert_validations(age_in_years=age_in_years,
                                                               difference_in_days=difference_in_days):
            self.check_weiter_button_is_disabled()
            #self.check_weiter_button_is_enabled()
        else:
            self.check_weiter_button_is_enabled()
            #self.check_weiter_button_is_disabled()

class Beitragsentlastung(WeiterButtonPage):
    my_url = "/beitragsentlastung"
    Lebensjahr64 = "Lebensjahr64"
    Lebensjahr67 = "Lebensjahr67"

    locators = deepcopy(WeiterButtonPage.locators)
    locators.update({Lebensjahr64:
                         './/label[contains(text(), " Ab dem 64. Lebensjahr")]',
                     Lebensjahr67:
                         './/label[contains(text(), " Ab dem 67. Lebensjahr")]',
                     })
    @property
    def random_lebensjahr_button(self) -> MyWebElement:
        return random.choice([self.find_lebensjahr64_button,
                              self.find_lebensjahr67_button])

    @property
    def find_lebensjahr64_button(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self.Lebensjahr64]))

    @property
    def find_lebensjahr67_button(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self.Lebensjahr67]))


class UbertragungswertPage(WeiterButtonPage):
    my_url = "/uebertragungswert"
    Uebertragungswert = "uebertragungswert"

    locators = deepcopy(WeiterButtonPage.locators)
    locators.update({Uebertragungswert:
                         './/input',
                     })

    @property
    def find_uebertragungswert_input(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self.Uebertragungswert]))

    def input_uebertragungswert(self):
        self.find_uebertragungswert_input.send_keys(200)
