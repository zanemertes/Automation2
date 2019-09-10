from pages.OnlineAssistent.Recomendation import RecomendationPage
from API.IMAP.API import get_emails
from datetime import date
from os import environ
from DataObjects import Users
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.OnlineAssistent.Tab1_Start import StartPage
from pages.OnlineAssistent.Tab2_BerufsStatus import BerufsStatusPage
from pages.OnlineAssistent.Tab3_TypeVersich import TypeVersicherung
from pages.OnlineAssistent.Tab4_DataEingabe import Eingabe
from pages.OnlineAssistent.Tab5_Result import ResultPageClinik

_base_url = "https://test.on.ag/online-assistent"
berufstatus_url = "/berechnen/berufsstatus"
tarifauswahl_url = "/berechnen/tarif-auswahl"
eingabe_url = "/berechnen/krankenversicherung/eingabe"
_path_to_chromedriver = "/usr/bin/chromedriver"
user_of_choice = Users.user_poor_employee

chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chromedriver)  # open internet
    # open internet

wait = WebDriverWait(chrome_webdriver, 20)

website = _base_url + StartPage.my_url
chrome_webdriver.get(website)

page = StartPage(driver=chrome_webdriver)

# 2 Click on Beitrag Berechnen tile
page.find_beitrag_berechnen_button.click()

wait.until(EC.url_contains(BerufsStatusPage.my_url))
page = BerufsStatusPage(driver=chrome_webdriver)
# 4 Select Student oder in Ausbildung
# BEFORE providing data into Beruf - Weiter button MUST NOT be enabled
page.check_weiter_button_is_disabled()


page.berufstatus_select.select_by_visible_text(Users.OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE) # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

page.check_weiter_button_is_enabled()
page.weiter_button.click()

# 5 Click on Vollversicherung tile
wait.until(EC.url_contains(TypeVersicherung.my_url))
page = TypeVersicherung(driver=chrome_webdriver)
page.find_clinik_button().click()

wait.until(EC.url_contains(Eingabe.my_url))
page = Eingabe(driver=chrome_webdriver)

page.check_weiter_button_is_disabled()
page.input_birthdate_clinik(user=user_of_choice)
page.check_weiter_button_is_enabled()
page.weiter_button.click()
wait.until(EC.url_contains(ResultPageClinik.my_url))

page = ResultPageClinik(driver=chrome_webdriver)
page.find_angebot_per_email_button.click()
wait.until(EC.url_contains(RecomendationPage.my_url))

page = RecomendationPage(driver=chrome_webdriver)
page.input_data_from_user_for_recommendation(user=user_of_choice)
page.find_send_button.click()

print(environ['TEST_USER'])

# emails = get_emails(recipient="zmertes@on-testing.de",
#                     subject="Das ist der passende Tarif für dich.",
#                     date_from=date(year=2019, month=4, day=5))
emails = get_emails(recipient=user_of_choice.email,
                    subject="Bitte bestätige deine E-Mail-Adresse.",
                    date_from=date(year=2019, month=4, day=1))

first_matching_email = emails[0]
# url_regex = '<(.*test.on.ag.*)>'
# results = re.findall(url_regex, first_matching_email)
# bitte_bestaetigen_link= results[0]
cluttered_link = first_matching_email[first_matching_email.find("E-Mail-Adresse bestätigen"):
                                      first_matching_email.find(
                                          "Um eine persönliche Tarifempfehlung und regelmäßig nicht")]
bitte_bestaetigen_link = cluttered_link[cluttered_link.find("<") + 1: cluttered_link.find(">")]
chrome_webdriver.get(bitte_bestaetigen_link)

emails = get_emails(recipient=user_of_choice.email,
                    subject="Dein unverbindliches Angebot für eine Krankenhauszusatzversicherung",
                    date_from=date(year=2019, month=4, day=1))

first_matching_email = emails[0]


url_regex = '<(.*test.on.ag.*)>'
results = re.findall(url_regex, first_matching_email)
beantragen_link = results[0]
chrome_webdriver.get(beantragen_link)