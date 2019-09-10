import requests
import pytest
import json

_url_v17 = "https://innovas-test.backend.ottonova.de"
_url_v19 = "https://innovas-batchtest-staging.backend.ottonova.de"

_archiveDocument = "/ottonova_ws/rest/archive/ArchiveService/archiveDocument"
_upload = "/ottonova_ws/rest/imsmartfix_server/UploadService/upload"

# Execution in newman.
# Need to generate Api key for the User: https://grey-resonance-7980.postman.co/integrations/services/pm_pro_api?workspace=f30d2802-4317-417a-b3ea-6f1b3a784f20
# Provides all the collections available to the user (OWNER and ID): curl --location --request GET "https://api.getpostman.com/collections"   --header "X-Api-Key: {{generated API key}}"
# Provides all the environments available to the user (OWNER and ID): curl --location --request GET "https://api.getpostman.com/environments"   --header "X-Api-Key: {{generated API key}}"
# Terminal: newman run   https://api.getpostman.com/collections/{{collection OWNER key}}-{{collection ID key}}?apikey={{generated API key}}   --environment https://api.getpostman.com/environments/{{environment OWNER key}}-{{environment ID key}}?apikey={{generated API key}}   --reporters cli --reporter-cli-no-banner^C
# Terminal for me: newman run   https://api.getpostman.com/collections/8628119-847c6fac-6c05-463e-8ca0-11ef19535e3c?apikey=f622e02cf0d243a991fe7648c0574e6b   --environment https://api.getpostman.com/environments/1281827-fb589334-04f3-4195-812e-ad76e6976b17?apikey=f622e02cf0d243a991fe7648c0574e6b   --reporters cli --reporter-cli-no-banner^C


@pytest.mark.innovasBErequest
def test__comparison_request_innovas_v17vsV19_PING(): #YES
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaHipmOnlineService/ping"
    _name_endpoint = "POST Ping"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
        "serviceContextInfo": {
            "locale": "de",
            "mandator": 17
        }
    }

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

@pytest.mark.innovasBErequest
def test__comparison_request_innovas_v17vsV19_getInsuranceCompanyListde(): #Yes
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaHipmOnlineService/getInsuranceCompanyList"
    _name_endpoint = "POST Listing insurance companies (de)"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
      }
    }

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

@pytest.mark.innovasBErequest
def test__comparison_request_innovas_v17vsV19_getProfessionListde(): #Yes
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaHipmOnlineService/getProfessionList"
    _name_endpoint = "POST Listing professions (de)"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
      }
    }

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

@pytest.mark.innovasBErequest
def test__comparison_request_innovas_v17vsV19_getInsuranceCompanyListen(): #Yes
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaHipmOnlineService/getInsuranceCompanyList"
    _name_endpoint = "POST Listing insurance companies (en)"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
      "serviceContextInfo": {
        "locale": "en",
        "mandator": 17
      }
    }

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

@pytest.mark.innovasBErequest   #TODO: Need Fixing
def test__comparison_request_innovas_v17vsV19_getProfessionListen():
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaHipmOnlineService/getProfessionList"
    _name_endpoint = "POST Listing professions (en)"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
      "serviceContextInfo": {
        "locale": "en",
        "mandator": 17
      }
    }

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

@pytest.mark.innovasBErequest
def test__comparison_request_BEK_innovas_v17vsV19_calculatNewIp_BeihilfeBEK(): #YES, NEED TO MAKE OTHER TARIFFS
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaCalculationService/calculatNewIp"
    _name_endpoint = "POST Tariff calculation BEK"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
    "offerControl": {
        "ind": "20180701"
    },
    "offerIp": {
        "dateOfBirth": "19970412",
        "ipConditionList": [
            {
                "ipConditionCharacteristic": {
                    "enumerator": 6
                },
                "ipConditionType": {
                    "enumerator": "COMPULSORY_EXTRA_PREMIUM"
                }
            },
            {
                "ipConditionCharacteristic": {
                    "enumerator": 10
                },
                "ipConditionType": {
                    "enumerator": "CNCI"
                }
            }
        ],
        "sex": {
            "enumerator": "FEMALE"
        }
    },
    "offerTariffList": [
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "BAZ50"
            },
            "tariffRate": 0.0,
            "tariffSpcList": []
        },
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "BS35"
            },
            "tariffRate": 0.0,
            "tariffSpcList": []
        },
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "BEC100"
            },
            "tariffRate": 0.0,
            "tariffSpcList": []
        },
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "BBC35"
            },
            "tariffRate": 0.0,
            "tariffSpcList": []
        },
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "BFC100"
            },
            "tariffRate": 0.0,
            "tariffSpcList": []
        },
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "pvb"
            },
            "tariffRate": 0.0,
            "tariffSpcList": []
        }
    ],
    "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
    },
    "validateFlag": "false"
}

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

@pytest.mark.innovasBErequest
def test__comparison_request_BEK_innovas_v17vsV19_calculatNewIp_FullInsuranceOLD():
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaCalculationService/calculatNewIp"
    _name_endpoint = "POST Tariff calculation FullInsurance"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
    "offerControl": {
        "ind": "20191001"
    },
    "offerIp": {
        "dateOfBirth": "19970412",
        "ipConditionList": [
            {
                "ipConditionCharacteristic": {
                    "enumerator": 6
                },
                "ipConditionType": {
                    "enumerator": "COMPULSORY_EXTRA_PREMIUM" # weg für kind
                }
            },
            {
                "ipConditionCharacteristic": {
                    "enumerator": 10  #changed was 10
                },
                "ipConditionType": {
                    "enumerator": "CNCI"
                }
            }
        ],
        "sex": {
            "enumerator": "FEMALE"
        }
    },
    "offerTariffList": [
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "FirstClass1" # changed "BAZ50"
            },
            "tariffRate": 0.0, #changed tarriff SpcList was empty
            "tariffSpcList": [
                {
                        "specialPolicyCondition": {
                            "enumerator": "RZ"
                        },
                        "spcValue": 10,
                        "spcValueType": {
                            "enumerator": "PERCENT"
                        }
                    },
            ]
        },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "KTA42"
        #     },
        #     "tariffRate": 30,
        #     "tariffSpcList": []
        # },
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "pvb" # was "BEC100"
            },
            "tariffRate": 0.0,
            "tariffSpcList": []
        },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "BBC35"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "BFC100"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "pvb"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # }
    ],
    "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
    },
    "validateFlag": "false"
}

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

    return rd_17, rd_19

@pytest.mark.innovasBErequest
def test__comparison_request_BEK_innovas_v17vsV19_calculatNewIp_FullInsuranceNew():
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaCalculationService/calculatNewIp"
    _name_endpoint = "POST Tariff calculation FullInsurance"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
    "offerControl": {
        "ind": "20191001"
    },
    "offerIp": {
        "dateOfBirth": "19970412",
        "ipConditionList": [
            {
                "ipConditionCharacteristic": {
                    "enumerator": 6
                },
                "ipConditionType": {
                    "enumerator": "COMPULSORY_EXTRA_PREMIUM" # weg für kind
                }
            },
            {
                "ipConditionCharacteristic": {
                    "enumerator": 10  #changed was 10
                },
                "ipConditionType": {
                    "enumerator": "CNCI"
                }
            }
        ],
        "sex": {
            "enumerator": "FEMALE"
        }
    },
    "offerTariffList": [
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "VFC10E" # changed "BAZ50"
            },
            "tariffRate": 0.0, #changed tarriff SpcList was empty
            "tariffSpcList": [
                {
                        "specialPolicyCondition": {
                            "enumerator": "RZ"
                        },
                        "spcValue": 10,
                        "spcValueType": {
                            "enumerator": "PERCENT"
                        }
                    },
            ]
        },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "KTA42"
        #     },
        #     "tariffRate": 30,
        #     "tariffSpcList": []
        # },
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "pvb" # was "BEC100"
            },
            "tariffRate": 0.0,
            "tariffSpcList": []
        },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "BBC35"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "BFC100"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "pvb"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # }
    ],
    "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
    },
    "validateFlag": "false"
}

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

    return rd_17, rd_19

@pytest.mark.innovasBErequest
def test__comparison_request_BEK_innovas_v17vsV19_calculatNewIp_FullInsuranceChild():
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaCalculationService/calculatNewIp"
    _name_endpoint = "POST Tariff calculation FullInsurance"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
    "offerControl": {
        "ind": "20191001"
    },
    "offerIp": {
        "dateOfBirth": "20100412",
        "ipConditionList": [
            {
                "ipConditionCharacteristic": {
                    "enumerator": 6
                },
                "ipConditionType": {
                    "enumerator": "COMPULSORY_EXTRA_PREMIUM" # weg für kind
                }
            },
            {
                "ipConditionCharacteristic": {
                    "enumerator": 12  #changed was 10
                },
                "ipConditionType": {
                    "enumerator": "CNCI"
                }
            }
        ],
        "sex": {
            "enumerator": "FEMALE"
        }
    },
    "offerTariffList": [
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "VFC10E" # changed "BAZ50"
            },
            "tariffRate": 0.0, #changed tarriff SpcList was empty
            "tariffSpcList": [
                {
                        "specialPolicyCondition": {
                            "enumerator": "RZ"
                        },
                        "spcValue": 10,
                        "spcValueType": {
                            "enumerator": "PERCENT"
                        }
                    },
            ]
        },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "KTA42"
        #     },
        #     "tariffRate": 30,
        #     "tariffSpcList": []
        # },
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "pvb" # was "BEC100"
            },
            "tariffRate": 0.0,
            "tariffSpcList": []
        },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "BBC35"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "BFC100"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "pvb"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # }
    ],
    "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
    },
    "validateFlag": "false"
}

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

    return rd_17, rd_19

@pytest.mark.innovasBErequest
def test__comparison_request_BEK_innovas_v17vsV19_calculatNewIp_Zahn():
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaCalculationService/calculatNewIp"
    _name_endpoint = "POST Tariff calculation FullInsurance"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
    "offerControl": {
        "ind": "20191001"
    },
    "offerIp": {
        "dateOfBirth": "19900412",
        "ipConditionList": [
            {
                "ipConditionCharacteristic": {
                    "enumerator": 6
                },
                "ipConditionType": {
                    "enumerator": "COMPULSORY_EXTRA_PREMIUM" # weg für kind
                }
            },
            {
                "ipConditionCharacteristic": {
                    "enumerator": 10  #changed was 10
                },
                "ipConditionType": {
                    "enumerator": "CNCI"
                }
            }
        ],
        "sex": {
            "enumerator": "FEMALE"
        }
    },
    "offerTariffList": [
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "ZahnBusiness" # changed "BAZ50"
            },
            "tariffRate": 0.0, #changed tarriff SpcList was empty
            "tariffSpcList": [
                {
                        "specialPolicyCondition": {
                            "enumerator": "RZ"
                        },
                        "spcValue": 10,
                        "spcValueType": {
                            "enumerator": "PERCENT"
                        }
                    },
            ]
        },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "KTA42"
        #     },
        #     "tariffRate": 30,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "pvb" # was "BEC100"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "BBC35"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "BFC100"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "pvb"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # }
    ],
    "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
    },
    "validateFlag": "false"
}

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

    return rd_17, rd_19

@pytest.mark.innovasBErequest
def test__comparison_request_BEK_innovas_v17vsV19_calculatNewIp_Clinik():
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaCalculationService/calculatNewIp"
    _name_endpoint = "POST Tariff calculation FullInsurance"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
    "offerControl": {
        "ind": "20191001"
    },
    "offerIp": {
        "dateOfBirth": "19900412",
        "ipConditionList": [
            {
                "ipConditionCharacteristic": {
                    "enumerator": 6
                },
                "ipConditionType": {
                    "enumerator": "COMPULSORY_EXTRA_PREMIUM" # weg für kind
                }
            },
            {
                "ipConditionCharacteristic": {
                    "enumerator": 10  #changed was 10
                },
                "ipConditionType": {
                    "enumerator": "CNCI"
                }
            }
        ],
        "sex": {
            "enumerator": "FEMALE"
        }
    },
    "offerTariffList": [
        {
            "tariffDisqualificationList": [],
            "tariffIdentification": {
                "enumerator": "Klinik1" # changed "BAZ50"
            },
            "tariffRate": 0.0, #changed tarriff SpcList was empty
            "tariffSpcList": [
                {
                        "specialPolicyCondition": {
                            "enumerator": "RZ"
                        },
                        "spcValue": 10,
                        "spcValueType": {
                            "enumerator": "PERCENT" #oder "ABSOLUT"
                        }
                    },
            ]
        },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "KTA42"
        #     },
        #     "tariffRate": 30,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "pvb" # was "BEC100"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "BBC35"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "BFC100"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # },
        # {
        #     "tariffDisqualificationList": [],
        #     "tariffIdentification": {
        #         "enumerator": "pvb"
        #     },
        #     "tariffRate": 0.0,
        #     "tariffSpcList": []
        # }
    ],
    "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
    },
    "validateFlag": "false"
}

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

    return rd_17, rd_19







@pytest.mark.innovasBErequest
def test__comparison_ottonova_cmk_OttonovaRetentionService_getTariffsRetentionRemainingForYear_request_innovas_v17vsV19():

# # /ottonova_ws/rest/ottonova_cmk/OttonovaRetentionService/getTariffsRetentionRemainingForYear
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17
#   },
#   "policyNumber": 90000111,
#   "ipNumber": 1,
#   "tariffIdentification": {
#       "enumerator": "FirstClass1"
#   },
#   "tariffNr": 1,
#   "dateInYear": "20171231"
# }
    _endpoint = "/ottonova_ws/rest/ottonova_cmk/OttonovaRetentionService/getTariffsRetentionRemainingForYear"
    _name_endpoint = "POST TarifsRetention" # Not in postman
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body_17 = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
      },
      "policyNumber": 90000111,
      "ipNumber": 1,
      "tariffIdentification": {
          "enumerator": "FirstClass1"
      },
      "tariffNr": 1,
      "dateInYear": "20171231"
    }

    body_19 = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
      },
      "policyNumber": 90000111,
      "ipNumber": 1,
      "tariffIdentification": {
          "enumerator": "FirstClass1"
      },
      "tariffNr": 1,
      "dateInYear": "20171231"
    }

    r_v17 = requests.post(_target_url_17, json=body_17, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body_17))

    r_v19 = requests.post(_target_url_19, json=body_19, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body_19))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))


    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

@pytest.mark.innovasBErequest
def test__comparison_ottonova_cmk_OttonovaRetentionService_getTariffsRetentionToKeepForYear_request_innovas_v17vsV19():

# # /ottonova_ws/rest/ottonova_cmk/OttonovaRetentionService/getTariffsRetentionToKeepForYear
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17
#   },
#   "policyNumber": 90000111,
#   "ipNumber": 1,
#   "tariffIdentification": {
#       "enumerator": "FirstClass1"
#   },
#   "tariffNr": 1,
#   "dateInYear": "20171231"
# }
    _endpoint = "/ottonova_ws/rest/ottonova_cmk/OttonovaRetentionService/getTariffsRetentionToKeepForYear"
    _name_endpoint = "POST TarifsRetentionToKeep" # Not in postman
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body_17 = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
      },
      "policyNumber": 90000111,
      "ipNumber": 1,
      "tariffIdentification": {
          "enumerator": "FirstClass1"
      },
      "tariffNr": 1,
      "dateInYear": "20171231"
    }

    body_19 = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17
      },
      "policyNumber": 90000111,
      "ipNumber": 1,
      "tariffIdentification": {
          "enumerator": "FirstClass1"
      },
      "tariffNr": 1,
      "dateInYear": "20171231"
    }

    r_v17 = requests.post(_target_url_17, json=body_17, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body_17))

    r_v19 = requests.post(_target_url_19, json=body_19, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body_19))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))


    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    # del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
          "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

# As the last
def test__comparison_ottonova_cmk_OttonovaHipmOnlineService_submit_request_innovas_v17vsV19(): #As the last
    # # /ottonova_ws/rest/ottonova_hipm/OttonovaHipmOnlineService/submit
    # {
    #   "value": {
    #     "policyNumber": "40000005",
    #     "contractNumber": 3005,
    #     "premium": 3038.12,
    #     "finishingFlag": "true",
    #     "errorLevel": {
    #       "enumerator": "NOT_DEFINED",
    #       "text": "CD_ERROR_LEVEL.0"
    #     },
    #     "errorSubLevel": {
    #       "enumerator": "NOT_DEFINED",
    #       "text": "CD_ERROR_SUB_LEVEL.0"
    #     },
    #     "errorMessageList": [],
    #     "onlineInsuredPersonRetList": [
    #       {
    #         "ipNr": 1,
    #         "premium": 3038.12,
    #         "onlineTariffRetList": [
    #           {
    #             "tariffIdentification": {
    #               "enumerator": "FirstClass1",
    #               "text": "CD_TARIFF.FirstClass1"
    #             },
    #             "tariffRate": 0,
    #             "premium": 1088.42,
    #             "onlineSpcRetList": [
    #               {
    #                 "diagnosis": {
    #                   "enumerator": "S83.2",
    #                   "text": "Meniskusriss, akut"
    #                 },
    #                 "textTemplateId": null,
    #                 "specialPolicyCondition": {
    #                   "enumerator": "RZ",
    #                   "text": "Risikozuschlag"
    #                 },
    #                 "spcValue": 10,
    #                 "spcValueType": {
    #                   "enumerator": "PERCENT",
    #                   "text": "Prozent"
    #                 },
    #                 "premium": 98.95,
    #                 "diagnosisText": "Meniskusriss, akut",
    #                 "spcText": "Risikozuschlag"
    #               }
    #             ],
    #             "onlineTarDisqRetList": []
    #           },
    #           {
    #             "tariffIdentification": {
    #               "enumerator": "KTA42",
    #               "text": "CD_TARIFF.KTA42"
    #             },
    #             "tariffRate": 30,
    #             "premium": 1949.7,
    #             "onlineSpcRetList": [],
    #             "onlineTarDisqRetList": []
    #           }
    #         ],
    #         "errorLevel": {
    #           "enumerator": "NOT_DEFINED",
    #           "text": "CD_ERROR_LEVEL.0"
    #         },
    #         "errorSubLevel": {
    #           "enumerator": "NOT_DEFINED",
    #           "text": "CD_ERROR_SUB_LEVEL.0"
    #         }
    #       }
    #     ]
    #   },
    #   "messages": [
    #     "Vorgang wurde auf Schwebe gelegt.",
    #     "Der Vorgang wurde freigegeben"
    #   ],
    #   "processNumber": 1015
    # }
    _endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaHipmOnlineService/submit"
    _name_endpoint = ""  # Not in postman
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body_17 = {
      "value": {
        "policyNumber": "40000005",
        "contractNumber": 3005,
        "premium": 3038.12,
        "finishingFlag": "true",
        "errorLevel": {
          "enumerator": "NOT_DEFINED",
          "text": "CD_ERROR_LEVEL.0"
        },
        "errorSubLevel": {
          "enumerator": "NOT_DEFINED",
          "text": "CD_ERROR_SUB_LEVEL.0"
        },
        "errorMessageList": [],
        "onlineInsuredPersonRetList": [
          {
            "ipNr": 1,
            "premium": 3038.12,
            "onlineTariffRetList": [
              {
                "tariffIdentification": {
                  "enumerator": "FirstClass1",
                  "text": "CD_TARIFF.FirstClass1"
                },
                "tariffRate": 0,
                "premium": 1088.42,
                "onlineSpcRetList": [
                  {
                    "diagnosis": {
                      "enumerator": "S83.2",
                      "text": "Meniskusriss, akut"
                    },
                    "textTemplateId": "null",
                    "specialPolicyCondition": {
                      "enumerator": "RZ",
                      "text": "Risikozuschlag"
                    },
                    "spcValue": 10,
                    "spcValueType": {
                      "enumerator": "PERCENT",
                      "text": "Prozent"
                    },
                    "premium": 98.95,
                    "diagnosisText": "Meniskusriss, akut",
                    "spcText": "Risikozuschlag"
                  }
                ],
                "onlineTarDisqRetList": []
              },
              {
                "tariffIdentification": {
                  "enumerator": "KTA42",
                  "text": "CD_TARIFF.KTA42"
                },
                "tariffRate": 30,
                "premium": 1949.7,
                "onlineSpcRetList": [],
                "onlineTarDisqRetList": []
              }
            ],
            "errorLevel": {
              "enumerator": "NOT_DEFINED",
              "text": "CD_ERROR_LEVEL.0"
            },
            "errorSubLevel": {
              "enumerator": "NOT_DEFINED",
              "text": "CD_ERROR_SUB_LEVEL.0"
            }
          }
        ]
      },
      "messages": [
        "Vorgang wurde auf Schwebe gelegt.",
        "Der Vorgang wurde freigegeben"
      ],
      "processNumber": 1015
    }


    body_19 = {
      "value": {
        "policyNumber": "40000005",
        "contractNumber": 3005,
        "premium": 3038.12,
        "finishingFlag": "true",
        "errorLevel": {
          "enumerator": "NOT_DEFINED",
          "text": "CD_ERROR_LEVEL.0"
        },
        "errorSubLevel": {
          "enumerator": "NOT_DEFINED",
          "text": "CD_ERROR_SUB_LEVEL.0"
        },
        "errorMessageList": [],
        "onlineInsuredPersonRetList": [
          {
            "ipNr": 1,
            "premium": 3038.12,
            "onlineTariffRetList": [
              {
                "tariffIdentification": {
                  "enumerator": "FirstClass1",
                  "text": "CD_TARIFF.FirstClass1"
                },
                "tariffRate": 0,
                "premium": 1088.42,
                "onlineSpcRetList": [
                  {
                    "diagnosis": {
                      "enumerator": "S83.2",
                      "text": "Meniskusriss, akut"
                    },
                    "textTemplateId": "null",
                    "specialPolicyCondition": {
                      "enumerator": "RZ",
                      "text": "Risikozuschlag"
                    },
                    "spcValue": 10,
                    "spcValueType": {
                      "enumerator": "PERCENT",
                      "text": "Prozent"
                    },
                    "premium": 98.95,
                    "diagnosisText": "Meniskusriss, akut",
                    "spcText": "Risikozuschlag"
                  }
                ],
                "onlineTarDisqRetList": []
              },
              {
                "tariffIdentification": {
                  "enumerator": "KTA42",
                  "text": "CD_TARIFF.KTA42"
                },
                "tariffRate": 30,
                "premium": 1949.7,
                "onlineSpcRetList": [],
                "onlineTarDisqRetList": []
              }
            ],
            "errorLevel": {
              "enumerator": "NOT_DEFINED",
              "text": "CD_ERROR_LEVEL.0"
            },
            "errorSubLevel": {
              "enumerator": "NOT_DEFINED",
              "text": "CD_ERROR_SUB_LEVEL.0"
            }
          }
        ]
      },
      "messages": [
        "Vorgang wurde auf Schwebe gelegt.",
        "Der Vorgang wurde freigegeben"
      ],
      "processNumber": 1015
    }

    r_v17 = requests.post(_target_url_17, json=body_17, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body_17))

    r_v19 = requests.post(_target_url_19, json=body_19, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body_19))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))

    # r_text17 = r_v17.text
    # rd_17 = json.loads(r_text17)
    #
    # r_text19 = r_v19.text
    # rd_19 = json.loads(r_text19)
    # # del rd_19['value']["lockType"]
    #
    # print(rd_17)
    # print(rd_19)
    #
    # assert rd_17 == rd_19
    # print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
    #       "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))

# error":"Ordnungsbegriff durch Benutzer xkvgast03 seit 22.08.2019 13:08:30 gesperrt. "
def test__comparison_LtxManager_startNewLtx_CONTRACT_request_innovas_v17vsV19():
    _endpoint = "/ottonova_ws/rest/infra/LtxManager/startNewLtx"
    _name_endpoint = "POST LtxManager.startNewLtx"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body_17 = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03"
      },
      "key": "{{contract_number}}",
      "processType": "HIPM_POLICY_MANAGEMENT",
      "ignoreExistingLocks": "false"
    }

    body_19 = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03"
      },
      "key": "{{contract_number}}",
      "processType": "HIPM_POLICY_MANAGEMENT",
      #"ignoreExistingLocks": "false"
    }

    r_v17 = requests.post(_target_url_17, json=body_17, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body_17))

    r_v19 = requests.post(_target_url_19, json=body_19, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body_19))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))

    return r_v17, r_v19

#"error":"Ordnungsbegriff durch Benutzer xkvgast03 seit 22.08.2019 11:11:44 gesperrt. "
def test__comparison_startNewLtx_PARTNER_request_innovas_v17vsV19():
    _endpoint = "/ottonova_ws/rest/infra/LtxManager/startNewLtx"
    _name_endpoint = "POST LtxManager.startNewLtx"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body_17={
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03"
      },
      "key": "{{partner_number}}",
      "processType": "PARTNERS_PARTNER_EDIT",
      "ignoreExistingLocks": "false"
    }

    body_19={
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03"
      },
      "key": "{{partner_number}}",
      "processType": "PARTNERS_PARTNER_EDIT",
      #"ignoreExistingLocks": "false"
    }

    r_v17 = requests.post(_target_url_17, json=body_17, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body_17))

    r_v19 = requests.post(_target_url_19, json=body_19, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body_19))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))


def test__comparison_LtxManager_getConflictingLock_request_innovas_v17vsV19():
    _endpoint = "/ottonova_ws/rest/infra/LtxManager/getConflictingLock"
    _name_endpoint = "POST LtxManager.getConflictingLock"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body_17 = {
      "serviceContextInfo": {
        "locale": "de",
          "mandator": 17,
          "userID": "xkvgast03"
      },
      "key": "{{partner_number}}",
      "processType": {
        "enumerator": "PARTNERS_PARTNER_EDIT"
      }
    }

    body_19 = {
      "serviceContextInfo": {
        "locale": "de",
          "mandator": 17,
          "userID": "xkvgast03"
      },
      "key": "{{partner_number}}",
      "processType": {
        "enumerator": "PARTNERS_PARTNER_EDIT"
      }
    }

    r_v17 = requests.post(_target_url_17, json=body_17, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body_17))

    r_v19 = requests.post(_target_url_19, json=body_19, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body_19))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))


def test__comparison_LtxManager_Lock_request_innovas_v17vsV19():
    _endpoint = "/ottonova_ws/rest/infra/LtxManager/lock"
    _name_endpoint = "POST LtxManager.lock"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint
    process_number = 433176

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body_17 = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03",
        "processNumber": process_number
      },
      "keyClass": "PARTNERNR",
      "key": "{{partner_number}}",
      "lockLevel": {
        "enumerator": "ALLOW_READ"
      }
    }

    body_19 = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03",
        "processNumber": process_number
      },
      "keyClass": "PARTNERNR",
      "key": "{{partner_number}}",
      "lockLevel": {
        "enumerator": "ALLOW_READ"
      }
    }

    r_v17 = requests.post(_target_url_17, json=body_17, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body_17))

    r_v19 = requests.post(_target_url_19, json=body_19, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body_19))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))


def test__comparison_LtxManager_getConflictingLock_request_innovas_v17vsV19():
    _endpoint = "/ottonova_ws/rest/infra/LtxManager/getConflictingLock"
    _name_endpoint = "POST LtxManager.getConflictingLock"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body_17 = {
      "serviceContextInfo": {
        "locale": "de",
          "mandator": 17,
          "userID": "xkvgast03"
      },
      "key": "{{partner_number}}",
      "processType": {
        "enumerator": "PARTNERS_PARTNER_EDIT"
      }
    }

    body_19 = {
      "serviceContextInfo": {
        "locale": "de",
          "mandator": 17,
          "userID": "xkvgast03"
      },
      "key": "{{partner_number}}",
      "processType": {
        "enumerator": "PARTNERS_PARTNER_EDIT"
      }
    }

    r_v17 = requests.post(_target_url_17, json=body_17, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body_17))

    r_v19 = requests.post(_target_url_19, json=body_19, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body_19))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))


def test__comparison_LtxManager_commit_request_innovas_v17vsV19():
    _endpoint = "/ottonova_ws/rest/infra/LtxManager/commit"
    _name_endpoint = "POST LtxManager.commit"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint
    process_number = 433176

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body_17 = {
      "serviceContextInfo": {
        "locale": "de",
          "mandator": 17,
          "userID": "xkvgast03",
          "processNumber": process_number
      }
    }

    body_19 = {
      "serviceContextInfo": {
        "locale": "de",
          "mandator": 17,
          "userID": "xkvgast03",
          "processNumber": process_number
      }
    }

    r_v17 = requests.post(_target_url_17, json=body_17, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body_17))

    r_v19 = requests.post(_target_url_19, json=body_19, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body_19))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))


def test__comparison_LtxManager_rollback_request_innovas_v17vsV19():
    _endpoint = "/ottonova_ws/rest/infra/LtxManager/rollback"
    _name_endpoint = "POST LtxManager.rollback"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint
    process_number = "432705"

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body_17 = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03",
        "processNumber": process_number
      }
    }

    body_19 = {
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03",
        "processNumber": process_number
      }
    }

    r_v17 = requests.post(_target_url_17, json=body_17, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body_17))

    r_v19 = requests.post(_target_url_19, json=body_19, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body_19))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))


def test__comparison_submit_request_innovas_v17vsV19():
    _endpoint = "/ottonova_ws/rest/infra/LtxManager/startNewLtx"
    #_endpoint = "/ottonova_ws/rest/infra/LtxManager/commit"
    _name_endpoint = "POST LtxManager.commit"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint
    process_number = "null"


    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    # #
    body={
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03"
      },
      "key": "{{partner_number}}",
      "processType": "PARTNERS_PARTNER_EDIT",
      #"ignoreExistingLocks": "false"
    }
#     body = {
#       "serviceContextInfo": {
#         "locale": "de",
#           "mandator": 17,
#           "userID": "xkvgast03",
#           "processNumber": 1
# #          "processNumber": {{process_number}}
#       }
#     }

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    #print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))


def test__comparison_submit_request_innovas_v17vsV19():
    _endpoint = "/ottonova_ws/rest/infra/LtxManager/getConflictingLock"
    #_endpoint = "/ottonova_ws/rest/infra/LtxManager/commit"
    _name_endpoint = "POST LtxManager.commit"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint
    process_number = "null"


    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    # #
    body={
      "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03"
      },
      "key": "{{partner_number}}",
      "processType": "PARTNERS_PARTNER_EDIT",
      #"ignoreExistingLocks": "false"
    }
#     body = {
#       "serviceContextInfo": {
#         "locale": "de",
#           "mandator": 17,
#           "userID": "xkvgast03",
#           "processNumber": 1
# #          "processNumber": {{process_number}}
#       }
#     }

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    #print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 17 response: {response}".format(response=r_v17.text))
    print("\nVersion 19 response: {response}".format(response=r_v19.text))

# # /ottonova_ws/rest/infra/LtxManager/commit
# #{
#   "serviceContextInfo": {
#     "locale": "de",
#       "mandator": 17,
#       "userID": "xkvgast03",
#       "processNumber": {{process_number}}
#   }
# }
# # /ottonova_ws/rest/infra/LtxManager/getConflictingLock
# {
#   "serviceContextInfo": {
#     "locale": "de",
#       "mandator": 17,
#       "userID": "xkvgast03"
#   },
#   "key": "{{partner_number}}",
#   "processType": {
#     "enumerator": "PARTNERS_PARTNER_EDIT"
#   }
# }
# # /ottonova_ws/rest/infra/LtxManager/rollback
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17,
#     "userID": "xkvgast03",
#     "processNumber": {{process_number}}
#   }
# }
# # /ottonova_ws/rest/infra/LtxManager/startNewLtx YES
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17,
#     "userID": "xkvgast03"
#   },
#   "key": "{{partner_number}}",
#   "processType": "PARTNERS_PARTNER_EDIT",
#   "ignoreExistingLocks": false
# }
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17,
#     "userID": "xkvgast03"
#   },
#   "key": "{{contract_number}}",
#   "processType": "HIPM_POLICY_MANAGEMENT",
#   "ignoreExistingLocks": false
# }
# # /ottonova_ws/rest/ottonova_cmk/OttonovaRetentionService/getTariffsRetentionRemainingForYear #YES
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17
#   },
#   "policyNumber": 90000111,
#   "ipNumber": 1,
#   "tariffIdentification": {
#       "enumerator": "FirstClass1"
#   },
#   "tariffNr": 1,
#   "dateInYear": "20171231"
# }
#
# # /ottonova_ws/rest/ottonova_cmk/OttonovaRetentionService/getTariffsRetentionToKeepForYear #YES
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17
#   },
#   "policyNumber": 90000111,
#   "ipNumber": 1,
#   "tariffIdentification": {
#       "enumerator": "FirstClass1"
#   },
#   "tariffNr": 1,
#   "dateInYear": "20171231"
# }
#
#
#
#
# # # /ottonova_ws/rest/ottonova_hipm/OttonovaCalculationService/calculatNewIp
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17
#   },
#   "offerControl": {
#     "ind": {{ingress_date_json}}
#   },
#   "offerIp": {
#     "dateOfBirth": {{date_of_birth_json}},
#     "ipConditionList": {{condition_list_json}},
#     "sex": {{sex_json}}
#   },
#   "offerTariffList": {{tariff_list_json}},
#   "validateFlag": "false"
# }
#
# # /ottonova_ws/rest/ottonova_hipm/OttonovaContractInformationService/getContractInformation
# body = {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17,
#     "userID": "xkvgast03"
#   },
#   "onlineData": {
#     "applicationTimeStamp": {{application_timestamp_json}},
#     "onlineIpList": {
#       {
#         "beginOfIp": {{ingress_date_json}},
#         "hiInsuranceCompany": 9096,
#         "ipConditionList": {{condition_list_json}},
#         "ipDiagnosisList": {{diagnosis_list_json}},
#         "ipEqualsPhFlag": {{has_no_coinsured_person}},
#         {{coinsured_person_data_json}}
#         "onlineTariffList": {{tariff_list_json}}
#       }
#   },
#     "onlinePolicyHolder": {
#       "onlineAddressData": {{address_data_json}},
#       "onlineCommunication": {{communication_json}},
#       "onlinePersonData": {{person_data_json}},
#       "signedFlag": true
#     },
#     "onlinePremiumPayer": {
#       "onlineBankData": {{bank_data_json}},
#       "ppEqualsPhFlag": true
#     },
#     "paymentPeriodId": {
#       "enumerator": 1
#     },
#     "paymentMethod": {
#       "enumerator": 1
#     },
#     "bzstTransmission": {
#       "enumerator": 2
#     },
#     "consentYear": 2017
#   }
# }
#
#
#
# # /ottonova_ws/rest/ottonova_hipm/OttonovaHipmOnlineService/submit
#
# {
#   "value": {
#     "policyNumber": "40000005",
#     "contractNumber": 3005,
#     "premium": 3038.12,
#     "finishingFlag": true,
#     "errorLevel": {
#       "enumerator": "NOT_DEFINED",
#       "text": "CD_ERROR_LEVEL.0"
#     },
#     "errorSubLevel": {
#       "enumerator": "NOT_DEFINED",
#       "text": "CD_ERROR_SUB_LEVEL.0"
#     },
#     "errorMessageList": [],
#     "onlineInsuredPersonRetList": [
#       {
#         "ipNr": 1,
#         "premium": 3038.12,
#         "onlineTariffRetList": [
#           {
#             "tariffIdentification": {
#               "enumerator": "FirstClass1",
#               "text": "CD_TARIFF.FirstClass1"
#             },
#             "tariffRate": 0,
#             "premium": 1088.42,
#             "onlineSpcRetList": [
#               {
#                 "diagnosis": {
#                   "enumerator": "S83.2",
#                   "text": "Meniskusriss, akut"
#                 },
#                 "textTemplateId": null,
#                 "specialPolicyCondition": {
#                   "enumerator": "RZ",
#                   "text": "Risikozuschlag"
#                 },
#                 "spcValue": 10,
#                 "spcValueType": {
#                   "enumerator": "PERCENT",
#                   "text": "Prozent"
#                 },
#                 "premium": 98.95,
#                 "diagnosisText": "Meniskusriss, akut",
#                 "spcText": "Risikozuschlag"
#               }
#             ],
#             "onlineTarDisqRetList": []
#           },
#           {
#             "tariffIdentification": {
#               "enumerator": "KTA42",
#               "text": "CD_TARIFF.KTA42"
#             },
#             "tariffRate": 30,
#             "premium": 1949.7,
#             "onlineSpcRetList": [],
#             "onlineTarDisqRetList": []
#           }
#         ],
#         "errorLevel": {
#           "enumerator": "NOT_DEFINED",
#           "text": "CD_ERROR_LEVEL.0"
#         },
#         "errorSubLevel": {
#           "enumerator": "NOT_DEFINED",
#           "text": "CD_ERROR_SUB_LEVEL.0"
#         }
#       }
#     ]
#   },
#   "messages": [
#     "Vorgang wurde auf Schwebe gelegt.",
#     "Der Vorgang wurde freigegeben"
#   ],
#   "processNumber": 1015
# }
# # /ottonova_ws/rest/partners/PartnersAddress/readAddress
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17,
#     "userID": "xkvgast03"
#   },
#   "partnersNumber" : {{partner_number}},
#   "addressNumber": 1,
#   "dop": null,
#   "ind": null
# }
# # /ottonova_ws/rest/partners/PartnersAddress/writeAddress
# {
# "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17,
#     "userID": "xkvgast03",
#     "processNumber": {{process_number}}
# },
# "address": {
#     "ind": "20170508",
#     "partnersNumber": "{{partner_number}}",
#     "postcode": 11111,
#     "city1": "Berlin",
#     "street": "some street",
#     "houseNumber": "11"
#
# },
# "ignoreValidation": true
# }
# # /ottonova_ws/rest/partners/PartnersBank/writeBank
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17,
#     "userID": "xkvgast03",
#     "processNumber": {{process_number}}
#   },
#   "bank" : {
#     "bankNr": null,
#     "partnersNumber": "{{partner_number}}",
#     "outdated": false,
#     "userId": null,
#     "bankCode": "",
#     "accountNumber": "",
#     "bankName": "",
#     "accountHolder": "",
#     "bankDistrict": "",
#     "districtBankCode": null,
#     "creditCardCompany": "",
#     "creditCardNumber": "",
#     "creditCardExpiry": null,
#     "creditCardSecurityCode": null,
#     "creditCardType": {
#       "enumerator": "",
#       "text": "nicht belegt"
#     },
#     "accountType": {
#       "enumerator": 0,
#       "text": "nicht belegt"
#     },
#     "bankState": {
#       "enumerator": "UNVERIFIED",
#       "text": "ungeprüft"
#     },
#     "town": null,
#     "streetAndNo": null,
#     "currencyOfAccount": null,
#     "ind": "10661014",
#     "reasonForChange": null,
#     "country": {
#       "enumerator": "DE",
#       "text": "Deutschland"
#     },
#     "postcode": null,
#     "iban": "DE24590100428525636302",
#     "bic": ""
#   },
#   "ignoreValidation": false
# }
# # /ottonova_ws/rest/partners/PartnersCompleteData/readCompletePartnerData
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17,
#     "userID": "xkvgast03"
#   },
#   "partnersNumber" : {{partner_number}},
#   "withFutureRoles": true
# }
# # /ottonova_ws/rest/partners/PartnersRole/readRole
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17,
#     "userID": "xkvgast03"
#   },
#   "leftSide" : {{contract_number}},
#   "role": {
#     "enumerator": "PH"
#    },
#   "withPartnerData": false,
#   "withComponentData": false,
#   "withDefaultRole": false
# }
# # 2
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17,
#     "userID": "xkvgast03"
#   },
#   "leftSide" : {{contract_number}},
#   "role": {
#     "enumerator": "IP"
#    },
#   "withPartnerData": false,
#   "withComponentData": false,
#   "withDefaultRole": false
# }
# # /ottonova_ws/rest/partners/PartnersRole/writeRole
# {
#   "serviceContextInfo": {
#     "locale": "de",
#     "mandator": 17,
#     "userID": "xkvgast03",
#     "processNumber": {{process_number}}
#   },
#   "partnersRole": {
#     "leftSide": "{{contract_number}}",
#     "ind":"20170301",
#     "rightSide": "{{partner_number}}",
#     "addressNr": "1",
#     "bankNr": "7",
#     "communicationNr": "1",
#     "externKey": "{{policy_number}}",
#     "role": {
#       "enumerator": "PH"
#     }
#   }
# }

# /ottonova_ws/rest/partners/PartnersTeleCommunication/writeTeleCommunication


@pytest.mark.innovasBErequest
def test__comparison_ping_request_innovas_v17vsV19():
    _ping_endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaHipmOnlineService/ping"
    _name_endpoint = "POST Ping"
    _target_url_17 = _url_v17 + _ping_endpoint
    _target_url_19 = _url_v19 + _ping_endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
        "serviceContextInfo": {
            "locale": "de",
            "mandator": 17
        }
    }

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    assert r_v17.text == r_v19.text
    print("\nCorrect! The actual response corresponds to the expected response.")

@pytest.mark.innovasBErequest
def test__comparison_getprocessinfo_request_innovas_v17vsV19():
    _endpoint = "/ottonova_ws/rest/infra/LtxManager/getProcessInfo"
    _name_endpoint = "POST LtxManager.getProcessInfo"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body = {
    "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03"
        },
    "processType": "PARTNERS_PARTNER_EDIT"
    }

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    #print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    #print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    del rd_19['value']["lockType"]

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
        "Correct! The actual response corresponds to the expected response.".format(exp=rd_17,act=rd_19))

    #assert r_text17 == r_text19


@pytest.mark.innovasBErequest
def test__comparison_completepartnerdata_request_innovas_v17vsV19():
    _endpoint = "/ottonova_ws/rest/partners/PartnersCompleteData/readCompletePartnerData"
    _name_endpoint = "POST LtxManager.getProcessInfo"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body = {
    "serviceContextInfo": {
        "locale": "de",
        "mandator": 17,
        "userID": "xkvgast03"
        },
    "partnersNumber" : "101",
    "withFutureRoles": "true"
    }

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    #print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    #print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text17 = r_v17.text
    rd_17 = json.loads(r_text17)

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    #del rd_19['value']["lockType"]

    print(rd_17)
    print(rd_19)

    assert rd_17 == rd_19
    print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
        "Correct! The actual response corresponds to the expected response.".format(exp=rd_17,act=rd_19))

def comparison_submit_request_innovas_v17vsV19():

    _endpoint = "/ottonova_ws/rest/ottonova_hipm/OttonovaHipmOnlineService/submit"
    _name_endpoint = "POST LtxManager.getProcessInfo"
    _target_url_17 = _url_v17 + _endpoint
    _target_url_19 = _url_v19 + _endpoint

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    body = {
      "value": {
        "policyNumber": "40000005",
        "contractNumber": 3005,
        "premium": 3038.12,
        "finishingFlag": "true",
        "errorLevel": {
          "enumerator": "NOT_DEFINED",
          "text": "CD_ERROR_LEVEL.0"
        },
        "errorSubLevel": {
          "enumerator": "NOT_DEFINED",
          "text": "CD_ERROR_SUB_LEVEL.0"
        },
        "errorMessageList": [],
        "onlineInsuredPersonRetList": [
          {
            "ipNr": 1,
            "premium": 3038.12,
            "onlineTariffRetList": [
              {
                "tariffIdentification": {
                  "enumerator": "FirstClass1",
                  "text": "CD_TARIFF.FirstClass1"
                },
                "tariffRate": 0,
                "premium": 1088.42,
                "onlineSpcRetList": [
                  {
                    "diagnosis": {
                      "enumerator": "S83.2",
                      "text": "Meniskusriss, akut"
                    },
                    "textTemplateId": "null",
                    "specialPolicyCondition": {
                      "enumerator": "RZ",
                      "text": "Risikozuschlag"
                    },
                    "spcValue": 10,
                    "spcValueType": {
                      "enumerator": "PERCENT",
                      "text": "Prozent"
                    },
                    "premium": 98.95,
                    "diagnosisText": "Meniskusriss, akut",
                    "spcText": "Risikozuschlag"
                  }
                ],
                "onlineTarDisqRetList": []
              },
              {
                "tariffIdentification": {
                  "enumerator": "KTA42",
                  "text": "CD_TARIFF.KTA42"
                },
                "tariffRate": 30,
                "premium": 1949.7,
                "onlineSpcRetList": [],
                "onlineTarDisqRetList": []
              }
            ],
            "errorLevel": {
              "enumerator": "NOT_DEFINED",
              "text": "CD_ERROR_LEVEL.0"
            },
            "errorSubLevel": {
              "enumerator": "NOT_DEFINED",
              "text": "CD_ERROR_SUB_LEVEL.0"
            }
          }
        ]
      },
      "messages": [
        "Vorgang wurde auf Schwebe gelegt.",
        "Der Vorgang wurde freigegeben"
      ],
      "processNumber": 1015
    }

    r_v17 = requests.post(_target_url_17, json=body, headers=headers)
    #r_text17 = r_v17.text
    #rd_17 = json.loads(r_text17)
    print(r_v17)

    print("\nVersion 17 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_17,
                             H=headers,
                             B=body))

    #print("\nVersion 17 response:{response}".format(response=r_v17.text))

    r_v19 = requests.post(_target_url_19, json=body, headers=headers)

    print("\n\nVersion 19 request details: \n"
          "Name of the request: {name} \n"
          "Endpoint: {url} \n"
          "Headers: {H} \n"
          "Body: {B}".format(name=_name_endpoint,
                             url=_target_url_19,
                             H=headers,
                             B=body))

    print("\nVersion 17 response:{response}".format(response=r_v17.text))
    print("\nVersion 19 response :{response}".format(response=r_v19.text))

    r_text19 = r_v19.text
    rd_19 = json.loads(r_text19)
    #del rd_19['value']["lockType"]

    print(rd_19)

    #assert rd_17 == rd_19
    # print("\nAsserting the difference between the following two responses. \n Expected: \n {exp} \n Actual: \n {act} \n"
    #    "Correct! The actual response corresponds to the expected response.".format(exp=rd_17, act=rd_19))





# r_text_19 = r_v19.text
# d = json.loads(r_text)
# type(d)
# <class 'dict'>
# r_text_19 = r_v19.text
# d19 = json.loads(r_text_19)
# type(d19)
# <class 'dict'>
# d == d19
# True
# exp = d
# print(exp)
# {'value': True, 'messages': [], 'processNumber': None}
# exp = {'value': True, 'processNumber': None, 'messages': []}
# d == exp
# True