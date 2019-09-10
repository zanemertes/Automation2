from pages.Page import Page
from elements.Locator import Locator
from elements.mywebelement import MyWebElement
from elements.myselect import MySelect as Select
from API.SalesForce.APISalesForce import info_according_to_the_name
from API.SalesForce.APISalesForce import get_expat_appointments_via_api
from copy import deepcopy
from datetime import datetime
from datetime import date
from time import sleep
import re

class Callback(Page):
    expected_url = ""
    A_MAIN = 'main'
    application = A_MAIN
    my_url = "https://test.on.ag"

    _CALLBACK_NAME = 'callback name'
    _CALLBACK_PHONE = 'callback phone'
    _RUCKRUF_ANFORDERN = 'ruckruf anfordern'
    _CALLBACK_DATE = 'callback date'
    _CALLBACK_TIME = 'callback time'
    _TERMIN_VEREINBAREN = 'termin vereinbaren'
    _FINAL_DATE = 'final date'
    _FINAL_TIME = 'final time'

    #locators = deepcopy(Page.locators)

    locators= {_CALLBACK_NAME:
                    Locator('.//div/input[@name="name"]'),
                     _CALLBACK_PHONE:
                    Locator('.//li/form/div/input[@name="phoneNumber"]'),
                     _RUCKRUF_ANFORDERN:
                    Locator('.//div/button[contains(text(), "Rückruf anfordern")]'),
                     _CALLBACK_DATE:
                    Locator('.//form/div/div/select[contains(@class,"dateSelect")]'),
                     _CALLBACK_TIME:
                    Locator('.//form/div/div/select[contains(@class,"timeSelect")]'),
                     _TERMIN_VEREINBAREN:
                    Locator('.//button[@label="appointment-booked"]'),
                     _FINAL_DATE:
                    Locator('.//span/strong[@class="fillDate"]'),
                     _FINAL_TIME:
                    Locator('.//span/strong[@class="fillTime"]')
                     }

    def __init__(self, driver):
        super().__init__(driver)
        self.CBname = self.call_back_name_random

    # def __init__(self, setup: Setup, open_page: bool):
    #    super().__init__(setup=setup, open_page=open_page)
    #    self.CBname = self.call_back_name_random

    @property
    def find_callback_name_field(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._CALLBACK_NAME]))

    @property
    def find_callback_phone_field(self) -> MyWebElement:
        return self.body.find_mwe(by=self.locators[self._CALLBACK_PHONE])

    @property
    def find_callback_ruckruf_anfordern(self) -> MyWebElement:
        return self.body.find_mwe(by=self.locators[self._RUCKRUF_ANFORDERN])

    @property
    def find_termin_vereinbaren(self) -> MyWebElement:
        return self.body.find_mwe(by=self.locators[self._TERMIN_VEREINBAREN])

    @property
    def find_final_date(self) -> MyWebElement:
        return self.body.find_mwe(by=self.locators[self._FINAL_DATE])

    @property
    def find_final_time(self) -> MyWebElement:
        return self.body.find_mwe(by=self.locators[self._FINAL_TIME])

    @property
    def select_callback_date(self) -> Select:
        return Select(_we=self.body.find_mwe(by=self.locators[self._CALLBACK_DATE]))

    @property
    def select_callback_time(self) -> Select:
        return Select(_we=self.body.find_mwe(by=self.locators[self._CALLBACK_TIME]))

    @property
    def call_back_name_random(self):
        return "ZM{0}".format(str(int(datetime.timestamp(datetime.now()))))

    def callback_input(self,
                       CBphone: str = "0123456789"):
        self.find_callback_name_field.send_keys(self.CBname)
        self.find_callback_phone_field.send_keys(CBphone)
        self.find_callback_ruckruf_anfordern.click()

        self.body.wait_until_element_found_is_present(by=self.locators[self._CALLBACK_DATE])
                        # presence_of_element_located(locator))
        self.select_callback_date.select_by_index(1)
        # self.select_callback_date.select_item_from_list(number=1)
        self.select_callback_time.select_by_index(1)
        # self.select_callback_time.select_item_from_list(number=1)
        # self.select_callback_date.select_by_index(1)
        # self.select_callback_time.select_by_index(1)
        self.find_termin_vereinbaren.click()#scroll_until_clickable_and_click()

    def read_info_ui(self):
        sleep(2)
        self.body.wait_until_element_found_is_present(by=self.locators[self._FINAL_DATE])
        self.body.wait_until_text_present_in_text(text_1="dem",
                                                  text_2=self.find_final_date.good_text,
                                                  timeout=2.0)
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
        print(UI_date_dt)

        # cest = pytz.timezone("Europe/Berlin")
        # UI_date_dt_tz = cest.localize(UI_date_dt, is_dst=None)
        # UI_date_dt_tz = UI_date_dt.astimezone(cest)
        return UI_date_dt

    def comparison_ui_and_salesforce(self):
        SFname, SFphone, SFappointment_str = info_according_to_the_name(name=self.CBname)
        print("SalesForce str: {SF}.".format(SF=SFappointment_str))
        SFappointment_dt_long = datetime.strptime(SFappointment_str, "%Y-%m-%dT%H:%M:%S.%f%z")
        SFappointment_dt = datetime(SFappointment_dt_long.year,
                                    SFappointment_dt_long.month,
                                    SFappointment_dt_long.day,
                                    SFappointment_dt_long.hour,
                                    SFappointment_dt_long.minute)

        # cest = pytz.timezone("Europe/Berlin")
        sleep(3)
        # SFappointment = cest.localize(SFappointment_dt, is_dst=None)
        # SFappointment = SFappointment_dt.astimezone(cest)

        UI_date_dt_tz = self.read_info_ui()
        print("SalesForce provided appointment time: {SF}.".format(SF=SFappointment_dt))
        print("User selected appointment time: {UI}.".format(UI=UI_date_dt_tz))
        assert SFappointment_dt == UI_date_dt_tz
        print("Correct date and time!")


    def available_appointments_in_calendar(self):
        get_expat_appointments_via_api(days=1)
