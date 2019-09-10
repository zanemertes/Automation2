import os
import socket
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait

# from onSeleniumBased.Methods import url
# from onSeleniumBased.Constants import SCHEMES, MACHINES, \
#     E_PREVIEW, E_LOCAL, E_TEST, E_STAGING, \
#     B_MASTER, \
#     A_MAIN, A_MIDDLEWARE, \
#     S_HTTPS, S_HTTP
# from onSeleniumBased.modules.Printing import log

log_path = "onSeleniumBased/logs" #keep

p_logs = os.path.join(os.getcwd(), log_path) #keep
# p_logs = os.path.join(os.getcwd(), "logs")
f___log = os.path.join(p_logs, "LOG_automated_test_" +
                       datetime.now().strftime("%Y_%m_%d__%H_%M_%S") + ".txt")
f__warn = os.path.join(p_logs, "WARNINGS_automated_test_" +
                       datetime.now().strftime("%Y_%m_%d__%H_%M_%S") + ".txt")
f_error = os.path.join(p_logs, "ERRORS_automated_test_" +
                       datetime.now().strftime("%Y_%m_%d__%H_%M_%S") + ".txt")
f_debug = os.path.join(p_logs, "DEBUGS_automated_test_" +
                       datetime.now().strftime("%Y_%m_%d__%H_%M_%S") + ".txt")

AGENT_EMAIL = "agent@ottonova.de"
AGENT_PASS = "agent"
USER_PASS = "7Zeichen"

#
# class Setup(object):
#     from selenium.webdriver import ChromeOptions
#     from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#     # this should define the webDriver properties
#     options = ChromeOptions()
#
#     # Enable JS console Output in terminal
#     settingsDict = DesiredCapabilities.CHROME
#     settingsDict['loggingPrefs'] = {'browser': 'ALL'}
#
#     options.add_argument("no-sandbox")
#     options.add_argument("start-maximized")
#     capabilities = options.to_capabilities()
#     desired_capabilities = {'browserName': 'Chrome'}
#     # capabilities = {'chrome.binary': '/usr/local/bin/chromedriver'}
#     chrome_driver_path = {MACHINES['bchmura']:
#                           '/usr/local/bin/chromedriver',
#                           MACHINES['zmertes']:
#                           "C:\\Users\\zane.mertes\\PycharmProjects\\chromedriver\\chromedriver.exe"}
#     # location = 'staging'
#     _application = A_MAIN
#     environment = E_PREVIEW
#     branch = B_MASTER
#     step = 0
#     run = 0
#     signup_incomplete = None
#     user = None
#
#     def __init__(self,
#                  environment: str=E_PREVIEW,
#                  branch: str=B_MASTER,
#                  remote: bool=True,
#                  start_browser: bool=True):
#         """
#             initializes the Setup class
#         :param environment:
#             on which test environment will the tests be executed
#         :param branch:
#             in case the env=PREVIEW, which code branch should the tests be executed against
#         :param remote:
#             should a remote selenium webdriver be used, or a local one?
#         :param start_browser:
#             should a browser be started then initializing?
#         """
#
#         print("env={0}".format(environment))
#         print("rmt={0}".format(remote))
#         self.environment = environment
#         self.remote = remote
#         self.branch = branch
#         self.signup_incomplete = None
#         # TODO: Fix gethostname
#         self.machine = socket.gethostname()
#         if self.machine in [MACHINES['bchmura'], MACHINES['zmertes']]:
#             self.command_executor = url(scheme=S_HTTP, env=E_LOCAL, app=A_MAIN, add_on=':4444/wd/hub')
#             # self.command_executor = SCHEMES['http'] + "localhost:4444/wd/hub"
#         else:
#             # SeleniumHub @ Ottonova
#             self.command_executor = SCHEMES[S_HTTP] + "selenium-hub:4444/wd/hub"
#         print("Will work with the following command executor: '{0}'".format(self.command_executor))
#
#         if self.remote:
#             self.driver = RemoteWebDriver(desired_capabilities=self.capabilities,
#                                           command_executor=self.command_executor)
#             print("RemoteWebDriver initialized")
#         else:
#             self.driver = webdriver.Chrome(self.chrome_driver_path[self.machine])
#             print("Local WebDriver initialized")
#         self.wait = WebDriverWait(self.driver, timeout=4, poll_frequency=0.5)
#
#         if start_browser:
#             new_window = self.driver.window_handles[0]
#             self.driver.switch_to.window(new_window)
#             # cls.driver.set_window_rect(1312, 24, 1248, 1416)
#             if self.remote:
#                 self.driver.set_window_rect(0, 0, 1920, 1080)
#             else:
#                 # TODO: Make this work :(
#                 if self.machine == MACHINES['zmertes']:
#                     self.driver.set_window_rect(0, 0, 1920, 1080)
#                 else:
#                     self.driver.execute("fullscreenWindow", {"windowHandle": "current"})
#                     time.sleep(2)
#                     self.driver.maximize_window()
#             # cls.driver.get(Setup.start_url)
#             from onSeleniumBased.modules.pages.Auth.Login import Login
#             # self.driver.get(self.build_url_1_1(app=Login.application, url=Login.expected_url, loc=self.environment))
#             self.driver.get(self.page_url(page_class=Login))
#
#             first_window_handle = self.driver.current_window_handle
#             # print("Current window handle = {0}".format(first_window_handle))
#             log("Current window handle = {0}".format(first_window_handle))
#
#         self.AGENT_EMAIL = AGENT_EMAIL
#         self.AGENT_PASS = AGENT_PASS
#         self.USER_PASS = USER_PASS
#
#     # BE SURE to check what version of HUB and NODE are being run.
#     # 3.1.0 as HUB will pose problems!
#     # 2.53.1 + 2.53.1 will work nice
#     # 3.5.3  + 3.5.3  will also work nice
#     # Testing of 3.5.3 as locally
#
#     # this should define the root url for all pages to use
#     # root_url = "http://localhost:8080"
#     # str_root_url = SCHEMES['https'] + LOCATIONS[environment]['auth-app'] + '/'
#     str_root_url = url(scheme='https', env=environment, app='auth-app', add_on='/')
#
#     def page_url(self,
#                  page_class,
#                  add_on: str= '',
#                  env: str= "",
#                  branch_hash: str= "",
#                  origin: str or None=None):
#         """
#             Builds a url based on the page class and environment
#
#         :param page_class:
#             respective class of the page for which the url is to be built
#         :param add_on:
#             what should be added to the URL at the end
#         :param env:
#             environment for which the url is to be built - per default takes the one set for 'Setup' class
#         :param branch_hash:
#             the branch hash to be used
#         :param origin:
#             which origin (if any) is to be used
#         :return:
#             complete url
#         """
#         from onSeleniumBased.Methods import page_url
#
#         if env == "":
#             env = self.environment
#         if branch_hash == "":
#             branch_hash = self.branch
#
#         return page_url(page_class=page_class, add_on=add_on, env=env, branch_hash=branch_hash, origin=origin)
#
#     def make_screenshot(self, test_name: str, step_description: str):
#         self.step += 1
#         self.driver.save_screenshot("Step {1} - Tab1_Passender_Tariff {0} - {2}.png".format(test_name,
#                                                                            self.step,
#                                                                            step_description))
#
#     def _write_to_file(self, _filename: str, object_key: str, append: bool=False, _type: str='variable'):
#         from onSeleniumBased.modules.Printing import write_to_file, append_to_file, p_e
#         from onSeleniumBased.modules.User import BodyMassIndex, Address, IBAN, CivilServant, HealthQuestions, \
#             Occupation, DailySicknessAllowance, AgeContributionRelief, PreviousInsurance
#         if object_key not in vars(self.user):
#             return
#
#         v = vars(self.user)[object_key]
#
#         _print_string = None
#         if type(v) in [BodyMassIndex,
#                        Address,
#                        IBAN,
#                        CivilServant,
#                        HealthQuestions,
#                        Occupation,
#                        AgeContributionRelief,
#                        DailySicknessAllowance,
#                        PreviousInsurance]:
#             _print_string = object_key + ':\n' + v.printable
#         else:
#             _print_string = object_key + '\t=\t' + str(v)
#
#         if append:
#             append_to_file(_filename=_filename, _print_string=_print_string)
#         else:
#             write_to_file(_filename=_filename, _print_string=_print_string)
#
#     def store_user_data_in_file(self, f: str or None):
#         from onSeleniumBased.modules.Printing import append_to_file
#
#         if f is None or f == "":
#             f = "ENVIRONMENT_" + self.environment + "_USER_" + self.user.forename + "_" + self.user.lastname + ".txt"
#         self._write_to_file(_filename=f, append=False, object_key='forename')
#         self._write_to_file(_filename=f, append=True, object_key='lastname')
#         self._write_to_file(_filename=f, append=True, object_key='title')
#         self._write_to_file(_filename=f, append=True, object_key='mobile')
#         self._write_to_file(_filename=f, append=True, object_key='email')
#         self._write_to_file(_filename=f, append=True, object_key='address')
#         self._write_to_file(_filename=f, append=True, object_key='date_of_birth')
#         self._write_to_file(_filename=f, append=True, object_key='bmi_parameters')
#         self._write_to_file(_filename=f, append=True, object_key='nationality')
#         self._write_to_file(_filename=f, append=True, object_key='occupation')
#         self._write_to_file(_filename=f, append=True, object_key='iban')
#         self._write_to_file(_filename=f, append=True, object_key='direct_debit_authorization')
#         self._write_to_file(_filename=f, append=True, object_key='previous_insurance')
#         self._write_to_file(_filename=f, append=True, object_key='transfer_value')
#         self._write_to_file(_filename=f, append=True, object_key='transfer_value_known')
#         self._write_to_file(_filename=f, append=True, object_key='transfer_requested')
#         self._write_to_file(_filename=f, append=True, object_key='civil_servant')
#         self._write_to_file(_filename=f, append=True, object_key='age_contribution_relief')
#         self._write_to_file(_filename=f, append=True, object_key='daily_sickness_allowance')
#         self._write_to_file(_filename=f, append=True, object_key='health_questions')
#         self._write_to_file(_filename=f, append=True, object_key='insurance_start_date')
#         self._write_to_file(_filename=f, append=True, object_key='request_consultation')
#         self._write_to_file(_filename=f, append=True, object_key='consultation_requested_date')
#         self._write_to_file(_filename=f, append=True, object_key='consultation_appointment')
#         self._write_to_file(_filename=f, append=True, object_key='consultation_completed')
#         self._write_to_file(_filename=f, append=True, object_key='tariff')
#         self._write_to_file(_filename=f, append=True, object_key='cost_participation')
#         # self._write_to_file(_filename=f, append=True, object_key='health_box')
#         self._write_to_file(_filename=f, append=True, object_key='account_created')
#         self._write_to_file(_filename=f, append=True, object_key='last_signup_stage_completed')
#         self._write_to_file(_filename=f, append=True, object_key='signup_completed')
#         self._write_to_file(_filename=f, append=True, object_key='underwriting_completed')
#         self._write_to_file(_filename=f, append=True, object_key='offer_to_be_accepted')
#         self._write_to_file(_filename=f, append=True, object_key='offer_accepted')
#         self._write_to_file(_filename=f, append=True, object_key='contract_signed')
#         self._write_to_file(_filename=f, append=True, object_key='expected_rejection')
#         self._write_to_file(_filename=f, append=True, object_key='signup_rejected')
#
#         _EXPECTED_ITEMS_LIST = ['forename',
#                                 'lastname',
#                                 'title',
#                                 'mobile',
#                                 'email',
#                                 'address',
#                                 'date_of_birth',
#                                 'bmi_parameters',
#                                 'nationality',
#                                 'iban',
#                                 'direct_debit_authorization',
#                                 'previous_insurance',
#                                 'transfer_value',
#                                 'transfer_value_known',
#                                 'transfer_requested',
#                                 'civil_servant',
#                                 'age_contribution_relief',
#                                 'daily_sickness_allowance',
#                                 'health_questions',
#                                 'insurance_start_date',
#                                 'request_consultation',
#                                 'consultation_requested_date',
#                                 'consultation_appointment',
#                                 'consultation_completed',
#                                 'tariff',
#                                 'cost_participation',
#                                 'account_created',
#                                 'last_signup_stage_completed',
#                                 'signup_completed',
#                                 'underwriting_completed',
#                                 'offer_to_be_accepted',
#                                 'offer_accepted',
#                                 'contract_signed',
#                                 'expected_rejection',
#                                 'signup_rejected']
#         _EXPECTED_OBJECTS_LIST = ['bmi_parameters',
#                                   'address',
#                                   'health_questions',
#                                   'iban',
#                                   'civil_servant',
#                                   'occupation',
#                                   'age_contribution_relief',
#                                   'daily_sickness_allowance',
#                                   'previous_insurance']
#         # iterates all variables in this class and prints their variable names ('key') and values
#         for key, value in vars(self.user).items():
#             # the first two are to be on top of the file ALWAYS. The rest contain class-instances
#             if key not in _EXPECTED_ITEMS_LIST:
#                 append_to_file(_filename=f, _print_string=key + "\t=\t" + str(value))
#             # in special cases, where the variables are objects - their printable versions are used
#             if key in _EXPECTED_OBJECTS_LIST and value is not None:
#                 append_to_file(_filename=f, _print_string=key + ":\n" + value.printable)
#
#     @property
#     def middleware_url(self) -> str:
#         if self.environment == E_PREVIEW:
#             return url(scheme=S_HTTPS, env=self.environment, app=A_MIDDLEWARE, branch_hash=self.branch)
#         else:
#             return url(scheme=S_HTTPS, env=self.environment, app=A_MIDDLEWARE)
#
#     @property
#     def long_env(self) -> str:
#         from onSeleniumBased.modules.Printing import p_e
#         if self.environment == E_PREVIEW:
#             return '{0}.on.ag'.format(self.branch)
#         if self.environment in [E_TEST, E_STAGING]:
#             return '{0}.on.ag'.format(self.environment)
#         else:
#             p_e("env: {0} not supported".format(self.environment))
#             raise ValueError
#
#
# def switch_to_tab(driver, which: int=-1) -> str:
#     new_window_handle = driver.window_handles[which]
#     driver.switch_to.window(new_window_handle)
#     return new_window_handle
