
from pages.OnlineAssistent.Callback import Callback
from selenium import webdriver
from time import sleep

_path_to_chromedriver = "/usr/bin/chromedriver"
chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chromedriver)

page = Callback(driver=chrome_webdriver)
page.callback_input()
sleep(5)
page.comparison_ui_and_salesforce()