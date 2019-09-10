from pages.OnlineAssistent.Tariff import TariffPage
from pages.OnlineAssistent.Tab5_Result import ResultPage
from pages.OnlineAssistent.Recomendation import RecomendationPage
from pages.OnlineAssistent.Beratung import BeratungPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.OnlineAssistent.Tab1_Start import StartPage
from API.IMAP.API import get_emails
from datetime import date
from os import environ
from selenium.webdriver.support import expected_conditions as EC
from DataObjects import Users
from pages.OnlineAssistent.Rec_Value import ValuePage
import re

_base_url = "https://test.on.ag/online-assistent"
berufstatus_url = "/berechnen/berufsstatus"
tarifauswahl_url = "/berechnen/tarif-auswahl"
eingabe_url = "/berechnen/krankenversicherung/eingabe"
_path_to_chromedriver = "/usr/bin/chromedriver"


def prefill_according_to_user(user: Users.OnlineAssistanceUsers, value: ValuePage.BUTTONS):
    # user_of_choice = Users.user_poor_employee
    # 1 Open Online Assistent
    chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chromedriver)  # open internet
    # open internet

    wait = WebDriverWait(chrome_webdriver, 20)

    website = _base_url + StartPage.my_url
    chrome_webdriver.get(website)

    page = StartPage(driver=chrome_webdriver)
    page.find_tariff_button.click()
    wait.until(EC.url_contains(TariffPage.my_url))
    page = TariffPage(driver=chrome_webdriver)

    page.check_weiter_button_is_disabled()

    # filling_according_to_the_job_types()
    page.input_data_from_user(user=user)

    page.check_weiter_button_is_enabled()
    page.click_weiter_button()
    wait.until(EC.url_contains(ValuePage.my_url))

    page = ValuePage(driver=chrome_webdriver, user=user)
    try:
        page.click_a_value(button_locator_name=value)
    except ValueError:
        chrome_webdriver.close()
        print("Test finished\n\n\n")
        return

    wait.until(EC.url_contains(ResultPage.my_url))
    page = ResultPage(driver=chrome_webdriver)

    page.find_recomendation_button.click()
    page = RecomendationPage(driver=chrome_webdriver)
    page.input_data_from_user_for_recommendation(user=user)
    page.find_send_button.click()

    print(environ['TEST_USER'])

    # emails = get_emails(recipient="zmertes@on-testing.de",
    #                     subject="Das ist der passende Tarif für dich.",
    #                     date_from=date(year=2019, month=4, day=5))
    emails = get_emails(recipient=user.email,
                        subject="Bitte bestätige deine E-Mail-Adresse.",
                        date_from=date(year=2019, month=4, day=1))

    first_matching_email = emails[0]

    #print(first_matching_email)


    #TODO: Use REGEX!!!!!!!!!!
    cluttered_link = first_matching_email[first_matching_email.find("E-Mail-Adresse bestätigen"):
                                          first_matching_email.find("Um eine persönliche Tarifempfehlung und regelmäßig nicht")]
    bitte_bestaetigen_link = cluttered_link[cluttered_link.find("<")+1: cluttered_link.find(">")]
    chrome_webdriver.get(bitte_bestaetigen_link)

    emails = get_emails(recipient=user.email,
                        subject="Das ist der passende Tarif für dich.",
                        date_from=date(year=2019, month=4, day=1))

    first_matching_email = emails[0]

    #print(first_matching_email)

    url_regex = '<(.*test.on.ag.*)>'
    results = re.findall(url_regex, first_matching_email)
    beratung_link = results[0]
    # cluttered_link = first_matching_email[first_matching_email.find("Beratungstermin vereinbaren"):
    #                                       first_matching_email.find("Top Bewertung")]
    # clean_link = cluttered_link[cluttered_link.find("<")+1: cluttered_link.find(">")]
    # print(beratung_link)
    chrome_webdriver.get(beratung_link)
    page = BeratungPage(driver=chrome_webdriver)
    page.asserting_if_correctly_prefilled(user=user)

    # print(RecomendationPage.name_field.text)
    # print("User " user_of_choice.name)
    chrome_webdriver.close()

    print("Test finished\n\n\n")


# def prefill_according_user_beste(user: Users.OnlineAssistanceUsers):
#     # user_of_choice = Users.user_poor_employee
#     # 1 Open Online Assistent
#     chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chromedriver)  # open internet
#     # open internet
#
#     wait = WebDriverWait(chrome_webdriver, 20)
#
#     website = _base_url + StartPage.my_url
#     chrome_webdriver.get(website)
#
#     page = StartPage(driver=chrome_webdriver)
#     page.find_tariff_button.click()
#     wait.until(EC.url_contains(TariffPage.my_url))
#     page = TariffPage(driver=chrome_webdriver)
#
#     page.check_weiter_button_is_disabled()
#
#     # filling_according_to_the_job_types()
#     page.input_data_from_user(user=user)
#
#     page.check_weiter_button_is_enabled()
#     page.click_weiter_button()
#     wait.until(EC.url_contains(ValuePage.my_url))
#
#     page = ValuePage(driver=chrome_webdriver)
#     page.click_a_value(value=value)
#
#     page.wert_beste
#     #page.find_beste_absicherung_button.click()
#     #wait.until(EC.url_contains(RecomendationPage.my_url))
#
#     wait.until(EC.url_contains(ResultPage.my_url))
#     page = ResultPage(driver=chrome_webdriver)
#
#     page.find_recomendation_button.click()
#     page = RecomendationPage(driver=chrome_webdriver)
#     page.input_data_from_user_for_recommendation(user=user)
#     page.find_send_button.click()
#
#     print(environ['TEST_USER']) # TODO: UNDERSTAND :D
#
#     # emails = get_emails(recipient="zmertes@on-testing.de",
#     #                     subject="Das ist der passende Tarif für dich.",
#     #                     date_from=date(year=2019, month=4, day=5))
#     emails = get_emails(recipient=user.email,
#                         subject="Bitte bestätige deine E-Mail-Adresse.",
#                         date_from=date(year=2019, month=4, day=1))
#
#     first_matching_email = emails[0]
#     # print(first_matching_email)
#     #TODO: Use REGEX!!!!!!!!!!
#     cluttered_link = first_matching_email[first_matching_email.find("E-Mail-Adresse bestätigen"):
#                                           first_matching_email.find("Um eine persönliche Tarifempfehlung und regelmäßig nicht")]
#     bitte_bestaetigen_link = cluttered_link[cluttered_link.find("<")+1: cluttered_link.find(">")]
#     chrome_webdriver.get(bitte_bestaetigen_link)
#
#     emails = get_emails(recipient=user.email,
#                         subject="Das ist der passende Tarif für dich.",
#                         date_from=date(year=2019, month=4, day=1))
#
#     first_matching_email = emails[0]
#     # print(first_matching_email)
#     url_regex ='<(.*test.on.ag.*)>'
#     results = re.findall(url_regex, first_matching_email)
#     beratung_link = results[0]
#     # cluttered_link = first_matching_email[first_matching_email.find("Beratungstermin vereinbaren"):
#     #                                       first_matching_email.find("Top Bewertung")]
#     # clean_link = cluttered_link[cluttered_link.find("<")+1: cluttered_link.find(">")]
#     # print(beratung_link)
#     chrome_webdriver.get(beratung_link)
#     page = BeratungPage(driver=chrome_webdriver)
#     page.asserting_if_correctly_prefilled(user=user)
#
#     # print(RecomendationPage.name_field.text)
#     # print("User " user_of_choice.name)
#     chrome_webdriver.close()
#
#
# def prefill_according_user_grund(user: Users.OnlineAssistanceUsers):
#     # user_of_choice = Users.user_poor_employee
#     # 1 Open Online Assistent
#     chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chromedriver)  # open internet
#     # open internet
#
#     wait = WebDriverWait(chrome_webdriver, 20)
#
#     website = _base_url + StartPage.my_url
#     chrome_webdriver.get(website)
#
#     page = StartPage(driver=chrome_webdriver)
#     page.find_tariff_button.click()
#     wait.until(EC.url_contains(TariffPage.my_url))
#     page = TariffPage(driver=chrome_webdriver)
#
#     page.check_weiter_button_is_disabled()
#
#     # filling_according_to_the_job_types()
#     page.input_data_from_user(user=user)
#
#     page.check_weiter_button_is_enabled()
#     page.click_weiter_button()
#     wait.until(EC.url_contains(ValuePage.my_url))
#
#     page = ValuePage(driver=chrome_webdriver)
# #    page.choosing_a_value(value=value)
#
#     page.wert_grund
#     #page.find_beste_absicherung_button.click()
#     #wait.until(EC.url_contains(RecomendationPage.my_url))
#
#     wait.until(EC.url_contains(ResultPage.my_url))
#     page = ResultPage(driver=chrome_webdriver)
#
#     page.find_recomendation_button.click()
#     page = RecomendationPage(driver=chrome_webdriver)
#     page.input_data_from_user_for_recommendation(user=user)
#     page.find_send_button.click()
#
#     print(environ['TEST_USER']) # TODO: UNDERSTAND :D
#
#     # emails = get_emails(recipient="zmertes@on-testing.de",
#     #                     subject="Das ist der passende Tarif für dich.",
#     #                     date_from=date(year=2019, month=4, day=5))
#     emails = get_emails(recipient=user.email,
#                         subject="Bitte bestätige deine E-Mail-Adresse.",
#                         date_from=date(year=2019, month=4, day=1))
#
#     first_matching_email = emails[0]
#     # print(first_matching_email)
#     #TODO: Use REGEX!!!!!!!!!!
#     cluttered_link = first_matching_email[first_matching_email.find("E-Mail-Adresse bestätigen"):
#                                           first_matching_email.find("Um eine persönliche Tarifempfehlung und regelmäßig nicht")]
#     bitte_bestaetigen_link = cluttered_link[cluttered_link.find("<")+1: cluttered_link.find(">")]
#     chrome_webdriver.get(bitte_bestaetigen_link)
#
#     emails = get_emails(recipient=user.email,
#                         subject="Das ist der passende Tarif für dich.",
#                         date_from=date(year=2019, month=4, day=1))
#
#     first_matching_email = emails[0]
#     # print(first_matching_email)
#     url_regex = r'<(.*test.on.ag.*)>'
#     results = re.findall(url_regex, first_matching_email)
#     beratung_link = results[0]
#     # cluttered_link = first_matching_email[first_matching_email.find("Beratungstermin vereinbaren"):
#     #                                       first_matching_email.find("Top Bewertung")]
#     # clean_link = cluttered_link[cluttered_link.find("<")+1: cluttered_link.find(">")]
#     # print(beratung_link)
#     chrome_webdriver.get(beratung_link)
#     page = BeratungPage(driver=chrome_webdriver)
#     page.asserting_if_correctly_prefilled(user=user)
#
#     # print(RecomendationPage.name_field.text)
#     # print("User " user_of_choice.name)
#     chrome_webdriver.close()
#
# for user in Users.USERS_ALL:
#     for value in ValuePage.VALUES:
#         print("Testing user")
#         user.print_yer_guts()
#         prefill_according_user_preis(user=user, value=value)

# for _user in Users.USERS_ALL:
#     for _value in ValuePage.BUTTONS:
#         print("testing user choosing beste")
#         _user.print_yer_guts()
#         prefill_according_to_user(user=_user, value=_value)

for _occupation in Users.OnlineAssistanceUsers.OA_ALLOWED_OCCUPATIONS:
    _user = Users.generate_user_by_occupation(occupation=_occupation)
    for _value in ValuePage.BUTTONS:
        print("testing user choosing {0}".format(_value))
        _user.print_yer_guts()
        prefill_according_to_user(user=_user, value=_value)

# for user in Users.USERS_GRUND:
# #     print("testing user choosing grund")
# #     user.print_yer_guts()
# #     prefill_according_user_grund(user=user)
