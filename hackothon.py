import re
from _datetime import datetime
from datetime import date
from datetime import time
from dateutil.relativedelta import relativedelta

import pymysql.cursors
from time import mktime
from datetime import datetime

connection = pymysql.connect(host='test-core-mysql-01-rds.czohthzn9tjg.eu-central-1.rds.amazonaws.com',
                             user='middleware_signup',
                             password='TESTfaemei0Ahchi0eiyai8eig8pu',
                             database='middleware_signup',
                             port=3306)

# connection_preview = pymysql.connect(host='db',
#                              user='signup',
#                              password='signup',
#                              database='signup',
#                              port=3306)

cursor = connection.cursor(pymysql.cursors.DictCursor)

print("Databases")
cursor.execute("show databases")
for databases in cursor:
    print(databases)

#signup_id = test.setup.user.signup_id
#test.setup.user.signup_id
#signup_id = '720f51e2-dddf-458b-99b9-42c4a5c3057e'
signup_id = 'e5487b57-08a8-43ef-9508-436b78e21dd8'

cursor.execute('select * from signup where signup_id="{signup_id}"'.format(signup_id=signup_id))

for old_state in cursor:
    print(old_state)

signup_data = old_state['signup_data']
print(signup_data)

url_regex = r'offer_expiry": "(.*)", "idd_consultation'
before_regex = r'(.*"offer_expiry": ")'
after_regex = r'(", "idd_consultation.*)'
results = re.findall(url_regex, signup_data)
ddate = results[0]
print(ddate)
#_date_time_read_formatting = "%Y-%m-%dT%H:%M:%S+00:00"
datetime_date = datetime.strptime(ddate, "%Y-%m-%dT%H:%M:%S+00:00")
print("Existing expiry: " + str(datetime_date))
d = date.today()
print("Todays date: " + str(d))
new_expiry = d - relativedelta(days=1)
new_offer_expiry_date = date(new_expiry.year, new_expiry.month, new_expiry.day)

new_offer_expiry_time = time(datetime_date.hour, datetime_date.minute, datetime_date.second)

#print("New expiry: " + str(new_offer_expiry))
#print("New expiry: " + str(new_offer_expiry_time))
nedate=str(new_offer_expiry_date)
netime=str(new_offer_expiry_time)
ne_expiry_string=(nedate+"T"+netime+"+00:00")

cursor.execute('select * from signup where signup_id="{signup_id}"'.format(signup_id=signup_id))
old_entry = cursor._rows[-1]

results_b = re.findall(before_regex, signup_data)
results_a = re.findall(after_regex, signup_data)
print(results_b[0]+ne_expiry_string+results_a[0])
final_string = (results_b[0]+ne_expiry_string+results_a[0])
# cursor.execute("""insert into signup set
#                id="{id}",
#                signup_id="{signup_id}",
#                account_id="{account_id}",
#                signup_state="{signup_state}",
#                version="{version}",
#                signup_data="{signup_data}",
#                member_data="{member_data}",
#                created={created})""".format(id=None,
#                                             signup_id=old_state["signup_id"],
#                                             account_id=old_state["account_id"],
#                                             signup_state=old_state["signup_state"],
#                                             version=old_state["version"]+1,
#                                             signup_data=final_string,
#                                             member_data=old_state["member_data"],
#                                             created=datetime.now()
#                                         ))


cursor.execute("""INSERT INTO `signup` VALUES ('{id}', '{signup_id}', '{account_id}', '{signup_state}', '{version}', '{signup_data}', '{member_data}', '{created}')""".format(
    id=None,
    signup_id=old_state['signup_id'],
    account_id=old_state['account_id'],
    signup_state=old_state['signup_state'],
    version=old_state['version']+1,
    signup_data=old_state['signup_data'],
    member_data=old_state['member_data'],
    created=datetime.now()
))

#member_data='[{"job": {"id": 263, "name": "Gerber/in"}, "meta": {"completed_sections": ["personal", "insurance", "job", "health", "tariff"]}, "name": {"title": "", "last_name": "Test BJAHAEBFDAEC N", "first_name": "Test BJAHAEBFDAEC V"}, "email": "zmertes+auto-compr-190704153042@on-testing.de", "gender": "female", "health": {"height": 150, "weight": 53, "questions": {"answers": {"allergy": {"type": "yes_no", "value": false}, "treatment": {"type": "yes_no", "value": false}, "addictions": {"type": "yes_no", "value": false}, "medication": {"type": "yes_no", "value": false}, "hiv_infection": {"type": "yes_no", "value": false}, "chronic_disease": {"type": "yes_no", "value": false}, "health_impairment": {"type": "checklist", "value": {"prosthesis": false, "hearing_aid": false, "infertility": false, "body_implant": false, "missing_teeth": false, "disability_malformation": false, "war_military_service_injury": false, "reduced_earning_capacity_occupational_disability": false}}, "malignant_disease": {"type": "yes_no", "value": false}, "planned_treatment": {"type": "yes_no", "value": false}, "psychological_care": {"type": "yes_no", "value": false}, "surgery_hospitalization": {"type": "yes_no", "value": false}}, "version": "20180326"}, "has_confirmed_disclaimer": true}, "salary": 62860, "address": {"zip": "85748", "city": "Garching b München", "street": "Schrödingerweg", "addition": "", "is_confirmed": true, "street_number": "2"}, "country": {"id": "EE", "name": "Estland", "is_in_eu": true}, "tariff_id": "business-10", "profile_id": "0603eb44-da4c-42a7-9a1d-b75ef8d455c7", "member_type": "insured_policy_holder_premium_payer", "phone_number": "+4917636362207", "underwriting": {"decision": "accepted"}, "date_of_birth": "1997-04-02", "contract_inquiry": {"contract_start_date": "2019-08-01"}, "residence_permit": {"immigration_date": "2012-07-01"}, "current_insurance": {"type": "private", "company_id": 4095, "start_date": "1997-05-03", "is_cancelled": true, "has_contribution_payment_deficit": false, "has_contribution_payment_emergency": false}, "risk_rating_result": {"type": "success", "rating_result": {"log": [{"rule": {"id": "hasLegalAge", "title": "None-Civil-Servant policy holder is of legal age", "reject": true}, "passed": true}, {"rule": {"id": "hasLegalCivilServantAge", "title": "Civil-Servant policy holder is of legal age", "reject": true}, "passed": true}, {"rule": {"id": "hasNoExceptionalBmi", "title": "Body Mass Index (BMI) is not exceptional low or high", "reject": true}, "passed": true}, {"rule": {"id": "hasNoMalignantDisease", "title": "No maligant desease", "reject": true}, "passed": true}, {"rule": {"id": "hasNoHivInfection", "title": "No HIV infection", "reject": true}, "passed": true}, {"rule": {"id": "hasNoAddictions", "title": "No addictions", "reject": true}, "passed": true}, {"rule": {"id": "hasNoReducedEarningCapacity", "title": "No reduced earning capacity", "reject": true}, "passed": true}, {"rule": {"id": "hasNoMilitaryServiceInjury", "title": "No military service injury", "reject": true}, "passed": true}, {"rule": {"id": "isNotASeniorStudent", "title": "Member must not be senior student", "reject": true}, "passed": true}, {"rule": {"id": "hasInsurableProfession", "title": "Member has an insurable profession", "reject": true}, "passed": true}, {"rule": {"id": "earnsMoreThanAnnualEarningLimit", "title": "Employed policy holders must earn more than the annual earning limit", "reject": true}, "passed": true}, {"rule": {"id": "hasNoPreviousInsuranceForAGoodReason", "title": "No previous insurance only for a good reason", "reject": true}, "passed": true}, {"rule": {"id": "hasNoTroubleWithPreviousInsurance", "title": "Member must not have trouble with previous insurance", "reject": true}, "passed": true}, {"rule": {"id": "hasUnsuspiciousSchufaFilter", "title": "Policy holders must have an unsuspicious SCHUFA filter", "reject": true}, "passed": true}, {"rule": {"id": "hasUnsuspiciousSchufaScoreAddenda", "title": "Policy holders must have unsuspicious SCHUFA addenda", "reject": true}, "passed": true}, {"rule": {"id": "hasUnsuspiciousSchufaScore", "title": "Policy holders must have an unsuspicious SCHUFA score", "reject": true}, "passed": true}, {"rule": {"id": "isNotASenior", "title": "Member is not a senior", "reject": false}, "passed": true}, {"rule": {"id": "isNotAJunior", "title": "Member is not a junior", "reject": false}, "passed": true}, {"rule": {"id": "isNotAWorkingAdolescent", "title": "Member is not a working adolescent", "reject": false}, "passed": true}, {"rule": {"id": "isNotACivilServantMinor", "title": "Civil-Servant policy holder is not a minor", "reject": false}, "passed": true}, {"rule": {"id": "hasNonQuestionableProfession", "title": "Member has a non-questionable profession", "reject": false}, "passed": false}, {"rule": {"id": "isNotSelfEmployed", "title": "Member is not self-employed", "reject": false}, "passed": true}, {"rule": {"id": "isNotAStudent", "title": "Member is not a student", "reject": false}, "passed": true}, {"rule": {"id": "hasValidAddress", "title": "Member has a valid address", "reject": false}, "passed": true}, {"rule": {"id": "hasNoNoticeableBmi", "title": "Body Mass Index (BMI) is not noticeable low or high", "reject": false}, "passed": true}, {"rule": {"id": "hasNoHealthIssues", "title": "No affirmed health questions", "reject": false}, "passed": true}, {"rule": {"id": "hasNoPsychologicalPreCondition", "title": "No psychological pre-condition", "reject": false}, "passed": true}, {"rule": {"id": "hasProfession", "title": "Member has a profession", "reject": false}, "passed": true}, {"rule": {"id": "hasPreviousInsurance", "title": "Member must have a previous insurance", "reject": false}, "passed": true}, {"rule": {"id": "hasNoForeignPreviousInsurance", "title": "No foreign previous insurance", "reject": false}, "passed": true}, {"rule": {"id": "livesInGermanyForAtLeast36Months", "title": "Immigrant has to live in Germany for at least 36 months", "reject": false}, "passed": true}, {"rule": {"id": "visaIsValidForAtLeast24Months", "title": "Visa holder has a valid visa for at least 24 months", "reject": false}, "passed": true}, {"rule": {"id": "hasNoSchufaFilter", "title": "Policy holders must not have a SCHUFA filter", "reject": false}, "passed": true}, {"rule": {"id": "hasNotOnlySchufaRequest", "title": "Polcy holders must not only have SCHUFA requests", "reject": false}, "passed": true}, {"rule": {"id": "hasUnsuspiciousSchufaScoreForSelfEmployees", "title": "Self employed policy holders must have an even more unsuspicious SCHUFA score", "reject": false}, "passed": true}, {"rule": {"id": "hasSchufaScore", "title": "Policy holders must have an known SCHUFA score", "reject": false}, "passed": true}], "rating": "underwriting", "context": {"lead": {"bmi": 23.555555555555557, "salary": 6286000, "bmiScore": "normal", "isStudent": false, "isEmployed": true, "profession": 263, "isImmigrant": true, "addressScore": "valid", "schufaFilter": null, "hasProfession": true, "preconditions": [], "schufaMessage": null, "isCivilServant": false, "isPolicyHolder": true, "isSelfEmployed": false, "hasPreconditions": false, "isNonEuImmigrant": false, "schufaScoreRating": "C", "schufaScoreAddenda": ["ST004"], "ageAtInsuranceStart": 22, "hasPreviousInsurance": true, "previousInsuranceType": "private", "noPreviousInsuranceReason": null, "hasTroubleWithPreviousInsurance": false, "monthsUntilVisaExpiryAtInsuranceStart": null, "monthsSinceImmigrationAtInsuranceStart": 85}}, "evaluated_at": "2019-07-04T13:31:28+00:00", "guidelines_version": "20190405-1752"}}, "has_accepted_schufa": true, "kt_tariff_selection": {"is_selected": true, "desired_payout_rate": 50, "desired_waiting_period": 182}, "occupational_status": "employed", "bek_tariff_selection": {"is_selected": true, "desired_start_age": 64, "desired_payout_rate": 260}, "has_confirmed_summary": true, "has_requested_idd_consultation": true}]'

#cursor.execute('insert into signup set id = "116906", signup_id="e5487b57-08a8-43ef-9508-436b78e21dd8", account_id = "1977bacd-0c02-49d0-9ac6-8f00514ee670, signup_state = "present_offer", version = "49", signup_data = "{signup_data}", member_data = "{member_data}", created = "2019-07-04 13:31:39"'.format(signup_data=final_string, member_data=member_data))
#cursor.execute('INSERT INTO signup ("id", "signup_id", "account_id", "version", "signup_data", "member_data", "created") VALUES ("116906", "e5487b57-08a8-43ef-9508-436b78e21dd8", "1977bacd-0c02-49d0-9ac6-8f00514ee670, "present_offer", "49", "{signup_data}", "{member_data}", "2019-07-04 13:31:39"'.format(signup_data=final_string, member_data=member_data))
#cursor.execute('INSERT INTO signup VALUES ("116906", "e5487b57-08a8-43ef-9508-436b78e21dd8", "1977bacd-0c02-49d0-9ac6-8f00514ee670, "present_offer", "49", "{signup_data}", "{member_data}", "2019-07-04 13:31:39"'.format(signup_data=final_string, member_data=member_data))

#cursor.fetchmany(size=1)

                             #db='db',
                             #charset='utf8mb4',
                             #cursorclass=pymysql.cursors.DictCursor)

#preview

#connection = pymysql.connect(host='db',
                             #user='signup',
                             #password='signup',
# database='signup',
# port=3306)

# from onSeleniumBased.Tests import Tests
# from onSeleniumBased.Constants import E_TEST, O_COMPREHENSIVE
# from onSeleniumBased.modules.Printing import log
# from onSeleniumBased.dataStructure.User.Occupation import Occupation as UserOccupation
# from onSeleniumBased.modules.pages.OnlineAssistent.Start.Start import StartPage
# from onSeleniumBased.modules.pages.OnlineAssistent.Tab2_Beitrag_berechnen.Berufsstatus import Occupation, \
#     Selection, Calculation, ContributionRelief, TransferValue
# from onSeleniumBased.modules.pages.OnlineAssistent.Tab2_Beitrag_berechnen.Result import Result
# from onSeleniumBased.modules.pages.OnlineAntrag.Stage0_IntroRegistration import AuthAppIntroPage, OptinPrefillPage
# from time import sleep
#
# tests = Tests()
# tests.setup_class(environment=E_TEST, start_browser=True, remote=False)
#
#
# def tags_according_to_user(tag_user: UserOccupation.job_types_tags_OA):
#     page = StartPage(setup=Tests.setup, open_page=True)
#     page.beitrag_tile.click()
#
#     page = Occupation(setup=Tests.setup, open_page=True)
#     log("USER: {user}.".format(user=tag_user))
#     page.occupation_select.select_by_visible_text(tag_user)
#     if tag_user == UserOccupation.OA_EMPLOYEE:
#         page.income_input.send_keys(80000)
#     page.check_continue_button_is_enabled()
#     page.continue_button.click()
#
#     page = Selection(setup=Tests.setup)
#     page.select_card_and_continue(card='Full')
#
#     page = Calculation(setup=Tests.setup)
#     page.input_30yo()
#
#     # Self-employed and Employed
#     if tag_user in [UserOccupation.OA_EMPLOYEE, UserOccupation.OA_SELF_EMPLOYED]:
#         if tag_user == UserOccupation.OA_SELF_EMPLOYED:
#             page.randomly_choosing_worker_amount_selbstandig()
#         page.select_insurance_start_date()
#         previous_insurance = page.select_previous_insurance_by_text()
#         page.check_continue_button_is_enabled()
#         page.continue_button.click()
#
#         # if previously privately insured
#         if previous_insurance == "Privat":
#             log("Private insurance!")
#             page = TransferValue(setup=Tests.setup)
#             page.input_uebertragungswert()
#             page.check_continue_button_is_enabled()
#             page.continue_button.click()
#         log("Choosing lebensjahr!")
#         page = ContributionRelief(setup=Tests.setup)
#         sleep(2)
#         random_lebensjahr_button = page.random_lebensjahr_button
#         random_lebensjahr_button.click()
#         log(random_lebensjahr_button.good_text)
#         page.check_continue_button_is_enabled()
#         page.continue_button.click()
#     else:
#         log("Non-existing profession!")
#
#     page = Result(setup=Tests.setup)
#     page.check_continue_button_footer_is_enabled()
#     page.continue_button_footer.click()
#
#     page = AuthAppIntroPage(setup=Tests.setup, origin=O_COMPREHENSIVE)
#     page.check_continue_button_is_enabled()
#     page.continue_button.click()
#
#     page = OptinPrefillPage(setup=Tests.setup, origin=O_COMPREHENSIVE)
#     birth_day = page.find_geburtsdatum_button.good_text
#     verisch_begin = page.find_versicherungsbeginn_button.good_text
#     verisch_status = page.find_versicherungsstatus_button.good_text
#     tarif = page.find_tarif_button.good_text
#     bebeginn = page.find_beitragsentlastungsbeginn_button.good_text
#     bebetrag = page.find_beitragsentlastungsbetrag_button.good_text
#     ktgbeginn = page.find_krankentagegeldbeginn_button.good_text
#     ktgbetrag = page.find_krankentagegeldbetrag_button.good_text
#     log("Tags present = {}".format(birth_day + verisch_begin +
#                                    verisch_status + tarif +
#                                    bebeginn + bebetrag +
#                                    ktgbeginn + ktgbetrag))
#
#
# for user in UserOccupation.job_types_tags_OA.values():
#     log("user:{user}".format(user=user))
#     tags_according_to_user(tag_user=user)
