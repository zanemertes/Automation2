# TODO: Turn on email verification
from selenium.webdriver.support.select import Select
from copy import deepcopy
from pages.OnlineAssistent.Recomendation import RecomendationPage
from selenium.webdriver.remote.webelement import WebElement
from elements.myselect import MySelect
from DataObjects.Users import OnlineAssistanceUsers


class BeratungPage(RecomendationPage):
    my_url = "/beratung"
    _PHONE = 'phone'
    _INTEREST = 'ich interesiere mich für'
    _APPOINTMENTDATE = 'appointment date'

    locators = deepcopy(RecomendationPage.locators)
    locators.update({_PHONE:
                     './/input[@formcontrolname="phoneNumber"]',
                     _INTEREST:
                     './/select[@formcontrolname="interest"]',
                     _APPOINTMENTDATE:
                     './/select[@formcontrolname="appointmentDate"]'
                     }/ergebnis)

    @property
    def phone_field(self) -> WebElement:
        return self.body.find_element_by_xpath(self.locators[self._PHONE])

    @property
    def interest_select(self) -> MySelect:
        return MySelect(_we=self.body.find_element_by_xpath(self.locators[self._INTEREST]))

    @property
    def appoinment_date_select(self) -> Select:
        return Select(self.body.find_element_by_xpath(self.locators[self._APPOINTMENTDATE]))

    def asserting_if_correctly_prefilled(self, user: OnlineAssistanceUsers):

        # condition_future = nd > d - relativedelta(days=0)
        # condition_too_young = d - relativedelta(days=0) >= nd > d - relativedelta(years=18)
        # condition_ok = d - relativedelta(years=18) >= nd > d - relativedelta(years=39)
        # condition_too_old = d - relativedelta(years=39) >= nd > d - relativedelta(years=99)
        # condition_archaeology = d - relativedelta(years=99) > nd
        #
        # if condition_future:
        #     print("Age test: future")
        #     self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, self.locators['validation'])))
        #     assert self.validation.text == "Du kannst dich erst ab 18 allein versichern!"
        #     print("SUCCESS")
        #     return False
        #
        # condition_name = RecomendationPage.name_field.text == user_of_choice.name

        name_expected = user.name
        name_actual = self.name_field.good_text

        surname_expected = user.surname
        surname_actual = self.surname_field.good_text

        email_expected = user.email
        email_actual = self.email_field.good_text

        interest_expected = user.interested_in
        interest_actual = self.interest_select.first_selected_option.text

        print("Checking if {} == {}".format(name_expected, name_actual))
        assert name_expected == name_actual
        print("Name correct!")

        print("Checking if {} == {}".format(surname_expected, surname_actual))
        assert surname_expected == surname_actual
        print("Surname correct!")

        print("Checking if {} == {}".format(email_expected, email_actual))
        assert email_expected == email_actual
        print("Email correct!")

        print("DEBUG : income = {}".format(user.income))

        print("Checking if {} == {}".format(interest_expected, interest_actual))
        assert interest_expected == interest_actual
        print("Interest correct!")
