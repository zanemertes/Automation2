# TODO: Fix loop

from selenium.webdriver.support.select import Select
from pages.Page import WeiterButtonPage
from copy import deepcopy
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from dateutil.relativedelta import relativedelta
from datetime import date
from copy import deepcopy
import random

from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement

from DataObjects import Users

from elements.mywebelement import MyWebElement
from objects.KindForm import KindForm
from pages.Page import WeiterButtonPage


class TariffPage(WeiterButtonPage):
    my_url = "/eingabe"
    _DAY = 'day'
    _MONTH = 'month'
    _YEAR = 'year'
    _OCCUPATION = 'berufsstatus select'
    _INCOME = 'income'
    _PREVIOUS_INSURANCE = 'previous versicherung select'
    _MITARBEITER_ANZAHL = 'mitarbeiter anzahl'
    _FUTURE_CIVIL = "zukünftiger beamter"
    _STATE_BEIHILFE = "beihilfeträger"
    OA_EMPLOYEE = "Angestellter"
    OA_SELF_EMPLOYED = "Selbstständig"
    OA_CIVIL_SERVANT = "Beamter"
    OA_CIVIL_SERVANT_APPLICANT = "Beamtenanwärter"
    OA_STUDENT = "Student oder in Ausbildung"
    OA_PRIVATE = "privat"
    OA_GOVERN = "gesetzlich"
    OA_JA = "Ja"
    OA_NEIN = "Nein"
    _KID = "+Kid"
    _KID_DAY = "Kid day field"
    _KID_MONTH = "Kid month field"
    _KID_YEAR = "Kid year field"
    _KID2_DAY = "Kid 2 day field"
    _KID_FORM = "Kid form"

    locators = deepcopy(WeiterButtonPage.locators)
    locators.update({_DAY:
                     './/div/input[@ng-reflect-name="day"]',
                     _MONTH:
                     './/div/input[@ng-reflect-name="month"]',
                     _YEAR:
                     './/div/input[@ng-reflect-name="year"]',
                     _OCCUPATION:
                     './/select[@id="occupational_status"]',
                     # TODO:Labels!!
                     _INCOME:
                     './/ngc-money-sum-input//input',
                     _PREVIOUS_INSURANCE:
                     './/select[@formcontrolname="previous_insurance"]',
                     _MITARBEITER_ANZAHL:
                     './/input[@formcontrolname="employees"]',
                     _FUTURE_CIVIL:
                     './/select[@formcontrolname="studying_teacher"]',
                     _STATE_BEIHILFE:
                     './/select[@formcontrolname="state"]',
                     _KID:
                     './/div/button[contains(text(), " + Kind ")]',
                     _KID_FORM:
                     './/oa-children-form/div',
                     # _KID_DAY:
                     # # './/div/input[@ng-reflect-name="day" and @class="form-control form-control-lg text-center ng-pristine ng-invalid ng-touched"]',
                     # './/oa-children-form//div/input[@ng-reflect-name="day"and @class="form-control form-control-lg text-center ng-pristine ng-invalid ng-touched"]',
                     # _KID_MONTH:
                     # './/div/input[@ng-reflect-name="month"and @class="form-control form-control-lg text-center ng-untouched ng-pristine ng-invalid"]',
                     # _KID_YEAR:
                     # './/div/input[@ng-reflect-name="year"and @class="form-control form-control-lg text-center ng-untouched ng-pristine ng-invalid"]',
                     # _KID2_DAY:
                     # './/div/input[@ng-reflect-name="day" and @class="form-control form-control-lg text-center ng-pristine ng-invalid ng-touched"]',
                     })

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def berufstatus_select(self) -> Select:
        return Select(self.body.find_element_by_xpath(xpath=self.locators[self._OCCUPATION]))

    @property
    def kid_forms(self) -> [KindForm]:
        return [KindForm(_we=_we) for _we in self.body.find_elements_by_xpath(self.locators[self._KID_FORM])]

    @property
    def kid_field(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._KID]))

    # @property
    # def kid_field_day(self) -> WebElement:
    #     return self.body.find_element_by_xpath(self.locators[self._KID_DAY])
    #
    # @property
    # def kid_field_month(self) -> WebElement:
    #     return self.body.find_element_by_xpath(self.locators[self._KID_MONTH])
    #
    # @property
    # def kid_field_year(self) -> WebElement:
    #     return self.body.find_element_by_xpath(self.locators[self._KID_YEAR])

    @property
    def previous_insurance_select(self) -> Select:
        return Select(self.body.find_element_by_xpath(xpath=self.locators[self._PREVIOUS_INSURANCE]))

    @property
    def future_civil_servant_select(self) -> Select:
        return Select(self.body.find_element_by_xpath(xpath=self.locators[self._FUTURE_CIVIL]))

    @property
    def beihilfetreager_select(self) -> Select:
        return Select(self.body.find_element_by_xpath(xpath=self.locators[self._STATE_BEIHILFE]))

    @property
    def employee_amount_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self._MITARBEITER_ANZAHL])

    @property
    def day_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self._DAY])

    @property
    def month_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self._MONTH])

    @property
    def year_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self._YEAR])

    @property
    def income_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self._INCOME])

    # def input_income(self, user: Users):
    #      self.income_field.send_keys(user.income)
    #
    # def input_future_cs(self, user: Users):
    #      self.future_civil_servant_select.select_by_visible_text(user.csapplicant)

    def input_data_kid_by_form(self, kid_form_number: int):
        self.kid_field.scroll_into_view()
        self.kid_field.click()

        self.kid_forms[kid_form_number].kid_field_day.clear()
        self.kid_forms[kid_form_number].kid_field_day.send_keys(1)

        self.kid_forms[kid_form_number].kid_field_month.clear()
        self.kid_forms[kid_form_number].kid_field_month.send_keys(1)

        self.kid_forms[kid_form_number].kid_field_year.clear()
        self.kid_forms[kid_form_number].kid_field_year.send_keys(2010)

    # def input_data_kid(self):
    #     from time import sleep
    #     self.kid_field.scroll_into_view()
    #     self.kid_field.click()
    #     sleep(1)
    #     # self.wait.until(EC.presence_of_element_located(self.locators[self._KID_DAY]))
    #
    #     self.kid_field_day.clear()
    #     self.kid_field_day.send_keys(1)
    #
    #     self.kid_field_month.clear()
    #     self.kid_field_month.send_keys(1)
    #
    #     self.kid_field_year.clear()
    #     self.kid_field_year.send_keys(2010)

    def input_data_from_user(self, user: Users):
        # date of birth magic
        self.day_field.clear()
        self.day_field.send_keys(user.date_of_birth.day)

        self.month_field.clear()
        self.month_field.send_keys(user.date_of_birth.month)

        self.year_field.clear()
        self.year_field.send_keys(user.date_of_birth.year)
        # specifies the occupation
        self.berufstatus_select.select_by_visible_text(user.occupation)
        # specifies the income ... if necessary
        if user.occupation == user.OA_OCCUPATION_EMPLOYEE:
            self.income_field.send_keys(user.income)
        # specifies the previous insurance (per default gesetzlich)
        self.previous_insurance_select.select_by_visible_text(user.previous_insurance)
        #if user.occupation == user.OA_OCCUPATION_STUDENT:
        #    self.future_civil_servant_select.select_by_visible_text(user.)
        if user.occupation == user.OA_OCCUPATION_SELF_EMPLOYED:
            self.employee_amount_field.send_keys(5)

    def input_date_of_birth(self, age_in_years: int, difference_in_days: int): #TODO: returns -> Date?
        d = date.today()
        _rd = relativedelta(years=age_in_years) + relativedelta(days=difference_in_days)
        nd = d - _rd

        self.day_field.clear()
        self.day_field.send_keys(nd.day)

        self.month_field.clear()
        self.month_field.send_keys(nd.month)

        self.year_field.clear()
        self.year_field.send_keys(nd.year)


    # def filling_according_to_the_job_types(self):
    #     job_types_UI_Online_Assitant = {self.OA_EMPLOYEE: 'Angestellter',
    #                                     self.OA_SELF_EMPLOYED: 'Selbstständig',
    #                                     self.OA_CIVIL_SERVANT: 'Beamter',
    #                                     self.OA_CIVIL_SERVANT_APPLICANT: 'Beamtenanwärter',
    #                                     self.OA_STUDENT: 'Student oder in Ausbildung'}
    #
    #     for key in job_types_UI_Online_Assitant.keys():
    #         if key == self.OA_EMPLOYEE:
    #             self.input_date_of_birth(age_in_years=30, difference_in_days=0).send_keys()
    #             self.berufstatus_select.select_by_visible_text(self.OA_EMPLOYEE)
    #             self.income_field.send_keys(100000)
    #             self.previous_insurance_select.select_by_visible_text(self.OA_GOVERN)
    #
    #     elif job_types_UI_Online_Assitant.keys(self.OA_SELF_EMPLOYED):
    #         self.input_date_of_birth(age_in_years=30, difference_in_days=0).send_keys()
    #         self.berufstatus_select.select_by_visible_text(self.OA_SELF_EMPLOYED)
    #         self.employee_amount.send_keys(5) # TODO: Check with Bartosz
    #         self.previous_insurance_select.select_by_visible_text(self.OA_GOVERN)
    #
    #     elif job_types_UI_Online_Assitant.keys(self.OA_CIVIL_SERVANT):
    #         self.input_date_of_birth(age_in_years=30, difference_in_days=0).send_keys()
    #         self.berufstatus_select.select_by_visible_text(self.OA_CIVIL_SERVANT)
    #         self.previous_insurance_select.select_by_visible_text(self.OA_GOVERN)
    #
    #     elif job_types_UI_Online_Assitant.keys(self.OA_CIVIL_SERVANT_APPLICANT):
    #         self.input_date_of_birth(age_in_years=30, difference_in_days=0).send_keys()
    #         self.berufstatus_select.select_by_visible_text(self.OA_CIVIL_SERVANT_APPLICANT)
    #         self.previous_insurance_select.select_by_visible_text(self.OA_GOVERN)
    #
    #     elif job_types_UI_Online_Assitant.keys(self.OA_STUDENT):
    #         self.input_date_of_birth(age_in_years=30, difference_in_days=0).send_keys()
    #         self.berufstatus_select.select_by_visible_text(self.OA_STUDENT)
    #         self.future_civil_servant_select.select_by_visible_text(self.OA_NEIN)
    #         self.previous_insurance_select.select_by_visible_text(self.OA_GOVERN)

    # Angestellter has following fields: Geburtsdatum, Berufstatus, Einkommen, Versicherungstype
    # Selbständig has following fields: Geburtsdatum, Berufstatus, WIE VIELE MITARBEITER HAST DU?, Versicherungstype
    # Beamter has following fields: Geburtsdatum, Berufstatus, Versicherungstype
    # Beamtenanwärter has following fields: Geburtsdatum, Berufstatus, Versicherungstype
    # Student oder in Ausbildung has following fields: Geburtsdatum, Berufstatus, Zukünftiger Beamter, Versicherungstype

    #def save_input_data(self,):
        #occupation_options = ['Angestellter', 'Selbstständig', 'Beamter', 'Beamtenanwärter', 'Student oder in Ausbildung']
        #elf.berufstatus_select.select_by_visible_text()
