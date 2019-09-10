from pages.Page import WeiterButtonPage
from elements.mywebelement import MyWebElement
from elements.myselect import MySelect
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from API.SalesForce.APISalesForce import info_according_to_the_name
from selenium.webdriver.support.select import Select
from copy import deepcopy
from datetime import datetime
from datetime import date
import pytz
import re


class Expats(WeiterButtonPage):
    my_url = "https://test.on.ag/expats"
    _GET_CONSULTATION = "Get a consultation"
    _NAME = 'name'
    _SURNAME = 'surname'
    _EMAIL = 'email'
    _PHONE = 'phone number'
    _BIRTHDAY = 'birthday'
    _NATIONALITY = 'nationality'
    _APPOINTENT_DATE = 'appointment date'
    _APPOINTENT_TIME = 'appointment time'
    _SUBMIT = 'submit'
    _OK = "OK"

    locators = deepcopy(WeiterButtonPage.locators)
    locators.update({_GET_CONSULTATION:
                    './/section[@id="hero"]//a[contains(text(), "Get a consultation")]',
                     _NAME:
                    './/div[contains(.,"First Name*")]/input[@name="firstName"]',
                     _SURNAME:
                    './/div/input[@name="lastName"]',
                     _EMAIL:
                    './/div/input[@name="email"]',
                     _PHONE:
                    './/div/input[@name="phoneNumber"]',
                     _BIRTHDAY:
                    './/div/input[@name="birthday"]',
                     _NATIONALITY:
                    './/div/input[@name="nationality"]',
                     _APPOINTENT_DATE:
                    './/div[contains(.,"Date")]/div/select[@class="dateSelect empty"]',
                     _APPOINTENT_TIME:
                    './/div[contains(.,"Time")]/div/select[@class="timeSelect empty"]',
                     _SUBMIT:
                    './/form/button[contains(text(), "Submit")]',
                     _OK:
                    './/button[contains(text(), "Ok")]',
                     })

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def find_consultation_buttton(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._GET_CONSULTATION]))

    @property
    def find_name_field(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._NAME]))

    @property
    def find_surname_field(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._SURNAME]))

    @property
    def find_email_field(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._EMAIL]))

    @property
    def find_phone_field(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._PHONE]))

    @property
    def find_birthday_field(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._BIRTHDAY]))

    @property
    def find_nationality_field(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._NATIONALITY]))

    @property
    def select_appointment_date(self)-> MySelect:
        return MySelect(_we=self.body.find_element_by_xpath(self.locators[self._APPOINTENT_DATE]))

    @property
    def select_appointment_time(self)-> MySelect:
        return MySelect(_we=self.body.find_element_by_xpath(self.locators[self._APPOINTENT_TIME]))
    @property
    def find_submit_button(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._SUBMIT]))
    @property
    def find_ok_button(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._OK]))



    def input_user_info(self, name: str = "Zane",
                        surname: str ="Mertes",
                        email: str = "zmertes+ExpatConsultation-23052019@on-testing.de",
                        phone: str = "0123456789",
                        birthday: str = "13.07.1989",
                        nationality: str = "German"):
        self.find_name_field.send_keys(name)
        self.find_surname_field.send_keys(surname)
        self.find_email_field.send_keys(email)
        self.find_phone_field.send_keys(phone)
        self.find_birthday_field.send_keys(birthday)
        self.find_nationality_field.send_keys(nationality)

    def select_appointment(self):
        self.select_appointment_date.select_by_index(1)
        #date = self.select_appointment_date.good_text
        #print(date)
        self.select_appointment_time.select_by_index(1)
        #time = self.select_appointment_time.good_text
        #print(time)

#curl 'https://services-test.on.ag/appointment/appointments/public?days=5&calendar=expat-idd-consultation' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://test.on.ag/expats' -H 'Origin: https://test.on.ag' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' --compressed

class Callback(WeiterButtonPage):
    my_url = "https://test.on.ag"
    _CALLBACK_NAME = 'callback name'
    _CALLBACK_PHONE = 'callback phone'
    _RUCKRUF_ANFORDERN = 'ruckruf anfordern'
    _CALLBACK_DATE = 'callback date'
    _CALLBACK_TIME = 'callback time'
    _TERMIN_VEREINBAREN = 'termin vereinbaren'
    _FINAL_DATE = 'final date'
    _FINAL_TIME = 'final time'

    locators = deepcopy(WeiterButtonPage.locators)
    locators.update({_CALLBACK_NAME:
                    './/div/input[@name="name"]',
                     _CALLBACK_PHONE:
                    './/li/form/div/input[@name="phoneNumber"]',
                     _RUCKRUF_ANFORDERN:
                    './/div/button[contains(text(), "Rückruf anfordern")]',
                     _CALLBACK_DATE:
                    './/form/div/div/select[@class="dateSelect empty"]',
                     _CALLBACK_TIME:
                    './/form/div/div/select[@class="timeSelect empty"]',
                     _TERMIN_VEREINBAREN:
                    './/button[@label="appointment-booked"]',
                     _FINAL_DATE:
                    './/span/strong[@class="fillDate"]',
                     _FINAL_TIME:
                    './/span/strong[@class="fillTime"]'
                     })

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def find_callback_name_field(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._CALLBACK_NAME]))

    @property
    def find_callback_phone_field(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._CALLBACK_PHONE]))

    @property
    def find_callback_ruckruf_anfordern(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._RUCKRUF_ANFORDERN]))

    @property
    def find_termin_vereinbaren(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._TERMIN_VEREINBAREN]))

    @property
    def find_final_date(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._FINAL_DATE]))

    @property
    def find_final_time(self)-> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._FINAL_TIME]))

    @property
    def select_callback_date(self) -> MySelect:
        return MySelect(_we=self.body.find_element_by_xpath(self.locators[self._CALLBACK_DATE]))

    @property
    def select_callback_time(self) -> MySelect:
        return MySelect(_we=self.body.find_element_by_xpath(self.locators[self._CALLBACK_TIME]))

    def call_back_name_random():
        CBname = "ZM{0}".format(str(int(datetime.timestamp(datetime.now()))))
        return CBname

    CBname = call_back_name_random()

    def callback_input(self,
                       CBphone: str = "0123456789"):
        self.find_callback_name_field.send_keys(self.CBname)
        self.find_callback_phone_field.send_keys(CBphone)
        self.find_callback_ruckruf_anfordern.click()
        locator = (By.XPATH, self.locators[self._CALLBACK_DATE])
        self.wait.until(EC.visibility_of_element_located(locator))
                        # presence_of_element_located(locator))
        self.select_callback_date.select_by_index(1)
        self.select_callback_time.select_by_index(1)
        self.find_termin_vereinbaren.click()

    def read_info_ui(self):
        locator = (By.XPATH, self.locators[self._FINAL_DATE])
        self.wait.until(EC.visibility_of_element_located(locator))

        final_time = self.find_final_time.good_text
        final_date = self.find_final_date.good_text
        UI_full_str = "{date} {time}". format(date=final_date, time=final_time)
        print(UI_full_str)
        regex = 'dem (.*) Uhr'
        UI_reg_str = re.findall(regex, UI_full_str)
        UI_reg_str_first = UI_reg_str[0]
        year = str(date.today().year)

        UI_full_str_with_year = "{year}.{str}".format(year=year, str=UI_reg_str_first)
        UI_date_dt = datetime.strptime(UI_full_str_with_year, "%Y.%d.%m. %H:%M")
        cest = pytz.timezone("Europe/Berlin")
        UI_date_dt_tz = UI_date_dt.astimezone(cest)
        return UI_date_dt_tz

    def comparison_ui_and_salesforce(self):
        SFname, SFphone, SFappointment_str  = info_according_to_the_name(name=self.CBname)
        SFappointment_dt = datetime.strptime(SFappointment_str, "%Y-%m-%dT%H:%M:%S.%f%z")
        cest = pytz.timezone("Europe/Berlin")
        SFappointment = SFappointment_dt.astimezone(cest)
        UI_date_dt_tz = self.read_info_ui()
        print("SalesForce provided appointment time: {SF}.".format(SF=SFappointment))
        print("User selected appointment time: {UI}.".format(UI=UI_date_dt_tz))
        assert SFappointment == UI_date_dt_tz
        print("Correct date and time!")
