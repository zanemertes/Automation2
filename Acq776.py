from pages.OnlineAssistent.onSeleniumBased.ConsultationExpats import Expats
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from elements.mywebelement import MyWebElement
from selenium.webdriver.support import expected_conditions as EC

def consultation_expats():
    #_base_url = "https://test.on.ag/expats"
    _path_to_chrome_driver = "/usr/bin/chromedriver"

    chrome_webdriver = webdriver.Chrome(executable_path=_path_to_chrome_driver)

    wait = WebDriverWait(chrome_webdriver, 20)
    website = Expats.my_url
    chrome_webdriver.get(website)

    page = Expats(driver=chrome_webdriver)
    page.find_consultation_buttton.click()
    time.sleep(2)
    # page.wait.until(EC.element_located_to_be_selected( locator='.//div[contains(.,"First Name*")]/input[@name="firstName"]'))
    # page.wait.until(EC.visibility_of_element_located())
    page.input_user_info()
    page.select_appointment()
    #page.find_submit_button.scroll_into_view()
    page.find_ok_button.click()
    time.sleep(2)
    page.find_submit_button.click()
    print("Appointment booked!")
    time.sleep(10)
    chrome_webdriver.close()

# consultation_expats()
# print("1")
#
# consultation_expats()
# print("2")
#
# consultation_expats()
# print("3")
#
# consultation_expats()
# print("4")
#
# consultation_expats()
# print("5")



for iterator in range(1, 10):
     print(iterator)
     consultation_expats()


