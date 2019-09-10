from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.mywebelement import MyWebElement
from selenium.webdriver.remote.webelement import WebElement


class Page(object):
    my_url = None


    def __init__(self, driver):
        self.wait = WebDriverWait(driver=driver, timeout=10)
        self.wait.until(EC.url_contains(self.my_url))
        assert self.my_url in driver.current_url
        print("Correct URL: {url}!".format(url=self.my_url))

        self.body = driver.find_element_by_xpath("//body")


class WeiterButtonPage(Page):
    _WEITERBUTTON = 'weiter button'

    locators = {_WEITERBUTTON:
                './/button[contains(text(), "Weiter")]'
                }

    def __init__(self, driver):
        super().__init__(driver)
        # self.wait.until(EC.visibility_of_element_located())

    @property
    def weiter_button(self) -> MyWebElement:
        return MyWebElement(_we=self.body.find_element_by_xpath(self.locators[self._WEITERBUTTON]))

    def check_weiter_button_is_disabled(self):
        self.weiter_button.scroll_into_view()
        #self.wait.until_not(EC.element_to_be_clickable(self.weiter_button))
        assert not self.weiter_button.is_enabled()
        print("Weiter button disabled!")

    def check_weiter_button_is_enabled(self):
        self.weiter_button.scroll_into_view()
        #self.wait.until(EC.element_to_be_clickable(self.weiter_button))
        assert self.weiter_button.is_enabled()
        print("Weiter button enabled!")

    def click_weiter_button(self):
        self.weiter_button.scroll_into_view()
        self.weiter_button.click()


