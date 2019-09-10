from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.OnlineAssistent.Tab1_Start import StartPage
from pages.OnlineAssistent.Tab2_BerufsStatus import BerufsStatusPage
from pages.OnlineAssistent.Tab3_TypeVersich import TypeVersicherung
from pages.OnlineAssistent.Tab4_DataEingabe import Eingabe

from pages.Page import WeiterButtonPage
from dateutil.relativedelta import relativedelta

import datetime



_base_url = "https://test.on.ag/online-assistent"
berufstatus_url = "/berechnen/berufsstatus"
tarifauswahl_url = "/berechnen/tarif-auswahl"
eingabe_url = "/berechnen/krankenversicherung/eingabe"

_path_to_chromedriver = "C:\\Users\\zane.mertes\\PycharmProjects\\chromedriver\\chromedriver.exe"
# 1 Open Online Assistent
chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chromedriver) # open internet
 # open internet


wait = WebDriverWait(chrome_webdriver, 20)

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
page.berufstatus_select.select_by_visible_text("Angestellter")
page.income_input.send_keys("100000")
# AFTER providing data into Beruf - Weiter button MUST be enabled
page.check_weiter_button_is_enabled()

#WeiterButtonPage.weiter_button.click()


wb = chrome_webdriver.find_element_by_xpath('//button[contains(text(), "Weiter")]')
wb.click()

# 5 Click on Vollversicherung tile
wait.until(EC.url_contains(TypeVersicherung.my_url))
page = TypeVersicherung(driver=chrome_webdriver)
page.find_vollversicherung_button.click()

# 6 Fill in the dates

wait.until(EC.url_contains(Eingabe.my_url))
page = Eingabe(driver=chrome_webdriver)

page.check_weiter_button_is_disabled()
page.assert_insurance_start_date()


# print('Future')
# page.input_all_data(age_in_years=99, difference_in_days=0)
print('upper bound too young')
page.input_all_data(age_in_years=16, difference_in_days=-1)
print('lower bound ok')
page.input_all_data(age_in_years=16, difference_in_days=0)
print('mid-ok')
page.input_all_data(age_in_years=20, difference_in_days=0)
print('upper bound ok')
page.input_all_data(age_in_years=99, difference_in_days=0)
# print('lower bound too old')
# page.input_all_data(age_in_years=39, difference_in_days=1)
# print('upper bound too old')
# page.input_all_data(age_in_years=99, difference_in_days=0)
print('WTF?')
page.input_all_data(age_in_years=100, difference_in_days=1)


# TEST SCENARIO FOR BOUNDARY VALUE ANALYSIS
# page.input_all_data(age_in_years=0, difference_in_days=-1,
#                     previous_insurance_type=Eingabe.RANDOM,
#                     insurance_start_date=datetime.date(year=2019, month=5, day=1))
# page.assert_conditions_on_weiter_button()
# page.input_all_data(age_in_years=18, difference_in_days=-1,
#                     previous_insurance_type=Eingabe.RANDOM,
#                     insurance_start_date=datetime.date(year=2019, month=5, day=1))
# page.assert_conditions_on_weiter_button()
# page.input_all_data(age_in_years=18, difference_in_days=0,
#                     previous_insurance_type=Eingabe.RANDOM,
#                     insurance_start_date=datetime.date(year=2019, month=5, day=1))
# page.assert_conditions_on_weiter_button()
# page.input_all_data(age_in_years=20, difference_in_days=0,
#                     previous_insurance_type=Eingabe.RANDOM,
#                     insurance_start_date=datetime.date(year=2019, month=5, day=1))
# page.assert_conditions_on_weiter_button()
# page.input_all_data(age_in_years=38, difference_in_days=-1,
#                     previous_insurance_type=Eingabe.RANDOM,
#                     insurance_start_date=datetime.date(year=2019, month=5, day=1))
# page.assert_conditions_on_weiter_button()
# page.input_all_data(age_in_years=38, difference_in_days=0,
#                     previous_insurance_type=Eingabe.RANDOM,
#                     insurance_start_date=datetime.date(year=2019, month=5, day=1))
# page.assert_conditions_on_weiter_button()
# page.input_all_data(age_in_years=99, difference_in_days=0,
#                     previous_insurance_type=Eingabe.RANDOM,
#                     insurance_start_date=datetime.date(year=2019, month=5, day=1))
# page.assert_conditions_on_weiter_button()
# page.input_all_data(age_in_years=100, difference_in_days=1,
#                     previous_insurance_type=Eingabe.RANDOM,
#                     insurance_start_date=datetime.date(year=2019, month=5, day=1))
# page.assert_conditions_on_weiter_button()

chrome_webdriver.close()

#TODO https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000055470-Missing-Create-Pull-Request-in-VCS-Git-
#TODO https://www.google.com/search?q=pull+request+pycharm&rlz=1C1GGRV_enDE765DE765&oq=pull+request+pycharm&aqs=chrome..69i57j69i61j0l2.7143j0j8&sourceid=chrome&ie=UTF-8
#TODO https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=breaks
#TODO https://de.wikipedia.org/wiki/HTTP-Statuscode
#TODO https://de.wikipedia.org/wiki/Hyper_Text_Coffee_Pot_Control_Protocol