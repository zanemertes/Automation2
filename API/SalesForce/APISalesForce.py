import requests
from os import environ
import re
from datetime import datetime
#import Acq119

E_TEST = 'test'
E_STAGING = 'staging'
C_EXPAT_IDD_CONSULTATION = 'expat-idd-consultation'
services_url = 'https://services-test.on.ag'
_appointment_api_key = {E_TEST: environ['APPOINTMENT_API_KEY_TEST'],
                        E_STAGING: environ['APPOINTMENT_API_KEY_STAGING']}

class Appointment(object):
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

    #def print_properties(self):
    #   log("Start:     {0}\n"
    #       "End:       {1}".format(self.start_dt.strftime(self._date_time_write_formatting),
    #                               self.end_dt.strftime(self._date_time_write_formatting)))

def info_according_to_the_name(name: str) -> dict:
    access_token, instance_url = login_salesforce_rest()
    leads_url = leads_records_by_name(name=name)

    target_url = "{instance_url}{leads_url}". format(instance_url=instance_url, leads_url=leads_url)
    header = {"Authorization": "Bearer {token}".format(token=access_token)}
    response_leads_data = requests.get(target_url, headers=header)
    dict_json = response_leads_data.json()
    # return dict_json
    CBname = dict_json["Name"]
    CBphone = dict_json["Phone"]
    CBappointment = dict_json["Vertriebsberatungstermin__c"]
    return CBname, CBphone, CBappointment

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

    _target_url = "{services}/appointment/appointments/public?days={days}&calendar={calendar}".format(
        services=services_url, days=days, calendar=calendar)
    _expected_response = 200
    print("\tGetting the appointments via API from {days} days\nEndpoint: {target_url}".format(
        target_url=_target_url,
        days=days))

    headers = {
        'Accept': 'application/json',
        'X-Api-Key': '{api_key}'.format(api_key=_appointment_api_key[E_STAGING].replace("\\", ""))
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
        print(list_element)
        #appointments_list.append(Appointment(a=list_element))
        appointments_list.append(list_element)

    return appointments_list

def login_salesforce_rest():
    url = "https://test.salesforce.com/services/oauth2/token"
    parameters = {"format": "json",
                  "grant_type": "password",
                  "client_id": environ["SALESFORCE_CLIENT_ID"],
                  "client_secret": environ["SALESFORCE_CLIENT_SECRET"],
                  "password": environ["SALESFORCE_PASSWORD"]+environ["SALESFORCE_SECURITY_TOKEN"],
                  "username": environ["SALESFORCE_USERNAME"]}
    response_login = requests.post(url, parameters)

    dict_json = response_login.json()
    access_token = dict_json["access_token"]
    instance_url = dict_json["instance_url"]

    return access_token, instance_url

def services_version():
# curl https://yourInstance.salesforce.com/services/data/
    access_token, instance_url = login_salesforce_rest()
    url = instance_url+"/services/data/"
    print(url)
    response_services = requests.get(url)
    dict_json = response_services.json()
    url = dict_json[-1]["url"]
    return url


def get_records_by_query(query: str):
    from urllib.parse import urlencode

    access_token, instance_url = login_salesforce_rest()

    # curl https://yourInstance.salesforce.com/services/data/v20.0/query/?q=SELECT+name+from+Account -H "Authorization: Bearer token"
    target_url = "{instance}{version}/{endpoint}?{encoded_parameters}".format(
        instance=instance_url,
        version=services_version(),
        endpoint="query",
        encoded_parameters=urlencode({
            "q":
            query})
        )

    header = {"Authorization": "Bearer {token}".format(token=access_token)}
    response_lead = requests.get(target_url, headers=header)
    dict_json = response_lead.json()

    return dict_json


def leads_records_by_email(email: str):
    from urllib.parse import urlencode

    access_token, instance_url= login_salesforce_rest()
    #curl https://yourInstance.salesforce.com/services/data/v20.0/query/?q=SELECT+name+from+Account -H "Authorization: Bearer token"
    target_url = "{instance}{version}/{endpoint}?{encoded_parameters}".format(
        instance=instance_url,
        version=services_version(),
        endpoint="query",
        encoded_parameters=urlencode({
            "q":
            "SELECT name, Email from Lead WHERE Email = '{0}'".format(email)})
        )

    header = {"Authorization": "Bearer {token}".format(token=access_token)}

    response_lead = requests.get(target_url, headers=header)
    dict_json = response_lead.json()
    url = dict_json["records"][0]["attributes"]["url"]

    return url

    # return get_records_by_query(query="SELECT name, Email from Lead WHERE Email = '{0}'".format(email))
    # response_email = get_records_by_query(query="SELECT name, Email from Lead WHERE Email = '{0}'".format(email))

def leads_records_by_name(name: str):
    from urllib.parse import urlencode

    access_token, instance_url= login_salesforce_rest()
    #curl https://yourInstance.salesforce.com/services/data/v20.0/query/?q=SELECT+name+from+Account -H "Authorization: Bearer token"
    target_url = "{instance}{version}/{endpoint}?{encoded_parameters}".format(
        instance=instance_url,
        version=services_version(),
        endpoint="query",
        encoded_parameters=urlencode({
            "q":
            "SELECT Name from Lead WHERE Name = '{0}'".format(name)})
        )

    header = {"Authorization": "Bearer {token}".format(token=access_token)}

    response_lead = requests.get(target_url, headers=header)
    dict_json = response_lead.json()
    url = dict_json["records"][0]["attributes"]["url"]

    return url

def info_according_to_the_email(email = str) -> dict:
    access_token, instance_url = login_salesforce_rest()
    email = "zmertes+delete@on-testing.de" # TODO:Adjust according to the UserEmail
    leads_url = leads_records_by_email(email=email)
    target_url = "{instance_url}{leads_url}". format(instance_url=instance_url, leads_url=leads_url)
    header = {"Authorization": "Bearer {token}".format(token=access_token)}
    response_leads_data = requests.get(target_url, headers=header)
    dict_json = response_leads_data.json()
    id = dict_json["Lead_ID__c"]
    return id
    #empfohlenes_tarif = dict_json["Empfohlener_Tarif__c"]
    #last_name = dict_json["LastName"]
    #first_name = dict_json["FirstName"]

    #return empfohlenes_produkt, empfohlenes_tarif, last_name, first_name

def deleting_according_to_the_id():
    #curl -X DELETE "https://services-test.on.ag/appointment/appointments" -H  "accept: application/json" -H  "Content-Type: application/json" -d "expat-idd-consultation"
    access_token, instance_url = login_salesforce_rest()
    id = info_according_to_the_email()
    target_url = "{instance_url}{leads_url}".format(instance_url=instance_url, leads_url=leads_url)
    header = {"Authorization": "Bearer {token}".format(token=access_token)}
    response_leads_data = requests.get(target_url, headers=header)



def info_according_to_the_name(name: str) -> dict:
    access_token, instance_url = login_salesforce_rest()
    leads_url = leads_records_by_name(name=name)
    target_url = "{instance_url}{leads_url}". format(instance_url=instance_url, leads_url=leads_url)
    header = {"Authorization": "Bearer {token}".format(token=access_token)}
    response_leads_data = requests.get(target_url, headers=header)
    dict_json = response_leads_data.json()
    # return dict_json
    CBname = dict_json["Name"]
    CBphone = dict_json["Phone"]
    CBappointment = dict_json["Vertriebsberatungstermin__c"]
    return CBname, CBphone, CBappointment


    # empfohlenes_tarif = dict_json["Empfohlener_Tarif__c"]
    # last_name = dict_json["LastName"]
    # first_name = dict_json["FirstName"]



    #return empfohlenes_produkt, empfohlenes_tarif, last_name, first_name

#print(info_according_to_the_email())


#
#
#


def bartosz_leads_records_by_email(email: str):
    return get_records_by_query(query="SELECT name, Email from Lead WHERE Email = '{0}'".format(email))


class AllAttributesOfLeads(object):
    def __init__(self):
        print("All attributes!")


def saving_all_attributes_as_variables() -> AllAttributesOfLeads:
    all_attributes = AllAttributesOfLeads()
    info_leads = info_according_to_the_email()
    for key, value in info_leads.items():
        all_attributes.__setattr__(key, value)
    return all_attributes


def accounts_records_by_email(email: str):
    return get_records_by_query(query="SELECT name, PersonEmail from Account WHERE PersonEmail = '{0}'".format(email))


def get_account_url(leads_dict: dict, record_number: int):
    print(leads_dict["records"])
    return leads_dict["records"][record_number]["attributes"]["url"]

# def get_account_url(leads_dict: dict, email: Acq230.user_of_choice.email):
#     return leads_dict["records"][record_number]["attributes"]["url"]
#     # curl https://yourInstance.salesforce.com/services/data/v46.0/sobjects/Account/0011q00000Edcw9AAB -H "Authorization: Bearer token"


def getting_account_info(account_url: str):
    access_token, instance_url = login_salesforce_rest()
    target_url = "{instance_url}{account_url}".format(
        instance_url=instance_url,
        account_url=account_url
    )

    header = {"Authorization": "Bearer {token}".format(token=access_token)}
    lead_account = requests.get(target_url, headers=header)
    dict_json = lead_account.json()
    return dict_json



# from API.SalesForce.APISalesForce import leads_records_by_email
# email="zmertes+angestellter-1557824427@on-testing.de"
# leads = leads_records_by_email(email=email)

def login_soap():
    host_name = "cs107.salesforce.com"
    Session_ID = "00D1q0000008cBo!AQgAQEiTOQOekvpWsr.37f9hgZp_N5qi161qnBUDi_6x__vIqwpIyoiyejATpNyr1v1GYaG1zClSdOpJ3qu8R5ncfMQnxxgX"
    Server_Url = "https://cs107.salesforce.com/services/Soap/u/45.0/00D1q0000008cBo"

    # curl https://test.salesforce.com/services/Soap/u/45.0 -H "Content-Type: text/xml; charset=UTF-8" -H "SOAPAction: login" -d @login.txt

    # Requests have body, header, url, request type
    # Main reaquest types: GET, POST, DELETE, UPDATE
    # Soap (Simple Object Access Protocol) and Rest languages for Accessing data
    # Http responses 200 (good), 400 (bad, but just an error), 500 (very bad, server crashed)
    # Header (what i will send, and what i expect to get back),
    #                       Content-Type: - how i will send the data
    #                       Accept - how i want to receive it
    # defines: - how the communication will be structured: text,
    #          - language (e.g. xml (extended markup language), json, html,),
    #          - encoding (e.g. charset=UTF-8)


    request_type = "GET"  # need to try out
    url = "https://test.salesforce.com/services/Soap/u/45.0"
    header = {"Content-Type": "text/xml",
         "charset": "UTF-8",
         "SOAPAction": "login"}
    body = """<?xml version="1.0" encoding="utf-8" ?>
    <env:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
    <env:Body>
    <n1:login xmlns:n1="urn:partner.soap.sforce.com">
    <n1:username>{username}</n1:username>)
    <n1:password>{password}{token}</n1:password>
    </n1:login>
    </env:Body>
    </env:Envelope>"""

    body = body.format(username=environ["SALESFORCE_USERNAME"],
                   password=environ["SALESFORCE_PASSWORD"],
                   token=environ["SALESFORCE_TOKEN"])

    response = requests.post(url, body, headers=header)

    # parameterized_string = "my_login={login};my_password={password}"
    # print(parameterized_string)
    # my_login={login};my_password={password}
    # print(parameterized_string.format(login="bchmura", password="MySuperSecretPassword"))
    # my_login=bchmura;my_password=MySuperSecretPassword

    import xml.dom.minidom
    x = xml.dom.minidom.parseString(response.text)
    session_id_element = x.getElementsByTagName("sessionId")  # get all matching elements with 'sessionId' tag
    session_id_element = x.getElementsByTagName("sessionId")[0]  # get just the first matching element with 'sessionId' tag
    session_id_element_xml = session_id_element.toxml()  # convert Element to XML

    session_id = element_value_from_xml(element_name="sessionId", xml_stuff=x)
    url = element_value_from_xml(element_name="serverUrl", xml_stuff=x)
    print(url)
    url_regex = '//(.*?)/'
    host_name_results = re.findall(url_regex, url)

    print(host_name_results[0])

def element_value_from_xml(element_name: str, xml_stuff):
    return xml_stuff.getElementsByTagName(element_name)[0].toxml().replace("<{}>".format(element_name), "")

