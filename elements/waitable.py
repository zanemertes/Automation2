from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from elements.mywebelement import MyWebElement


class Waitable(MyWebElement):
    def __init__(self, _we: WebElement):
        super().__init__(_we=_we)
        self.wait = WebDriverWait(driver=_we.parent, timeout=2)

    # def scroll_until_clickable_and_click(self) -> bool:
    #     clicked = False
    #     iterations = 1
    #     # wait until the page has loaded after the successful click
    #     wait = WebDriverWait(driver=self.parent, timeout=10)
    #     self.scroll_into_view()
    #     # find screen current height
    #     window_height = self.parent.get_window_size()['height']
    #     _p = 0.4
    #     # scroll towards bottom of the screen - if the element is possibly obscured by the header
    #     # if self.location_once_scrolled_into_view['y'] > window_height*p:
    #     direction = -1
    #     # if self.location_once_scrolled_into_view['y'] < window_height*(1.0-_p):
    #     # if window_height*_p < self.location_once_scrolled_into_view['y']:
    #     # if the element is below 40% of the screen - scroll down
    #     if window_height*_p < self.location_once_scrolled_into_view['y']:
    #         direction = 1
    #
    #     iteration_limit = 51.0
    #
    #     while (not clicked) and (iterations < iteration_limit):
    #         clicked = self.try_click(iterations, iteration_limit)
    #         if clicked:
    #             wait.until(method=eec.PageIsReady())
    #             return True
    #         else:
    #             self.scroll_by(y=direction*int(window_height*iterations/iteration_limit))
    #             iterations += 1
    #
    #     self.make_screenshot(test_name="", step_number=0, step_description="Element obscured")
    #     return False
    #
    # def try_click(self, iterator, limit):
    #     try:
    #         self.click()
    #         print("Click on {0} performed.".format(self.locator.value))
    #         return True
    #
    #     except (ElementClickInterceptedException, WebDriverException):
    #         p_w("Click unsuccessful! Element was obscured. Attempt {0}/{1}".format(iterator, limit))
    #         return False
    #
    # def scroll_by(self, y: int=0):
    #     self.parent.execute_script("window.scrollTo(0, "+str(self.current_scroll_height+y)+")")