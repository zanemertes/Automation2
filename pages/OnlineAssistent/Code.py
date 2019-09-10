from pages.OnlineAssistent.Callback import Callback
from selenium import webdriver
from time import sleep

_base_url = "https://test.on.ag/expats"
#berufstatus_url = "/berechnen/berufsstatus"
#tarifauswahl_url = "/berechnen/tarif-auswahl"
#eingabe_url = "/berechnen/krankenversicherung/eingabe"
_path_to_chromedriver = "/usr/bin/chromedriver"
#user_of_choice = Users.user_poor_employee

chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chromedriver)  # open internet
    # open internet

#wait = WebDriverWait(chrome_webdriver, 20)

website = _base_url
chrome_webdriver.get(website)
#chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chromedriver)

page = Callback(driver=chrome_webdriver)
page.callback_input()
sleep(5)
page.comparison_ui_and_salesforce()



# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pages.OnlineAssistent.Tab1_Start import StartPage
# from pages.OnlineAssistent.Tab2_BerufsStatus import BerufsStatusPage
# from pages.OnlineAssistent.Tab4_DataEingabe import Eingabe, Beitragsentlastung, UbertragungswertPage
# from pages.OnlineAssistent.Tab5_Result import ResultPageClinik
# from pages.OnlineAssistent.AuthApp import AuthAppPage
# from pages.OnlineAssistent.Tab3_TypeVersich import TypeVersicherung
# import random
# from time import sleep
# from DataObjects.Users import OnlineAssistanceUsers
#
#
# _base_url = "https://test.on.ag/online-assistent"
# _path_to_chromedriver = "/usr/bin/chromedriver"
#
# # Defining prefill users
#
# selbstandig = OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED
# angestellter = OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE
#
# # Defining user choice
# users_of_choice = [selbstandig,
#                    angestellter
#                    ]
# random_user = random.choice(users_of_choice) #No randomization here
#
# chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chromedriver) # chrome
# wait = WebDriverWait(chrome_webdriver, 20)
#
# # 1 Open website
# website = _base_url + StartPage.my_url
# chrome_webdriver.get(website)
# page = StartPage(driver=chrome_webdriver)
#
# # 2 Click on Beitrag Berechnen tile
# page.find_beitrag_berechnen_button.click()
# wait.until(EC.url_contains(BerufsStatusPage.my_url))
# page = BerufsStatusPage(driver=chrome_webdriver)
# page.check_weiter_button_is_disabled()
#
# # 3 Select user
# print("USER: {user}.".format(user=random_user))
# page.berufstatus_select.select_by_visible_text(random_user)
#
# if random_user == OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE:
#    page.income_input.send_keys(OnlineAssistanceUsers.generate_random_income(rich=True))
# page.check_weiter_button_is_enabled()
# page.weiter_button.click()
#
# # 4 Choose insurance type
# page = TypeVersicherung(driver=chrome_webdriver)
# randomly_chosing_insurance_type = random.choice(OnlineAssistanceUsers.OA_ALLOWED_OCCUPATIONS)
# #if random_user in [OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT,
# #                   OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT_APPLICANT]:
# page.find_vollversicherung_button.click()
# #else:
# #     page.randomly_chosing_insurance_type.click()
#
# # 5 Adding necesary information about the user
# def users_info():
#     page = Eingabe(driver=chrome_webdriver)
#     page.input_30yo()
#     # Self-employed and Employed
#     if random_user in [OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED,
#                        OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE]:
#         if random_user == OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED:
#             page.randomly_choosing_worker_amount_selbstandig()
#         if random_user == OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED:
#             page.randomly_choosing_worker_amount_selbstandig()
#         page.select_insurance_start_date()
#         previous_insurance = page.select_previous_insurance_by_text()
#         page.check_weiter_button_is_enabled()
#         page.weiter_button.click()
#         # if previously privately insured
#         if previous_insurance == "Privat":
#             print("Private insurance!")
#             page = UbertragungswertPage(driver=chrome_webdriver)
#             page.input_uebertragungswert()
#             page.weiter_button.click()
#         print("Choosing lebensjahr!")
#         page = Beitragsentlastung(driver=chrome_webdriver)
#         sleep(2)
#         random_lebensjahr_button = page.random_lebensjahr_button
#         random_lebensjahr_button.click()
#         print(random_lebensjahr_button.good_text)
#         page.check_weiter_button_is_enabled()
#         page.weiter_button.click()
#     # Student
#     elif random_user == OnlineAssistanceUsers.OA_OCCUPATION_STUDENT:
#         page.select_previous_insurance_by_text()
#         page.select_insurance_start_date()
#         page.weiter_button.click()
#     # Civil servant and civil servant applicant
#     elif random_user == OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT or OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT_APPLICANT:
#         page.select_randomly_beihilfe_state()
#         page.select_randomly_beihilfe_satz()
#         page.input_beihilfe_start()
#         page.select_randomly_beihilfe_start()
#         page.weiter_button.click()
#     else:
#         print("Non-existing proffession!")
#
# users_info()
# page = ResultPageClinik(driver=chrome_webdriver)
# page.find_weiter_button.click()
# page = AuthAppPage(driver=chrome_webdriver)
# page.check_weiter_button_is_enabled()
# page.weiter_button.click()
#
# # elif random_user == OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED:
#     #page.randomly_choosing_worker_amount_selbstandig()
#
#
#
#
#
#
#
#
#
#
#
#
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from onSeleniumBased.modules.pages.OnlineAssistent.Start import Start
# from onSeleniumBased.modules.pages.OnlineAssistent.Tab2_Beitrag_berechnen.Berufsstatus import Occupation, \
#     Calculation, ContributionRelief, TransferValue, Selection
# from onSeleniumBased.modules.pages.OnlineAssistent.Tab2_Beitrag_berechnen.Result import Result
# from onSeleniumBased.modules.pages.OnlineAntrag.Stage0_IntroRegistration import IntroPage
# import random
# from time import sleep
#
# #TODO: Optin prefill page add into Stage0_introRegistration
#
# #from pages.OnlineAssistent.Tab1_Start import StartPage
# #from pages.OnlineAssistent.Tab2_BerufsStatus import BerufsStatusPage
# #from pages.OnlineAssistent.Tab3_TypeVersich import TypeVersicherung
# #from pages.OnlineAssistent.Tab4_DataEingabe import Eingabe, Beitragsentlastung, UbertragungswertPage
# #from pages.OnlineAssistent.Tab5_Result import ResultPageClinik
# #from pages.OnlineAssistent.AuthApp import AuthAppPage
#
#
# from DataObjects.Users import OnlineAssistanceUsers
#
# s = self.setup
#
# page = AdminAppLogin.Login(setup=s, open_page=True)
#
# _base_url = "https://test.on.ag/online-assistent"
# _path_to_chromedriver = "/usr/bin/chromedriver"
#
# # Defining prefill users
#
# selbstandig = OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED
# angestellter = OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE
#
# # Defining user choice
# users_of_choice = [selbstandig,
#                    angestellter
#                    ]
# random_user = random.choice(users_of_choice) #No randomization here
#
# chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chromedriver) # chrome
# wait = WebDriverWait(chrome_webdriver, 20)
#
# # 1 Open website
# website = _base_url + StartPage.my_url
# chrome_webdriver.get(website)
# page = StartPage(driver=chrome_webdriver)
#
# # 2 Click on Beitrag Berechnen tile
# page.find_beitrag_berechnen_button.click()
# wait.until(EC.url_contains(BerufsStatusPage.my_url))
# page = BerufsStatusPage(driver=chrome_webdriver)
# page.check_weiter_button_is_disabled()
#
# # 3 Select user
# print("USER: {user}.".format(user=random_user))
# page.berufstatus_select.select_by_visible_text(random_user)
#
# if random_user == OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE:
#    page.income_input.send_keys(OnlineAssistanceUsers.generate_random_income(rich=True))
# page.check_weiter_button_is_enabled()
# page.weiter_button.click()
#
# # 4 Choose insurance type
# page = TypeVersicherung(driver=chrome_webdriver)
# randomly_chosing_insurance_type = random.choice(OnlineAssistanceUsers.OA_ALLOWED_OCCUPATIONS)
# #if random_user in [OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT,
# #                   OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT_APPLICANT]:
# page.find_vollversicherung_button.click()
# #else:
# #     page.randomly_chosing_insurance_type.click()
#
# # 5 Adding necesary information about the user
# def users_info():
#     page = Eingabe(driver=chrome_webdriver)
#     page.input_30yo()
#     # Self-employed and Employed
#     if random_user in [OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED,
#                        OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE]:
#         if random_user == OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED:
#             page.randomly_choosing_worker_amount_selbstandig()
#         if random_user == OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED:
#             page.randomly_choosing_worker_amount_selbstandig()
#         page.select_insurance_start_date()
#         previous_insurance = page.select_previous_insurance_by_text()
#         page.check_weiter_button_is_enabled()
#         page.weiter_button.click()
#         # if previously privately insured
#         if previous_insurance == "Privat":
#             print("Private insurance!")
#             page = UbertragungswertPage(driver=chrome_webdriver)
#             page.input_uebertragungswert()
#             page.weiter_button.click()
#         print("Choosing lebensjahr!")
#         page = Beitragsentlastung(driver=chrome_webdriver)
#         sleep(2)
#         random_lebensjahr_button = page.random_lebensjahr_button
#         random_lebensjahr_button.click()
#         print(random_lebensjahr_button.good_text)
#         page.check_weiter_button_is_enabled()
#         page.weiter_button.click()
#     # Student
#     elif random_user == OnlineAssistanceUsers.OA_OCCUPATION_STUDENT:
#         page.select_previous_insurance_by_text()
#         page.select_insurance_start_date()
#         page.weiter_button.click()
#     # Civil servant and civil servant applicant
#     elif random_user == OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT or OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT_APPLICANT:
#         page.select_randomly_beihilfe_state()
#         page.select_randomly_beihilfe_satz()
#         page.input_beihilfe_start()
#         page.select_randomly_beihilfe_start()
#         page.weiter_button.click()
#     else:
#         print("Non-existing proffession!")
#
# users_info()
# page = ResultPageClinik(driver=chrome_webdriver)
# page.find_weiter_button.click()
# page = AuthAppPage(driver=chrome_webdriver)
# page.check_weiter_button_is_enabled()
# page.weiter_button.click()
#
# # OPTINPREFILL prepared for data
#
