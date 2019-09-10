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
user_of_choice = Users.user_student
#value_of_choice = ValuePage.GRUNDVERSICHERUNG
#value_of_choice = ValuePage.PREIS
value_of_choice = ValuePage.PREIS
nr_kids = 0
# if user_of_choice == Users.user_self_employed_46yo or Users.user_rich_employee_46yo:
#     nr_kids = 0
# elif user_of_choice == Users.user_self_employed_45yo or Users.user_rich_employee_45yo:
#     nr_kids = 1
# elif user_of_choice == Users.user_self_employed_40yo or Users.user_rich_employee_40yo:
#     nr_kids = 2
# elif user_of_choice == Users.user_self_employed_35yo or Users.user_rich_employee_35yo:
#     nr_kids = 3

def prefill_according_to_user(user: user_of_choice, value: value_of_choice):
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

    if nr_kids >= 1:
        page.input_data_kid_by_form(kid_form_number=0)
    if nr_kids >= 2:
        page.input_data_kid_by_form(kid_form_number=1)
    if nr_kids >= 3:
        page.input_data_kid_by_form(kid_form_number=2)
    if nr_kids == 0:
        print("No kids!")

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
    #description_OA = page.find_offer_description.good_text
    #first_class_OA = page.find_first_class_description.good_text
    #klinik_einbett_OA = page.find_klinik_einbett_description.good_text
    #print("OA klinik einbett: " + klinik_einbett_OA)
    #page.asserting_if_OA_equals_Email()

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

    # print(first_matching_email)

    url_regex = '=\s\s\s(.*\s.*\s.*\s.*\s.*\s.*\s.*\s.*)'
    results_description_email = re.findall(url_regex, first_matching_email)
    description_email = results_description_email[0]
    print("Email description: " + description_email)
    #print("OA description: " + description_OA)
    url_regex_first = '\.\s{19,}(.*)\n'
    results_first_email = re.findall(url_regex_first, first_matching_email)
    first_email = results_first_email[0]
    print("Email first: " + first_email)
    #print("OA first: " + first_class_OA)
    url_regex_second = 'ZUSATZVERSICHERUNG\s*(.*)'
    results_second_email = re.findall(url_regex_second, first_matching_email)
    #second_email = results_second_email[0]
    #print("Email second: " + second_email)
    #print("OA second: " + klinik_einbett_OA)
    #assert description_email == description_OA
    #assert first_email == first_class_OA
    #assert second_email == klinik_einbett_OA




    # beratung_link = results_description_email[0]
    # cluttered_link = first_matching_email[first_matching_email.find("Beratungstermin vereinbaren"):
    #                                       first_matching_email.find("Top Bewertung")]
    # clean_link = cluttered_link[cluttered_link.find("<")+1: cluttered_link.find(">")]
    # print(beratung_link)
    #chrome_webdriver.get(beratung_link)
    #page = BeratungPage(driver=chrome_webdriver)
    #page.asserting_if_correctly_prefilled(user=user)

    # print(RecomendationPage.name_field.text)
    # print("User " user_of_choice.name)
    #chrome_webdriver.close()

    #print("Test finished\n\n\n")
#for user in Users.USER_RECOMENDATION:
prefill_according_to_user(user=user_of_choice, value=value_of_choice)
from API.SalesForce.APISalesForce import info_according_to_the_email
email = user_of_choice.email
print(info_according_to_the_email(email=email))
#     for value in ValuePage.VALUES:
#         print("Testing user")
#         user.print_yer_guts()
#         prefill_according_user_preis(user=user, value=value)


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

# for _occupation in Users.OnlineAssistanceUsers.OA_ALLOWED_OCCUPATIONS:
#     _user = Users.generate_user_by_occupation(occupation=_occupation)
#     for _value in ValuePage.BUTTONS:
#         print("testing user choosing {0}".format(_value))
#         _user.print_yer_guts()
#         prefill_according_to_user(user=_user, value=_value)

# for user in Users.USERS_GRUND:
# #     print("testing user choosing grund")
# #     user.print_yer_guts()
# #     prefill_according_user_grund(user=user)
