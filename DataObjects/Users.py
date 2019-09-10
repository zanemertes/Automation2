from datetime import date, datetime
from random import randint


class OnlineAssistanceUsers(object):
    OA_OCCUPATION_EMPLOYEE = "Angestellter"
    OA_OCCUPATION_SELF_EMPLOYED = "Selbstständig"
    OA_OCCUPATION_CIVIL_SERVANT = "Beamter"
    OA_OCCUPATION_CIVIL_SERVANT_APPLICANT = "Beamtenanwärter"
    OA_OCCUPATION_STUDENT = "Student oder in Ausbildung"
    OA_ALLOWED_OCCUPATIONS = [OA_OCCUPATION_STUDENT,
                              OA_OCCUPATION_CIVIL_SERVANT,
                              OA_OCCUPATION_CIVIL_SERVANT_APPLICANT,
                              OA_OCCUPATION_SELF_EMPLOYED,
                              OA_OCCUPATION_EMPLOYEE]

    OA_PREVIOUS_INSURANCE_PRIVATE = "privat"
    OA_PREVIOUS_INSURANCE_GOVERN = "gesetzlich"
    OA_ALLOWED_PREVIOUS_INSURANCE_TYPE = [OA_PREVIOUS_INSURANCE_PRIVATE,
                                          OA_PREVIOUS_INSURANCE_GOVERN]

    OA_INTEREST_ALLGEMEINE_BERATUNG = "Allgemeine Beratung"
    OA_INTEREST_FULL_INSURANCE = "Krankenvollversicherung"
    OA_INTEREST_CIVIL_INSURANCE = "Beihilfeversicherung"
    OA_INTEREST_DENTAL_TOPUP = "Zahnzusatzversicherung"
    OA_INTEREST_CLINIC_TOPUP = "Krankenhauszusatzversicherung"

    OA_ALLOWED_INTEREST_TYPES = [OA_INTEREST_ALLGEMEINE_BERATUNG,
                                 OA_INTEREST_FULL_INSURANCE,
                                 OA_INTEREST_CIVIL_INSURANCE,
                                 OA_INTEREST_DENTAL_TOPUP,
                                 OA_INTEREST_CLINIC_TOPUP]


    OA_JA = "Ja"
    OA_NEIN = "Nein"
    OA_ALLOWED_CS_APPLICANT = [OA_JA,
                               OA_NEIN]

    OA_BIRTHDAY = "birthday"
    OA_BIRTHMONTH = "birthmonth"
    OA_BIRTHYEAR = "birthyear"

    _income_limit = 60750

    __occupation = None
    __income = None
    __interested_in = None

    def __init__(self,
                 date_of_birth: date,
                 _occupation: str,
                 name: str = "Zane",
                 surname: str = "Mertes",
                 email: str or None=None,
                 _income: int or None = None,
                 _csapplicant: str or None = None,
                 previous_insurance: str = OA_PREVIOUS_INSURANCE_GOVERN,
                 price_choice: int = 0,
                 ):
        self.name = name
        self.surname = surname
        self.email = email
        # occupation  MUST be before income - see setter of income
        self.occupation = _occupation
        self.income = _income
        # this needs both: self.occupation and self.income
        self.calculate_interest()
        self.previous_insurance = previous_insurance
        self.price_choice = price_choice
        self.date_of_birth = date_of_birth
        self.csapplicant = _csapplicant

    def print_yer_guts(self):
        print("occupation = {}".format(self.occupation))
        print("income = {}".format(self.income))
        print("interested in = {}".format(self.interested_in))
        print("first name = {}".format(self.name))
        print("last name = {}".format(self.surname))

    @property
    def interested_in(self):
        return self.__interested_in

    @property
    def occupation(self):
        return self.__occupation

    @occupation.setter
    def occupation(self, occupation_name: str):
        # if the occupation is valid
        if occupation_name in self.OA_ALLOWED_OCCUPATIONS:
            self.__occupation = occupation_name
            # if the email was not given - then make one from the occupation name + timestamp
            if self.email is None and occupation_name == self.OA_OCCUPATION_STUDENT:
                self.email = "zmertes+Student-{0}@on-testing.de".format(str(int(datetime.timestamp(datetime.now()))))
            elif self.email is None and occupation_name == self.OA_OCCUPATION_SELF_EMPLOYED:
                self.email = "zmertes+SelfEmployed-{0}@on-testing.de".format(str(int(datetime.timestamp(datetime.now()))))
            elif self.email is None and occupation_name == self.OA_OCCUPATION_CIVIL_SERVANT_APPLICANT:
                self.email = "zmertes+CsApplicant-{0}@on-testing.de".format(str(int(datetime.timestamp(datetime.now()))))
            elif self.email is None:
                self.email = "zmertes+{0}-{1}@on-testing.de".format(occupation_name,
                                                                  str(int(datetime.timestamp(datetime.now()))))

        # else scream
        else:
            print('occupation name "{0}" not defined'.format(occupation_name))
            raise ValueError

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, income_value: int or None):
        if self.occupation == self.OA_OCCUPATION_EMPLOYEE and income_value is None:
            print("missing income for employee")
            raise ValueError
        else:
            self.__income = income_value

    @staticmethod
    def generate_random_income(rich: bool):
        if rich:
            return randint(OnlineAssistanceUsers._income_limit, 10 * OnlineAssistanceUsers._income_limit)
        else:
            return randint(0, OnlineAssistanceUsers._income_limit)

    def calculate_interest(self):
        # if employee...:
        if self.occupation == self.OA_OCCUPATION_EMPLOYEE and self.income >= 60750:
 #           # ... is rich
  #          if self.income > 60750:
                self.__interested_in = self.OA_INTEREST_FULL_INSURANCE
            # ... is poor:
        elif self.occupation == self.OA_OCCUPATION_EMPLOYEE and self.income < 60750:
                self.__interested_in = self.OA_INTEREST_DENTAL_TOPUP
        # if selbst.:
        elif self.occupation == self.OA_OCCUPATION_SELF_EMPLOYED:
            self.__interested_in = self.OA_INTEREST_FULL_INSURANCE
        elif self.occupation == self.OA_OCCUPATION_STUDENT:
            self.__interested_in = self.OA_INTEREST_FULL_INSURANCE
        # if beamter or beamtenanw.:
        elif self.occupation in [self.OA_OCCUPATION_CIVIL_SERVANT,
                                 self.OA_OCCUPATION_CIVIL_SERVANT_APPLICANT]:
            self.__interested_in = self.OA_INTEREST_CIVIL_INSURANCE
        # should not happen:
        else:
            raise ValueError

    @staticmethod
    def generate_random_number_of_workers(): # selbständig
        return randint(0, 1000)

    @property
    def is_user_rich(self) -> bool:
        return self.income >= self._income_limit


user_rich_employee = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE,
                                           _income=OnlineAssistanceUsers.generate_random_income(rich=True),
                                           date_of_birth=date(year=1990, month=1, day=1))

user_poor_employee = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE,
                                           _income=OnlineAssistanceUsers.generate_random_income(rich=False),
                                           date_of_birth=date(year=1990, month=1, day=1))

user_student = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_STUDENT,
                                     _csapplicant=OnlineAssistanceUsers.OA_NEIN,
                                     date_of_birth=date(year=1990, month=1, day=1))

user_self_employed = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED,
                                           _income=OnlineAssistanceUsers.generate_random_income(rich=False),
                                           date_of_birth=date(year=1990, month=1, day=1))

user_cs = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT,
                                date_of_birth=date(year=1990, month=1, day=1))

user_cs_applicant = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT_APPLICANT,
                                          date_of_birth=date(year=1990, month=1, day=1))

user_rich_employee_35yo = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE,
                                                _income=OnlineAssistanceUsers.generate_random_income(rich=True),
                                                date_of_birth=date(year=1984, month=1, day=1))

user_rich_employee_40yo = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE,
                                                _income=OnlineAssistanceUsers.generate_random_income(rich=True),
                                                date_of_birth=date(year=1979, month=1, day=1))

user_rich_employee_45yo = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE,
                                                _income=OnlineAssistanceUsers.generate_random_income(rich=True),
                                                date_of_birth=date(year=1974, month=1, day=1))

user_rich_employee_46yo = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE,
                                                _income=OnlineAssistanceUsers.generate_random_income(rich=True),
                                                date_of_birth=date(year=1973, month=1, day=1))

user_self_employed_35yo = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED,
                                                _income=OnlineAssistanceUsers.generate_random_income(rich=False),
                                                date_of_birth=date(year=1984, month=1, day=1))

user_self_employed_40yo = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED,
                                                _income=OnlineAssistanceUsers.generate_random_income(rich=False),
                                                date_of_birth=date(year=1979, month=1, day=1))

user_self_employed_45yo = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED,
                                                _income=OnlineAssistanceUsers.generate_random_income(rich=False),
                                                date_of_birth=date(year=1974, month=1, day=1))

user_self_employed_46yo = OnlineAssistanceUsers(_occupation=OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED,
                                                _income=OnlineAssistanceUsers.generate_random_income(rich=False),
                                                date_of_birth=date(year=1973, month=1, day=1))

def generate_user_by_occupation(occupation: str) -> OnlineAssistanceUsers:
    # Rich Employee
    if occupation == OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE:
        return OnlineAssistanceUsers(_occupation=occupation,
                                     _income=OnlineAssistanceUsers.generate_random_income(rich=True),
                                     date_of_birth=date(year=1990, month=1, day=1))
    # Poor Employee
    elif occupation == OnlineAssistanceUsers.OA_OCCUPATION_EMPLOYEE:
        return OnlineAssistanceUsers(_occupation=occupation,
                                     _income=OnlineAssistanceUsers.generate_random_income(rich=False),
                                     date_of_birth=date(year=1990, month=1, day=1))
    # Student
    elif occupation == OnlineAssistanceUsers.OA_OCCUPATION_STUDENT:
        return OnlineAssistanceUsers(_occupation=occupation,
                                     _csapplicant=OnlineAssistanceUsers.OA_NEIN,
                                     date_of_birth=date(year=1990, month=1, day=1))
    # Self Employed
    elif occupation == OnlineAssistanceUsers.OA_OCCUPATION_SELF_EMPLOYED:
        return OnlineAssistanceUsers(_occupation=occupation,
                                     _income=OnlineAssistanceUsers.generate_random_income(rich=False),
                                     date_of_birth=date(year=1990, month=1, day=1))
    # Civil Servant
    elif occupation == OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT:
        return OnlineAssistanceUsers(_occupation=occupation,
                                     date_of_birth=date(year=1990, month=1, day=1))
    # Civil Servant Applicant
    elif occupation == OnlineAssistanceUsers.OA_OCCUPATION_CIVIL_SERVANT_APPLICANT:
        return OnlineAssistanceUsers(_occupation=occupation,
                                     date_of_birth=date(year=1990, month=1, day=1))
    else:
        print("WHAT?")
        raise ValueError




# TODO: Fix the poor - rich employee overlapping
USERS_ALL = [user_cs_applicant,
             user_cs,
             user_rich_employee,
             user_student,
             user_self_employed
             ]

# TODO: Fix the poor - rich employee overlapping
USERS_GRUND = [user_cs_applicant,
               user_cs
               ]

USER_RECOMENDATION = [user_rich_employee_35yo,
                      user_rich_employee_40yo,
                      user_rich_employee_45yo,
                      user_rich_employee_46yo,
                      user_poor_employee,
                      user_self_employed_35yo,
                      user_self_employed_40yo,
                      user_self_employed_45yo,
                      user_self_employed_46yo
                      ]