from selenium.webdriver.remote.webelement import WebElement


class MyWebElement(WebElement):
    def __init__(self, _we: WebElement):
        super().__init__(parent=_we.parent, id_=_we.id)

    @property
    def good_text(self) -> str:
        _text = self.text
        if _text is not None and _text is not '':
            return _text

        _value = self.value
        if _value is not None and _value is not '':
            return _value

        return ''

    @property
    def value(self) -> str:
        _value_by_attribute = self.get_attribute('value')
        _value_by_property = self.get_property('value')

        if _value_by_attribute is not None and _value_by_attribute is not '':
            return _value_by_attribute

        if _value_by_property is not None and _value_by_property is not '':
            return _value_by_property

        return ''

    def scroll_into_view(self):
        self.parent.execute_script("return arguments[0].scrollIntoView(true);", self)

    @property
    def current_scroll_height(self):
        return self.parent.execute_script("return window.pageYOffset")
