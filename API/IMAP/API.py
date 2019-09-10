from API.IMAP import User
from API.IMAP import Tariff
from API.IMAP.Printing import log, p_e, p_w
from API.IMAP.Printing import Printable
from API.IMAP.Setup import log_path, p_logs, f___log, f__warn, f_error, f_debug

import socket
import imaplib
import locale
from datetime import date
import time
import re
from os import environ


_imap_host = 'mail.on-testing.de'
_date_query_formatting = "%d-%b-%Y"
M_BCHMURA = 'bchmura'
M_ZMERTES_L = "zmertes-linux"
M_ZMERTES_W = "zmertes-windows"
MACHINES = {
    M_BCHMURA:
        "onnb-bchmura",
    M_ZMERTES_W:
        "onnb-016",
    M_ZMERTES_L:
        "onnb-zmertes",
    'selenium hub':
        ""}


def get_emails(recipient: str,
               date_from: date=None,
               date_until: date=None,
               subject: str=None,
               sleep_time: int=0) \
        -> [str]:
    """
        Returns a list of emails that match given criteria.
        Needs an environment variable holding the access key to the Mandrill API
    :param recipient: for the DELIVERED-TO parameter
    :param date_from: for the SINCE parameter
    :param date_until: for the BEFORE parameter
        M.search(None, '(SINCE "01-Jan-2012")')
        M.search(None, '(BEFORE "01-Jan-2012")')
        M.search(None, '(SINCE "01-Jan-2012" BEFORE "02-Jan-2012")')
    :param subject: for the SUBJECT parameter
    :param sleep_time: how long should the method wait before trying to get emails
    :return: list of messages as strings
    """

    from ftfy import fix_text
    _imap_user = environ['TEST_USER']
    _imap_pass = environ['TEST_PASSWORD']
    _machine = socket.gethostname()
    # handle the locale settings for the Windows machine

    # if _machine == MACHINES[M_ZMERTES_W]:
    #     _locale_string = "en-US"
    # locale.setlocale(locale.LC_TIME, _locale_string)

    if _machine == MACHINES[M_ZMERTES_L]:
        _locale_string = "en_US.UTF-8"
    locale.setlocale(locale.LC_TIME, _locale_string)


    imap = imaplib.IMAP4_SSL(_imap_host)
    imap.login(_imap_user, _imap_pass)
    imap.select('Inbox')

    _query = 'TO "{0}"'.format(recipient)
    if date_from is not None:
        _query += ' SINCE "{0}"'.format(date_from.strftime(_date_query_formatting))
    if date_until is not None:
        _query += ' BEFORE "{0}"'.format(date_until.strftime(_date_query_formatting))

    _locale_string = "de_DE.UTF-8"
    # handle the locale settings for the Windows machine
    if _machine == MACHINES[M_ZMERTES_W]:
        _locale_string = "deu-DE"
    locale.setlocale(locale.LC_TIME, _locale_string)

    if _machine == MACHINES[M_ZMERTES_L]:
        _locale_string = "de_DE.UTF-8"
    locale.setlocale(locale.LC_TIME, _locale_string)

    if subject is not None:
        _query += ' SUBJECT "{0}"'.format(subject)
    _query = '({0})'.format(_query)
    _full_query = u'{0}'.format(_query).encode('utf-8')
    print('Full Query = {0}'.format(_full_query))

    # The server seems to need some time to notice it has sent an email
    log("Giving the server {0}s to handle the email".format(sleep_time))
    time.sleep(sleep_time)
    log("Getting emails for query: '{0}'".format(_full_query))

    _messages = []
    # this should try up to 120 times, once every 2s to get a non-empty search result
    for iteration in range(0, 120):

        tmp, data = imap.uid('SEARCH', 'CHARSET', 'UTF-8', _full_query)

        _messages = []

        for num in data[0].split():
            tmp, data = imap.fetch(num, '(BODY[TEXT])')
            if type(data[0][1]) == int:
                p_e("The contents of 'data' seem to be incorrect.\n\nData:\n{0}\n\n".format(data))
                raise ValueError
            else:
                _raw = data[0][1].decode('utf-8')
                _fixed = fix_text(_raw.replace('=C3=A4', 'ä').replace('=C3=BC', 'ü').replace('=C3=B6', 'ö').
                                  replace('=C3=9F', 'ß').replace('=3D', '=').
                                  replace('=09', '\t').replace('=\n', ''))
                _messages.append(_fixed.replace('=C3=A4', 'ä').replace('=C3=BC', 'ü').replace('=C3=B6', 'ö').
                                 replace('=C3=9F', 'ß').replace('=3D', '=').replace('=09', '\t').replace('=\n', ''))
                break

        # in case the list of search results is not-empty - return it
        if len(_messages) > 0:
            log("Attempt #{0}/120... SUCCESS".format(iteration))
            imap.close()
            return _messages
        log("Attempt #{0}/120... failed".format(iteration))

        time.sleep(2)

    imap.close()
    return _messages


def get_confirmation_link_for_recipient(environment_string: str,
                                        recipient: str,
                                        date_from: date=date.today(),
                                        date_until: date=None,
                                        subject: str="Bitte aktiviere deinen Account",
                                        sleep_time: int=0) \
        -> str or None:
    """
        Returns a list of emails that match given criteria.
        Needs an environment variable holding the access key to the Mandrill API
    :param environment_string: what environment is expected
    :param recipient: for the FROM parameter
    :param date_from: for the SINCE parameter
    :param date_until: for the BEFORE parameter
        M.search(None, '(SINCE "01-Jan-2012")')
        M.search(None, '(BEFORE "01-Jan-2012")')
        M.search(None, '(SINCE "01-Jan-2012" BEFORE "02-Jan-2012")')
    :param subject: for the SUBJECT parameter
    :param sleep_time: how long should the method wait before trying to get emails
    :return: confirmation_url or None
    """

    emails = get_emails(recipient=recipient,
                        date_from=date_from,
                        date_until=date_until,
                        subject=subject,
                        sleep_time=sleep_time)

    email = emails[0]
    # get the email_id for further processing
    if len(emails) == 1:
        log("Found one confirmation email")
    elif len(emails) > 1:
        log("Found multiple confirmation emails. Returning the latest one...")
        # TODO: implement a correct 'latest' method
        # email = latest(emails)
    else:
        p_e("No emails were found!")

    if email is not None:
        # email = email.replace('=C3=A4', 'ä').replace('=C3=BC', 'ü').replace('=C3=B6', 'ö').replace('=C3=9F', 'ß').\
        #     replace('=3D', '=').replace('=09', '\t').replace('=\n', '')
        url_regex = r'<a href="(https:\/\/' + environment_string + '\/.*registration_id=.*?)" .*>'
        results = re.findall(url_regex, email)
        reg_url = results[0]
        return reg_url

    p_e("Something went wrong! Inspect code!")
    raise ValueError


def get_registration_id_for_recipient(environment_string: str,
                                      recipient: str,
                                      date_from: date=date.today(),
                                      date_until: date=None,
                                      subject: str="Bitte aktiviere deinen Account",
                                      sleep_time: int=0) \
        -> str or None:

    emails = get_emails(recipient=recipient,
                        date_from=date_from,
                        date_until=date_until,
                        subject=subject,
                        sleep_time=sleep_time)

    email = emails[0]
    # get the email_id for further processing
    if len(emails) == 1:
        log("Found one confirmation email")
    elif len(emails) > 1:
        log("Found multiple confirmation emails. Returning the latest one...")
        # TODO: implement a correct 'latest' method
        # email = latest(emails)
    else:
        p_e("No emails were found!")

    if email is not None:
        # email = email.replace('=C3=A4', 'ä').replace('=C3=BC', 'ü').replace('=C3=B6', 'ö').replace('=C3=9F', 'ß').\
        #     replace('=3D', '=').replace('=09', '\t').replace('=\n', '')
        id_regex = r'<a href="(https:\/\/' + environment_string + '\/.*registration_id=)(.*?)" .*>'
        results = re.findall(id_regex, email)
        id_url = results[0][1]
        return id_url

    p_e("Something went wrong! Inspect code!")
    raise ValueError


def get_consultation_email(recipient: str,
                           date_from: date=date.today(),
                           date_until: date=None,
                           sleep_time: int=0) -> bool:
    """
        Returns True/False based on whether the consultation email has/-not been found
    :param recipient: for the FROM parameter
    :param date_from: for the SINCE parameter
    :param date_until: for the BEFORE parameter
    :param sleep_time: how many seconds to wait before calling the API (time for the server to handle the emails)
    :return:
    """

    _texts = ["Deine Beratung ist schon unterwegs.",
              "du hast dir für deine telefonische Beratung den",
              "Halte einfach dein Telefon bereit - wir melden uns dann bei dir.",
              "Sollte der Termin doch nich passen, sag uns kurz Bescheid und wir finden eine Alternative.",
              "Per E-Mail an beratung@ottonova.de oder ruf uns an unter 089/12140712",
              "Hast du Fragen oder Anliegen?",
              "Schreib uns gerne."]

    _email_title = "Deine persönliche Beratung"

    return get_email(recipient=recipient,
                     subject=_email_title,
                     email_comparison_list=_texts,
                     date_from=date_from,
                     date_until=date_until,
                     sleep_time=sleep_time)


def get_consultation_finished_email(recipient: str,
                                    date_from: date = date.today(),
                                    date_until: date = None,
                                    sleep_time: int=30) -> bool:
    """
        Returns True/False based on whether the consultation-completed email has/-not been found
    :param recipient: the address of the recipient
    :param date_from: SINCE parameter
    :param date_until: BEFORE parameter
    :param sleep_time: how many seconds to wait before calling the API (time for the server to handle the emails)
    :return:
    """

    _texts = ["Vielen Dank für deine Zeit!",
              "Jetzt geht es weiter mit einem Telefonat zu noch offenen Fragen.",
              "Du bekommst hierzu in Kürze einen Anruf von uns.",
              "Hast du Fragen oder Anliegen?",
              "Schreib uns gerne."]

    _email_title = "Beratung abgeschlossen"

    return get_email(recipient=recipient,
                     subject=_email_title,
                     email_comparison_list=_texts,
                     date_from=date_from,
                     date_until=date_until,
                     sleep_time=sleep_time)


def get_offer_email(recipient: str,
                    date_from: date=date.today(),
                    date_until: date=None,
                    sleep_time: int=0) -> bool:
    """
        Returns True/False based on whether the offer email has/-not been found
    :param recipient: the address of the recipient
    :param date_from: SINCE parameter
    :param date_until: BEFORE parameter
    :param sleep_time: how many seconds to wait before calling the API (time for the server to handle the emails)
    :return:
    """

    _texts = ["Vielen Dank und weiter geht's!",
              "Wir haben alle nötigen Informationen von dir erhalten.",
              "Deinen aktuellen Gesundheitsstatus merken wir uns ab heute 4 Wochen lang vor.",
              "Bis dahin hast du die Möglichkeit, deine Angaben in unserer Zusammenfassung zu überprüfen.",
              "Klicke dazu einfach auf den nachfolgenden Button.",
              "Zu deinem Ergebnis",
              "Hast du Fragen oder Anliegen?",
              "Schreib uns gerne."]
    _email_title = "Ergebnis deiner personalisierten Risikoprüfung"

    return get_email(recipient=recipient,
                     subject=_email_title,
                     email_comparison_list=_texts,
                     date_from=date_from,
                     date_until=date_until,
                     sleep_time=sleep_time)


def get_tariff_recommendation_email(user: User,
                                    tariff: Tariff,
                                    date_from: date=date.today(),
                                    date_until: date=None,
                                    sleep_time: int=0) -> bool:
    """
        Returns True/False based on whether the tariff-recommendation offer email has/-not been found
    :param user: the user for whom the email is to be retrieved
    :param tariff: the tariff that the user has booked
    :param date_from: SINCE parameter
    :param date_until: BEFORE parameter
    :param sleep_time: how many seconds to wait before calling the API (time for the server to handle the emails)
    :return:
    """
    locale.setlocale(locale.LC_MONETARY, 'de_DE.UTF-8')

    _texts = ["Hallo {0}".format(user.forename),
              "wir freuen uns sehr, dass dich unsere private Krankenversicherung neugierig gemacht hat!",
              "Hier ist unser Angebot für dich wenn du zum {0} startest.".format(
                  user.insurance_start_date.strftime("%Y-%m-%d")),
              "Dein Beitrag als Versicherungsnehmer",
              "(geb. {0})".format(user.date_of_birth.strftime("%d.%m.%Y")),
              "{0}".format(tariff.name.replace("Tariff", "")),
              "{0}".format(locale.currency(tariff.price)),
              "Hast du Fragen oder Anliegen?",
              "Schreib uns gerne."]
    _email_title = "Dein persönliches Angebot"

    return get_email(recipient=user.email,
                     subject=_email_title,
                     email_comparison_list=_texts,
                     date_from=date_from,
                     date_until=date_until,
                     sleep_time=sleep_time)


# TODO: Refactor or remove
def get_email(recipient: str,
              subject: str,
              email_comparison_list: [str],
              date_from: date=date.today(),
              date_until: date=None,
              sleep_time: int=0) -> bool:
    """
        Returns True/False based on whether the offer email has/-not been found
    :param recipient: FROM parameter
    :param subject: the title of the email. MAKE SURE IT LOOKS LIKE '"Title"'
    :param email_comparison_list: the contents of the email stored as a list of strings
    :param date_from: SINCE parameter
    :param date_until: BEFORE parameter
    :param sleep_time: how many seconds to wait before calling the API (time for the server to handle the emails)
    :return:
    """

    emails = get_emails(recipient=recipient,
                        date_from=date_from,
                        date_until=date_until,
                        subject=subject,
                        sleep_time=sleep_time)

    email = emails[0]
    # get the email_id for further processing
    if len(emails) == 1:
        log("Found one email")
        # email_id = emails[0]['_id']
    elif len(emails) > 1:
        log("Found multiple emails. Returning the latest one...")
        # email_id = latest(emails)['_id']
    else:
        p_e("No emails were found!")

    time.sleep(2)

    _result = True
    for t in email_comparison_list:
        if t not in email:
            _result = False
            p_w("The following text was not found in the email!\n{0}".format(t))

    log("The email contained the required text elements.")
    return _result


# TODO: write an appropriate 'latest' method using the message Date:
def latest(messages: []):
    _ts = 0
    the_message = messages[0]
    for message in messages:
        _ts_new = message['ts']
        if _ts_new > _ts:
            _ts = _ts_new
            the_message = message
    return the_message
