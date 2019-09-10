from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class Page(object):
    my_url = None

    def __init__(self, driver):
        self.wait = WebDriverWait(driver=driver, timeout=10)
        self.wait.until(EC.url_contains(self.my_url))
        assert self.my_url in driver.current_url
        print("Correct URL!")

        self.body = driver.find_element_by_xpath("//body")


class WeiterButtonPage(Page):
    locators = {'weiter button':
                '//button[contains(text(), "Weiter")]'
                }

    @property
    def weiter_button(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators['weiter button'])

    def check_weiter_button_is_disabled(self):
        assert not self.weiter_button.is_enabled()
        print("Weiter button disabled!")

    def check_weiter_button_is_enabled(self):
        assert self.weiter_button.is_enabled()
        print("Weiter button enabled!")

