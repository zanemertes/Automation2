from selenium.webdriver.common.by import By


class Locator(object):
    SUPPORTED_BYS = [By.ID,
                     By.XPATH,
                     By.LINK_TEXT,
                     By.PARTIAL_LINK_TEXT,
                     By.NAME,
                     By.TAG_NAME,
                     By.CLASS_NAME,
                     By.CSS_SELECTOR]

    def __init__(self,
                 value: str,
                 by: str=By.XPATH):
        if by not in self.SUPPORTED_BYS:
            raise Exception('Invalid locator')
        else:
            self.by = by
            self.value = value

    @property
    def tupled(self):
        return self.by, self.value

    def replace_value(self, old: str, new: str):
        self.value = self.value.replace(old, new)

    def concatenate(self, second: 'Locator'):
        sv = second.value
        if sv[0] == '.':
            sv = second.value[1:]
        self.value = self.value + sv
