from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime


def check_disabled():
    weiter_button = chrome.find_element_by_xpath(xpath=weiter_button_locator)
    assert not weiter_button.is_enabled()
    print("Weiter button disabled!")


def check_enabled():
    weiter_button = chrome.find_element_by_xpath(xpath=weiter_button_locator)
    assert weiter_button.is_enabled()
    print("Weiter button enabled!")

#def Weiter


# 1 Opened Online Assistent

chrome = webdriver.Chrome(executable_path="C:\\Users\\zane.mertes\\PycharmProjects\\chromedriver\\chromedriver.exe") #open internet
website = "https://test.on.ag/online-assistent/start"
chrome.get(website)

# 2 Click on Beitrag Berechnen tile
berufstatus_url = "/berechnen/berufsstatus"
tarifauswahl_url = "/berechnen/tarif-auswahl"
eingabe_url = "/berechnen/krankenversicherung/eingabe"

mein_beitrag_locator = "//oa-tile[contains(@ng-reflect-navigate-to,'" + berufstatus_url + "')]"
mein_beitrag = chrome.find_element_by_xpath(xpath=mein_beitrag_locator)

mein_beitrag.click()

wait = WebDriverWait(chrome, 10)
wait.until(EC.url_contains(berufstatus_url))
new_url = chrome.current_url

assert berufstatus_url in new_url
print("Correct URL!")
# Switched page to Berufsstatus

# 4 Select Student oder in Ausbildung

beruf_locator = "//select"
weiter_button_locator = '//button[contains(text(), "Weiter")]'

weiter_button = chrome.find_element_by_xpath(xpath=weiter_button_locator)
# BEFORE providing data into Beruf - Weiter button MUST NOT be enabled

check_disabled()

beruf = Select(webelement=chrome.find_element_by_xpath(xpath=beruf_locator))
beruf.select_by_visible_text("Student oder in Ausbildung")
# AFTER providing data into Beruf - Weiter button MUST be enabled

check_enabled()

weiter_button.click()

# 5 Click on Vollversicherung tile
wait.until(EC.url_contains(tarifauswahl_url))
# vollversicherung_locator = '//ngc-product-card/div[@class="card mx-0 mx-sm-2"]'
vollversicherung_locator = "//ngc-product-card/div"
# wait.until(EC.presence_of_element_located(locator=vollversicherung_locator))
vollversicherung_button = chrome.find_element_by_xpath(xpath=vollversicherung_locator)

vollversicherung_button.click()

# 6 Fill in the date OLD STUDENT

# Day

wait.until(EC.url_contains(eingabe_url))

weiter_button_locator = '//button[contains(text(), "Weiter")]'
weiter_button = chrome.find_element_by_xpath(xpath=weiter_button_locator)

day_locator = '//div/input[@formcontrolname="day"]'
month_locator = '//div/input[@formcontrolname="month"]'
year_locator = '//div/input[@formcontrolname="year"]'

day_field = chrome.find_element_by_xpath(xpath=day_locator)
month_field = chrome.find_element_by_xpath(xpath=month_locator)
year_field = chrome.find_element_by_xpath(xpath=year_locator)

delta = 38
adjustment = 1
days = 365.25
deltadays = (delta * days) + adjustment
tday = datetime.date.today()
tdelta = datetime.timedelta(days=deltadays)

finaldate =tday-tdelta
print(finaldate)

day_field.send_keys(finaldate.day)
month_field.send_keys(finaldate.month)
# Year 0019 - waaaay over a 100 years => we expect a validation error message and Weiter button to REMAIN disabled
year_field.send_keys(finaldate.year)


validation_locator = '//div[@class="validation-message-text text-danger ng-star-inserted"]'

wait.until(EC.visibility_of_element_located(locator=(By.XPATH, validation_locator)))

# as an example how the 'find_element' method works, what kind of locator data it expects
validation = chrome.find_element(by=By.XPATH, value=validation_locator)


assert validation.text == "Du kannst dich nur bis 38 bei uns als ein Student versichern"
print("Validation exists!")

check_disabled()

# Previous insurance tile

previous_insurance_locator = '//div/select[@formcontrolname="previous_insurance"]'
previous_insurance = Select(webelement=chrome.find_element_by_xpath(xpath=previous_insurance_locator))
previous_insurance.select_by_visible_text("Privat")

versicherungsbeginn_locator = '//div/select[@formcontrolname="ingress_date"]'
versicherungsbeginn = chrome.find_element_by_xpath(xpath=versicherungsbeginn_locator)
versicherungsbeginn.send_keys('01.03.2019')

# We expect the button to be disabled
check_disabled()

# What will happen when clicking on a disabled button?
weiter_button.click()

# find weiter
# click on it
# check if disabled

# === Click on Weiter
# === Click on Vollversicherung
# === Enter an Age in the future
# === Find validation message
# === Find Weiter
# === Check if Weiter stays disabled
# === Select any value


# === Enter an Age in the future
# === Find validation message
# === Find Weiter
# === Check if Weiter stays disabled


chrome.close()