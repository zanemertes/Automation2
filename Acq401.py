from pages.OnlineAssistent.onSeleniumBased.ConsultationExpats import Callback
from selenium import webdriver


_path_to_chrome_driver = "/usr/bin/chromedriver"
chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chrome_driver)
website = Callback.my_url
chrome_webdriver.get(website)
page = Callback(driver=chrome_webdriver)
page.callback_input()
final = page.read_info_ui()
page.comparison_ui_and_salesforce()

# BE Request for calendar
# OA into Signup. Welche Tags wird für welchen signup vorbereitet
# BUY- https://jira.office.ottonova.de/browse/BUY-363