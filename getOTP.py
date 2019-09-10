from os import environ
from datetime import date

from twilio.rest import Client
from twilio.rest.api.v2010.account.message import MessageInstance

#from onSeleniumBased.modules.Printing import p_e

def extract_otp(message: MessageInstance,
                splitting_string: str = '(OTP): ') -> str:
    """
        gets the OTP from a MessageInstance
    :param message:
        a MessageInstance from the Twilio API
    :param splitting_string:
        where to split the string containing the OTP

    :return:
        the OTP as a string
    """
    otp_string = message.body

    #if splitting_string not in otp_string:
    #    p_e("Splitting string '{0}' not found in latest message '{1}'".format(splitting_string,
    #                                                                          otp_string))
    #    raise ValueError

    # splits the message
    trash, otp = otp_string.split(splitting_string)
    return otp


def get_otp_for_recipient(telephone: str=environ['TELEPHONE_NUMBER'],
                          splitting_string: str='(OTP): ',
                          timeout: int=1) -> str:
    """
        gets OTP from MessageBird for a user account based on the account_id
    :param telephone:
        the user telephone number
    :param splitting_string:
        where to split the string containing the OTP
    :param timeout:
        how many seconds to wait before sending request

    :return:
        OTP string
    """
    from time import sleep
    sleep(timeout)

    return extract_otp(message=latest(messages_to_number_from_today(telephone=telephone)),
                       splitting_string=splitting_string)

#IN CONSOLE:
#from getOTP import get_otp_for_recipient
#otp = get_otp_for_recipient(telephone="+4917647681010", splitting_string='(OTP): ')




# def get_otp_for_recipient_with_id(account_id: str,
#                                   telephone: str=environ['TELEPHONE_NUMBER'],
#                                   splitting_string: str='(OTP): ') -> str:
#     """
#         gets OTP from MessageBird for a user account based on the account_id
#     :param account_id:
#         the account-id used to identify the specific account for which to return the OTP
#     :param telephone:
#         the user telephone number
#     :param splitting_string:
#         where to split the string containing the OTP
#
#     :return:
#         OTP string
#     """
#     account_sid = environ['TWILIO_ACCOUNT_SID']
#     auth_token = environ['TWILIO_AUTH_TOKEN']
#     client = Client(account_sid, auth_token)
#
#     latest_matching_message = latest(messages_with_matching_id(messages=client.messages.list(),
#                                                                _id=account_id))['body']
#
#     # checks if the message can be split
#     if splitting_string not in latest_matching_message:
#         p_e("Splitting string '{0}' not found in latest message '{1}'".format(splitting_string,
#                                                                               latest_matching_message))
#         raise ValueError
#
#     # splits the message
#     trash, otp = latest_matching_message.split(splitting_string)
#
#     return otp

def messages_to_number_from_today(telephone: str=environ['TELEPHONE_NUMBER']) -> [MessageInstance]:

    """
        gets messages with the matching telephone number from an array of messages sent on this day
    :param telephone:
        +4912345 type of number

    :return:
        array of messages
    """
    import re
    account_sid = environ['TWILIO_ACCOUNT_SID']
    auth_token = environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    if telephone.startswith("0"):
        # replaces the starting '0' with the DE direction number
        telephone = re.sub('^%s' % "0", "+49", telephone)

    return client.messages.list(to=telephone,
                                date_sent=date.today())


def messages_with_matching_id(messages: [MessageInstance], _id: str) -> [MessageInstance]:
    """
        filters out messages with the matching id from an array of messages
    :param messages:
        initial array of messages
    :param _id:
        ID used to filter the messages out

    :return:
        array of messages
    """
    import ast
    matching_messages = []

    # TODO: Check how the messages store the IDs

    for m in messages:
        ref = ast.literal_eval(m['reference'])
        if 'account_id' in ref and ref['account_id'] == _id:
            print("Appending matching message:\n{0}".format(m))
            matching_messages.append(m)
        if 'registration_id' in ref and ref['registration_id'] == _id:
            print("Appending matching message:\n{0}".format(m))
            matching_messages.append(m)

    if len(matching_messages) == 0:
        print("WARNING! No matching messages found")

    return matching_messages


def latest(messages: [MessageInstance]):
    """
        gets the most recent message from a list
    :param messages:
        array of messages

    :return:
        most recent message
    """

    # initialize with the first message
    # TODO: check how the messages dates are stored and formatted
    dt1 = messages[0].date_updated
    latest_message = messages[0]

    # iterate over all messages and check which is the latest
    for message in messages:
        dt2 = message.date_updated
        # print("Checking dt2={0}".format(dt2))
        if dt2 > dt1:
            dt1 = dt2
            latest_message = message

    return latest_message
