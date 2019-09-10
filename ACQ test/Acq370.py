from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.OnlineAssistent.Tab1_Start import StartPage
from pages.OnlineAssistent.Tab2_BerufsStatus import BerufsStatusPage
from pages.OnlineAssistent.Tab3_TypeVersich import TypeVersicherung
from pages.OnlineAssistent.Tab4_DataEingabe import Eingabe
from DataObjects import Users

import datetime

_base_url = "https://test.on.ag/online-assistent"
berufstatus_url = "/berechnen/berufsstatus"
tarifauswahl_url = "/berechnen/tarif-auswahl"
eingabe_url = "/berechnen/krankenversicherung/eingabe"
_path_to_chromedriver = "/usr/bin/chromedriver"

# 1 Open Online Assistent
chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chromedriver) # open internet
wait = WebDriverWait(chrome_webdriver, 10)

website = _base_url + StartPage.my_url
chrome_webdriver.get(website)

page = StartPage(driver=chrome_webdriver)

# 2 Click on Beitrag Berechnen tile
page.find_beitrag_berechnen_button.click()
wait.until(EC.url_contains(BerufsStatusPage.my_url))

# 3. Switch page to Berufsstatus
page = BerufsStatusPage(driver=chrome_webdriver)
# 4 Select Student oder in Ausbildung
# BEFORE providing data into Beruf - Weiter button MUST NOT be enabled
page.check_weiter_button_is_disabled()
page.berufstatus_select.select_by_visible_text(Users.OnlineAssistanceUsers.OA_OCCUPATION_STUDENT)
# AFTER providing data into Beruf - Weiter button MUST be enabled
page.check_weiter_button_is_enabled()
page.weiter_button.click()

# 5 Click on Vollversicherung tile
wait.until(EC.url_contains(TypeVersicherung.my_url))
page = TypeVersicherung(driver=chrome_webdriver)
page.find_vollversicherung_button.click()


# TODO:
# 6 Fill in the date OLD STUDENT

# Day

wait.until(EC.url_contains(Eingabe.my_url))
page = Eingabe(driver=chrome_webdriver)

page.check_weiter_button_is_disabled()


# TEST SCENARIO FOR BOUNDARY VALUE ANALYSIS
page.input_all_data(age_in_years=0, difference_in_days=-1,
                    previous_insurance_type=Eingabe.RANDOM,
                    insurance_start_date=datetime.date(year=2019, month=5, day=1))
page.input_all_data(age_in_years=18, difference_in_days=-1,
                    previous_insurance_type=Eingabe.RANDOM,
                    insurance_start_date=datetime.date(year=2019, month=5, day=1))
page.input_all_data(age_in_years=18, difference_in_days=0,
                    previous_insurance_type=Eingabe.RANDOM,
                    insurance_start_date=datetime.date(year=2019, month=5, day=1))
page.input_date_of_birth_and_assert_validations(age_in_years=20, difference_in_days=0)
page.input_date_of_birth_and_assert_validations(age_in_years=38, difference_in_days=-1)
page.input_date_of_birth_and_assert_validations(age_in_years=38, difference_in_days=0)
page.input_date_of_birth_and_assert_validations(age_in_years=99, difference_in_days=-1)
page.input_date_of_birth_and_assert_validations(age_in_years=99, difference_in_days=0)
page.input_date_of_birth_and_assert_validations(age_in_years=100, difference_in_days=1)

chrome_webdriver.close()
