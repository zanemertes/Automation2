from datetime import datetime
import requests
from os import environ


E_TEST = 'test'
E_STAGING = 'staging'
C_EXPAT_IDD_CONSULTATION = 'expat-idd-consultation'
services_url = 'https://services-test.on.ag'

appointment_api_key = {E_STAGING: environ["EXPATS_STAGING_CALENDAR_API_KEY"]}


class Appointment(object):
    from datetime import datetime
    # TODO: Implement the %z/%Z parameter correctly (UTC offset - https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
    _date_time_read_formatting = "%Y-%m-%dT%H:%M:00+02:00"
    _date_time_write_formatting = "%Y-%m-%dT%H:%M:00+02:00"

    def __init__(self, a: dict):
        self._full_dictionary = a
        self.start_dt = datetime.strptime(a['start'], self._date_time_read_formatting)
        self.end_dt = datetime.strptime(a['end'], self._date_time_read_formatting)

    @property
    def start(self) -> str:
        return self.start_dt.strftime(self._date_time_write_formatting)

    @property
    def end(self) -> str:
        return self.end_dt.strftime(self._date_time_write_formatting)

    def print_properties(self):
        print("Start:     {0}\n"
              "End:       {1}".format(self.start_dt.strftime(self._date_time_write_formatting),
                                      self.end_dt.strftime(self._date_time_write_formatting)))


def get_expat_appointments_via_api(days: int) -> [Appointment]:
    """
        Gets available appointment slots in the Outlook Calendar of choice.
        Since the appointments are NOT yet booked, the typical 'OutlookAppointment' parameters are not present/set yet
        The only available ones are 'start_date' and 'end_date'
    :param days:
        is the amount of WORKING (?) days from .today() (presumably) for which the available appointments will be
        retrieved
 
    :return:
        list of Appointment() instances
    """

    if days not in range(0, 10):
        print("The amount of days '{0}' is not supported".format(days))
        raise ValueError

    calendar = C_EXPAT_IDD_CONSULTATION
                
    _target_url = "{services}/appointment/appointments?days={days}&calendar={calendar}".format(
        services=services_url, days=days, calendar=calendar)
    _expected_response = 200
    print("\tGetting the appointments via API from {days} days\nEndpoint: {target_url}".format(
        target_url=_target_url,
        days=days))

    headers = {
        'Accept': 'application/json',
        'X-Api-Key': '{api_key}'.format(api_key=appointment_api_key[E_STAGING].replace("\\", ""))
    }

    r = requests.get(_target_url, headers=headers)

    if r.status_code is not _expected_response:
        print("The response code was NOT '{0}': {1}".format(_expected_response, r.status_code))
        print("Response content: {0}".format(r.content))
        raise ValueError
    else:
        print("Request response OK. Got appointments...")

    rj = r.json()

    _key = 'result'
    if _key not in rj:
        print("{0} not found in the response dictionary".format(_key))
        raise ValueError

    appointments_list = []
    for list_element in rj[_key]:
        appointments_list.append(Appointment(a=list_element))

    return appointments_list


def appointments_before_limit(bla: [Appointment], dt_limit: datetime) -> [Appointment]:
    foo = []
    for item in bla:
        if item.end_dt < dt_limit:
            foo.append(item)
    return foo


def book_expat_appointment(appointment: Appointment):
    """): #

    :return:
    """
    # curl {services}/lead/consultation
    # - H 'Accept: application/json, text/javascript, */*; q=0.01'
    # - H 'Referer: https://test.on.ag/expats'
    # - H 'Origin: https://test.on.ag' \
    # - H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    # - H 'Content-Type: application/json; charset=UTF-8' - -data - binary
    # '{"contactDetails":
    #      {"firstName":"de",
    #      "lastName":"de",
    #      "email":"zmertes@on-testing.de",
    #      "phoneNumber":"2222222222222222222222222222222",
    #      "birthday":"1988-02-21",
    #      "nationality":"German",
    #      "interest":"comprehensive-expat"},
    #   "calendar":"expat-idd-consultation",
    #   "appointment":{"start":"2019-05-22T10:30:00+02:00","end":"2019-05-22T11:00:00+02:00"}}' - -compressed

    calendar = C_EXPAT_IDD_CONSULTATION
    _action_name = "Booking appointment"

    _target_url = "{services}/lead/consultation".format(
        services=services_url)
    _expected_response = 200
    print("\t{action} {start} via API\nEndpoint: {url}".format(
        action=_action_name,
        url=_target_url,
        start=appointment.start))

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Api-Key': '{api_key}'.format(api_key=appointment_api_key[E_STAGING].replace("\\", ""))
    }

    # body = {
    #     "contactDetails":
    #         {
    #             "firstName": "de",
    #             "lastName": "de",
    #             "email": "zmertes@on-testing.de",
    #             "phoneNumber": "2222222222222222222222222222222",
    #             "birthday": "1988-02-21",
    #             "nationality": "German",
    #             "interest": "comprehensive-expat"
    #         },
    #     "calendar": calendar,
    #     "appointment":
    #         {
    #             "start": "2019-07-03T16:30:00+02:00",
    #             "end": "2019-07-03T17:00:00+02:00"
    #         }
    # }

    body = {
        "contactDetails":
            {
                "firstName": "de",
                "lastName": "de",
                "email": "zmertes@on-testing.de",
                "phoneNumber": "2222222222222222222222222222222",
                "birthday": "1988-02-21",
                "nationality": "German",
                "interest": "comprehensive-expat"
            },
        "calendar": calendar,
        "appointment":
            {
                "start": appointment.start,
                "end": appointment.end
            }
    }

    r = requests.post(_target_url, json=body, headers=headers)

    if r.status_code is not _expected_response:
        print("The response code was NOT '{0}': {1}".format(_expected_response, r.status_code))
        print("Response content: {0}".format(r.content))
        raise ValueError
    else:
        print("Request response OK. {action}\n".format(action=_action_name))

    rj = r.json()

    # _key = 'result'
    # if _key not in rj:
    #     print("{0} not found in the response dictionary".format(_key))
    #     raise ValueError
    return rj
#from BE_Requests.ExpatCalendarFilling import book_a_specific_expat_appointment
#resp = book_a_specific_expat_appointment()

def book_a_specific_expat_appointment(start: datetime, end: datetime):
    """:( ): #

    :return:
    """
    # curl {services}/lead/consultation
    # - H 'Accept: application/json, text/javascript, */*; q=0.01'
    # - H 'Referer: https://test.on.ag/expats'
    # - H 'Origin: https://test.on.ag' \
    # - H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    # - H 'Content-Type: application/json; charset=UTF-8' - -data - binary
    # '{"contactDetails":
    #      {"firstName":"de",
    #      "lastName":"de",
    #      "email":"zmertes@on-testing.de",
    #      "phoneNumber":"2222222222222222222222222222222",
    #      "birthday":"1988-02-21",
    #      "nationality":"German",
    #      "interest":"comprehensive-expat"},
    #   "calendar":"expat-idd-consultation",
    #   "appointment":{"start":"2019-05-22T10:30:00+02:00","end":"2019-05-22T11:00:00+02:00"}}' - -compressed

    calendar = C_EXPAT_IDD_CONSULTATION
    _action_name = "Booking appointment"

    _target_url = "{services}/lead/consultation".format(
        services=services_url)
    _expected_response = 200
    print("\t{action} {start} via API\nEndpoint: {url}".format(
        action=_action_name,
        url=_target_url,
        start=str(start)))
        #start=appointment.start))

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Api-Key': '{api_key}'.format(api_key=appointment_api_key[E_STAGING].replace("\\", ""))
    }

    # body = {
    #     "contactDetails":
    #         {
    #             "firstName": "de",
    #             "lastName": "de",
    #             "email": "zmertes@on-testing.de",
    #             "phoneNumber": "2222222222222222222222222222222",
    #             "birthday": "1988-02-21",
    #             "nationality": "German",
    #             "interest": "comprehensive-expat"
    #         },
    #     "calendar": calendar,
    #     "appointment":
    #         {
    #             "start": "2019-07-03T16:30:00+02:00",
    #             "end": "2019-07-03T17:00:00+02:00"
    #         }
    # }

    body = {
        "contactDetails":
            {
                "firstName": "de",
                "lastName": "de",
                "email": "zmertes@on-testing.de",
                "phoneNumber": "2222222222222222222222222222222",
                "birthday": "1988-02-21",
                "nationality": "German",
                "interest": "comprehensive-expat"
            },
        "calendar": calendar,
        "appointment":
            {
                "start": str(start),
                "end": str(end)
            }
    }

    r = requests.post(_target_url, json=body, headers=headers)

    if r.status_code is not _expected_response:
        print("The response code was NOT '{0}': {1}".format(_expected_response, r.status_code))
        print("Response content: {0}".format(r.content))
        raise ValueError
    else:
        print("Request response OK. {action}\n".format(action=_action_name))

    rj = r.json()

    # _key = 'result'
    # if _key not in rj:
    #     print("{0} not found in the response dictionary".format(_key))
    #     raise ValueError
    return rj


def book_appointments_until_limit(limit: datetime):
    appointments = appointments_before_limit(bla=get_expat_appointments_via_api(days=(limit - datetime.now()).days),
                                             dt_limit=limit)
    for item in appointments:
        book_expat_appointment(item)


def book_appointments_until_limit_except_last(limit: datetime):
    appointments = appointments_before_limit(bla=get_expat_appointments_via_api(days=(limit - datetime.now()).days),
                                             dt_limit=limit)
    for item in appointments[:-1]:
        book_expat_appointment(item)


def delete_specific_expat_appointment(appID: str):
    """

    :return:
    """
    # curl {services}/lead/consultation
    # - H 'Accept: application/json, text/javascript, */*; q=0.01'
    # - H 'Referer: https://test.on.ag/expats'
    # - H 'Origin: https://test.on.ag' \
    # - H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    # - H 'Content-Type: application/json; charset=UTF-8' - -data - binary
    # '{"contactDetails":
    #      {"firstName":"de",
    #      "lastName":"de",
    #      "email":"zmertes@on-testing.de",
    #      "phoneNumber":"2222222222222222222222222222222",
    #      "birthday":"1988-02-21",
    #      "nationality":"German",
    #      "interest":"comprehensive-expat"},
    #   "calendar":"expat-idd-consultation",
    #   "appointment":{"start":"2019-05-22T10:30:00+02:00","end":"2019-05-22T11:00:00+02:00"}}' - -compressed
    #'AAMkAGVjZDcyZDc4LWU1NDctNGMxZi05ZGIyLWE4ZTM1YTBjZmZhZABGAAAAAAA3AHz-pxYmToTOZAhq8kzQBwBtXs5r8ZXXTrSjyNYtKiMgAAAAAAENAABtXs5r8ZXXTrSjyNYtKiMgAACgCyT3AAA='

    # curl -X DELETE "https://services-test.on.ag/appointment/appointments" -H  "accept: application/json" -H  "X-Api-Key: NwrvnsQMo&Gk^6vbTDAe9FaLTt;ZPnNjcyhGZ" -H  "Content-Type: application/json" -d "calendar: expat-idd-consultation" -d "id: AAMkAGVjZDcyZDc4LWU1NDctNGMxZi05ZGIyLWE4ZTM1YTBjZmZhZABGAAAAAAA3AHz-pxYmToTOZAhq8kzQBwBtXs5r8ZXXTrSjyNYtKiMgAAAAAAENAABtXs5r8ZXXTrSjyNYtKiMgAACQMCFUAAA="

    calendar = C_EXPAT_IDD_CONSULTATION

    _target_url = "{services}/appointment/appointments".format(services=services_url)
    #_target_url = "http://appointment.services.localhost/appointments".format(services=services_url)

    _expected_response = 200
    print("\tStarting get appointments via API\nEndpoint: {0}".format(_target_url))

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Api-Key': '{api_key}'.format(api_key=appointment_api_key[E_STAGING].replace("\\", "")),
        'cache-control': 'no-cache'
    }

    body = {
        "id": str(appID),
        "calendar": calendar
    }

 # 'AAMkAGVjZDcyZDc4LWU1NDctNGMxZi05ZGIyLWE4ZTM1YTBjZmZhZABGAAAAAAA3AHz-pxYmToTOZAhq8kzQBwBtXs5r8ZXXTrSjyNYtKiMgAAAAAAENAABtXs5r8ZXXTrSjyNYtKiMgAACrrz3GAAA='

    r = requests.delete(_target_url, json=body, headers=headers)

    if r.status_code is not _expected_response:
        print("The response code was NOT '{0}': {1}".format(_expected_response, r.status_code))
        print("Response content: {0}".format(r.content))
        raise ValueError
    else:
        print("Appointment deleted")

def delete_expat_appointment():
        """

        :return:
        """
        # curl {services}/lead/consultation
        # - H 'Accept: application/json, text/javascript, */*; q=0.01'
        # - H 'Referer: https://test.on.ag/expats'
        # - H 'Origin: https://test.on.ag' \
        # - H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        # - H 'Content-Type: application/json; charset=UTF-8' - -data - binary
        # '{"contactDetails":
        #      {"firstName":"de",
        #      "lastName":"de",
        #      "email":"zmertes@on-testing.de",
        #      "phoneNumber":"2222222222222222222222222222222",
        #      "birthday":"1988-02-21",
        #      "nationality":"German",
        #      "interest":"comprehensive-expat"},
        #   "calendar":"expat-idd-consultation",
        #   "appointment":{"start":"2019-05-22T10:30:00+02:00","end":"2019-05-22T11:00:00+02:00"}}' - -compressed

        # curl - X DELETE "https://services-test.on.ag/appointment/appointments" - H "accept: application/json" - H "Content-Type: application/json" - d "underwriting"

        calendar = C_EXPAT_IDD_CONSULTATION

        _target_url = "{services}/appointment/appointments".format(
            services=services_url)
        _expected_response = 200
        print("\tStarting get appointments via API\nEndpoint: {0}".format(_target_url))

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json;',
            'X-Api-Key': '{api_key}'.format(api_key=appointment_api_key[E_STAGING].replace("\\", ""))
        }

        body = {
            "id": appointment['appointmentId'],
            "calendar": calendar
        }

        r = requests.delete(_target_url, json=body, headers=headers)

        if r.status_code is not _expected_response:
            print("The response code was NOT '{0}': {1}".format(_expected_response, r.status_code))
            print("Response content: {0}".format(r.content))
            raise ValueError
        else:
            print("Appointment deleted")

    #rj = r.json()

    # _key = 'result'
    # if _key not in rj:
    #     print("{0} not found in the response dictionary".format(_key))
    #     raise ValueError

    #return rj

# Data
# from requests import request
# url = "https://services-test.on.ag/appointment/appointments?days={days}&calendar=expat-idd-consultation".format(days=5)
# import requests
# response = requests.get(url, headers=header)
# rf = response.json()
# class Appointment(object):
#     # TODO: Implement the %z/%Z parameter correctly (UTC offset - https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
#     _date_time_read_formatting = "%Y-%m-%dT%H:%M:00+02:00"
#     _date_time_write_formatting = "%Y-%m-%d %H:%M:00+02:00"
#
#     def __init__(self, a: dict):
#         self._full_dictionary = a
#         self.start_dt = datetime.strptime(a['start'], self._date_time_read_formatting)
#         self.end_dt = datetime.strptime(a['end'], self._date_time_read_formatting)
#
#     def print_properties(self):
#         print("Start:     {0}\n"
#               "End:       {1}".format(self.start_dt.strftime(self._date_time_write_formatting),
#                                       self.end_dt.strftime(self._date_time_write_formatting)))
#
#
# rf['result']
# rf['result'][0]
# class Appointment(object):
#     from datetime import datetime
#     # TODO: Implement the %z/%Z parameter correctly (UTC offset - https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
#     _date_time_read_formatting = "%Y-%m-%dT%H:%M:00+02:00"
#     _date_time_write_formatting = "%Y-%m-%d %H:%M:00+02:00"
#     def __init__(self, a: dict):
#         self._full_dictionary = a
#         self.start_dt = datetime.strptime(a['start'], self._date_time_read_formatting)
#         self.end_dt = datetime.strptime(a['end'], self._date_time_read_formatting)
#     def print_properties(self):
#         print("Start:     {0}\n"
#               "End:       {1}".format(self.start_dt.strftime(self._date_time_write_formatting),
#                                       self.end_dt.strftime(self._date_time_write_formatting)))
#
# from datetime import datetime
# a0 = Appointment(a=rf['result'][0])
# appointment_list = []
# rf['result'][0]
# {'start': '2019-05-23T10:00:00+02:00', 'end': '2019-05-23T10:30:00+02:00'}
# for item in rf['result']:
#     print(item)
#
# or item in rf['result']:
# appointment_list.append(Appointment(a=item))
#
# appointment_list[5]
# appointment_list[5].start_dt
# for appointment in appointment_list:
#     if appointment.start_dt < datetime(year=2019, month=5, day=23):
#         appointment.print_properties
#
# for appointment in appointment_list:
#     if appointment.start_dt < datetime(year=2019, month=5, day=23):
#         appointment.print_properties()
# from BE_Requests.ExpatCalendarFilling import get_expat_appointments_via_api
# bla = get_expat_appointments_via_api(days=2)
# from datetime import datetime
# dt_limit = datetime(2019,5,27,18,30,0)
# dt_limit = datetime(2019,5,25,15,30,0)
# foo = []
# for item in bla:
#    if item.end_dt<dt_limit:
#       foo.append(item)

id={}
for i in range (0,maximum):
    respp = book_a_specific_expat_appointment(start=appointmentsshort[i]["start"], end=appointmentsshort[i]["end"])
    id["appID{nr}".format(nr=i)] = respp["appointmentId"]
