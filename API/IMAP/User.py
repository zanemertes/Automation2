from API.IMAP.Printing import log, p_e, p_w, p_d
from API.IMAP.Printing import Printable
import locale
import datetime
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import random
import re

DATE_YMD = "%Y-%m-%d"
E_STAGING = 'staging'
E_TEST = 'test'

#telephone = environ['TELEPHONE_NUMBER']
password = "7Zeichen"

C_NON_EU = "NON_EU"
C_EU = "EU"
C_DE = "DE"
C_ANY = "Any"
C_OPTIONS = [C_DE, C_EU, C_NON_EU]

countries = [{'label': 'Afghanistan', 'value': 'AF', 'option': C_NON_EU},
             {'label': 'Albanien', 'value': 'AL', 'option': C_NON_EU},
             {'label': 'Algerien', 'value': 'DZ', 'option': C_NON_EU},
             {'label': 'Amerikanisch-Samoa', 'value': 'AS', 'option': C_NON_EU},
             {'label': 'Andorra', 'value': 'AD', 'option': C_NON_EU},
             {'label': 'Angola', 'value': 'AO', 'option': C_NON_EU},
             {'label': 'Anguilla', 'value': 'AI', 'option': C_NON_EU},
             {'label': 'Antarktis', 'value': 'AQ', 'option': C_NON_EU},
             {'label': 'Antigua und Barbuda', 'value': 'AG', 'option': C_NON_EU},
             {'label': 'Argentinien', 'value': 'AR', 'option': C_NON_EU},
             {'label': 'Armenien', 'value': 'AM', 'option': C_NON_EU},
             {'label': 'Aruba', 'value': 'AW', 'option': C_NON_EU},
             {'label': 'Australien', 'value': 'AU', 'option': C_NON_EU},
             {'label': 'Österreich', 'value': 'AT', 'option': C_EU},
             {'label': 'Aserbaidschan', 'value': 'AZ', 'option': C_NON_EU},
             {'label': 'Bahamas', 'value': 'BS', 'option': C_NON_EU},
             {'label': 'Bahrain', 'value': 'BH', 'option': C_NON_EU},
             {'label': 'Bangladesch', 'value': 'BD', 'option': C_NON_EU},
             {'label': 'Barbados', 'value': 'BB', 'option': C_NON_EU},
             {'label': 'Weißrussland', 'value': 'BY', 'option': C_NON_EU},
             {'label': 'Belgien', 'value': 'BE', 'option': C_EU},
             {'label': 'Belize', 'value': 'BZ', 'option': C_NON_EU},
             {'label': 'Benin', 'value': 'BJ', 'option': C_NON_EU},
             {'label': 'Bermuda', 'value': 'BM', 'option': C_NON_EU},
             {'label': 'Bhutan', 'value': 'BT', 'option': C_NON_EU},
             {'label': 'Bolivien', 'value': 'BO', 'option': C_NON_EU},
             {'label': 'Bosnien und Herzegowina', 'value': 'BA', 'option': C_NON_EU},
             {'label': 'Botswana', 'value': 'BW', 'option': C_NON_EU},
             {'label': 'Bouvetinsel', 'value': 'BV', 'option': C_NON_EU},
             {'label': 'Brasilien', 'value': 'BR', 'option': C_NON_EU},
             {'label': 'Britisches Territorium im Indischen Ozean', 'value': 'IO', 'option': C_NON_EU},
             {'label': 'Brunei', 'value': 'BN', 'option': C_NON_EU},
             {'label': 'Bulgarien', 'value': 'BG', 'option': C_EU},
             {'label': 'Burkina Faso', 'value': 'BF', 'option': C_NON_EU},
             {'label': 'Burundi', 'value': 'BI', 'option': C_NON_EU},
             {'label': 'Kambodscha', 'value': 'KH', 'option': C_NON_EU},
             {'label': 'Kamerun', 'value': 'CM', 'option': C_NON_EU},
             {'label': 'Kanada', 'value': 'CA', 'option': C_NON_EU},
             {'label': 'Kapverdische Inseln', 'value': 'CV', 'option': C_NON_EU},
             {'label': 'Kaimaninseln', 'value': 'KY', 'option': C_NON_EU},
             {'label': 'Zentralafrikanische Republik', 'value': 'CF', 'option': C_NON_EU},
             {'label': 'Tschad', 'value': 'TD', 'option': C_NON_EU},
             {'label': 'Chile', 'value': 'CL', 'option': C_NON_EU},
             {'label': 'China', 'value': 'CN', 'option': C_NON_EU},
             {'label': 'Weihnachtsinsel', 'value': 'CX', 'option': C_NON_EU},
             {'label': 'Kokosinseln', 'value': 'CC', 'option': C_NON_EU},
             {'label': 'Kolumbien', 'value': 'CO', 'option': C_NON_EU},
             {'label': 'Komoren', 'value': 'KM', 'option': C_NON_EU},
             {'label': 'Kongo', 'value': 'CG', 'option': C_NON_EU},
             {'label': 'Demokratische Republik Kongo', 'value': 'CD', 'option': C_NON_EU},
             {'label': 'Cookinseln', 'value': 'CK', 'option': C_NON_EU},
             {'label': 'Costa Rica', 'value': 'CR', 'option': C_NON_EU},
             {'label': 'Elfenbeinküste', 'value': 'CI', 'option': C_NON_EU},
             {'label': 'Kroatien', 'value': 'HR', 'option': C_EU},
             {'label': 'Kuba', 'value': 'CU', 'option': C_NON_EU},
             {'label': 'Zypern', 'value': 'CY', 'option': C_EU},
             {'label': 'Tschechische Republik', 'value': 'CZ', 'option': C_EU},
             {'label': 'Dänemark', 'value': 'DK', 'option': C_EU},
             {'label': 'Dschibuti', 'value': 'DJ', 'option': C_NON_EU},
             {'label': 'Dominica', 'value': 'DM', 'option': C_NON_EU},
             {'label': 'Dominikanische Republik', 'value': 'DO', 'option': C_NON_EU},
             {'label': 'Ecuador', 'value': 'EC', 'option': C_NON_EU},
             {'label': 'Ägypten', 'value': 'EG', 'option': C_NON_EU},
             {'label': 'El Salvador', 'value': 'SV', 'option': C_NON_EU},
             {'label': 'Äquatorialguinea', 'value': 'GQ', 'option': C_NON_EU},
             {'label': 'Eritrea', 'value': 'ER', 'option': C_NON_EU},
             {'label': 'Estland', 'value': 'EE', 'option': C_EU},
             {'label': 'Äthiopien', 'value': 'ET', 'option': C_NON_EU},
             {'label': 'Falklandinseln', 'value': 'FK', 'option': C_NON_EU},
             {'label': 'Färöer', 'value': 'FO', 'option': C_NON_EU},
             {'label': 'Fidschi', 'value': 'FJ', 'option': C_NON_EU},
             {'label': 'Finnland', 'value': 'FI', 'option': C_EU},
             {'label': 'Frankreich', 'value': 'FR', 'option': C_EU},
             {'label': 'Französisch-Guayana', 'value': 'GF', 'option': C_NON_EU},
             {'label': 'Französisch-Polynesien', 'value': 'PF', 'option': C_NON_EU},
             {'label': 'Französische Süd- und Antarktisgebiete', 'value': 'TF', 'option': C_NON_EU},
             {'label': 'Gabun', 'value': 'GA', 'option': C_NON_EU},
             {'label': 'Gambia', 'value': 'GM', 'option': C_NON_EU},
             {'label': 'Georgien', 'value': 'GE', 'option': C_NON_EU},
             {'label': 'Deutschland', 'value': 'DE', 'option': C_DE},
             {'label': 'Ghana', 'value': 'GH', 'option': C_NON_EU},
             {'label': 'Gibraltar', 'value': 'GI', 'option': C_NON_EU},
             {'label': 'Griechenland', 'value': 'GR', 'option': C_EU},
             {'label': 'Grönland', 'value': 'GL', 'option': C_NON_EU},
             {'label': 'Grenada', 'value': 'GD', 'option': C_NON_EU},
             {'label': 'Guadeloupe', 'value': 'GP', 'option': C_NON_EU},
             {'label': 'Guam', 'value': 'GU', 'option': C_NON_EU},
             {'label': 'Guatemala', 'value': 'GT', 'option': C_NON_EU},
             {'label': 'Guinea', 'value': 'GN', 'option': C_NON_EU},
             {'label': 'Guinea-Bissau', 'value': 'GW', 'option': C_NON_EU},
             {'label': 'Guyana', 'value': 'GY', 'option': C_NON_EU},
             {'label': 'Haiti', 'value': 'HT', 'option': C_NON_EU},
             {'label': 'Heard und McDonaldinseln', 'value': 'HM', 'option': C_NON_EU},
             {'label': 'Vatikanstadt', 'value': 'VA', 'option': C_NON_EU},
             {'label': 'Honduras', 'value': 'HN', 'option': C_NON_EU},
             {'label': 'Hong Kong', 'value': 'HK', 'option': C_NON_EU},
             {'label': 'Ungarn', 'value': 'HU', 'option': C_EU},
             {'label': 'Island', 'value': 'IS', 'option': C_NON_EU},
             {'label': 'Indien', 'value': 'IN', 'option': C_NON_EU},
             {'label': 'Indonesien', 'value': 'ID', 'option': C_NON_EU},
             {'label': 'Iran', 'value': 'IR', 'option': C_NON_EU},
             {'label': 'Irak', 'value': 'IQ', 'option': C_NON_EU},
             {'label': 'Irland', 'value': 'IE', 'option': C_EU},
             {'label': 'Israel', 'value': 'IL', 'option': C_NON_EU},
             {'label': 'Italien', 'value': 'IT', 'option': C_EU},
             {'label': 'Jamaika', 'value': 'JM', 'option': C_NON_EU},
             {'label': 'Japan', 'value': 'JP', 'option': C_NON_EU},
             {'label': 'Jordanien', 'value': 'JO', 'option': C_NON_EU},
             {'label': 'Kasachstan', 'value': 'KZ', 'option': C_NON_EU},
             {'label': 'Kenia', 'value': 'KE', 'option': C_NON_EU},
             {'label': 'Kiribati', 'value': 'KI', 'option': C_NON_EU},
             {'label': 'Nordkorea', 'value': 'KP', 'option': C_NON_EU},
             {'label': 'Südkorea', 'value': 'KR', 'option': C_NON_EU},
             {'label': 'Kuwait', 'value': 'KW', 'option': C_NON_EU},
             {'label': 'Kirgisistan', 'value': 'KG', 'option': C_NON_EU},
             {'label': 'Laos', 'value': 'LA', 'option': C_NON_EU},
             {'label': 'Lettland', 'value': 'LV', 'option': C_EU},
             {'label': 'Libanon', 'value': 'LB', 'option': C_NON_EU},
             {'label': 'Lesotho', 'value': 'LS', 'option': C_NON_EU},
             {'label': 'Liberia', 'value': 'LR', 'option': C_NON_EU},
             {'label': 'Libyen', 'value': 'LY', 'option': C_NON_EU},
             {'label': 'Liechtenstein', 'value': 'LI', 'option': C_NON_EU},
             {'label': 'Litauen', 'value': 'LT', 'option': C_EU},
             {'label': 'Luxembourg', 'value': 'LU', 'option': C_EU},
             {'label': 'Macau', 'value': 'MO', 'option': C_NON_EU},
             {'label': 'Mazedonien', 'value': 'MK', 'option': C_NON_EU},
             {'label': 'Madagaskar', 'value': 'MG', 'option': C_NON_EU},
             {'label': 'Malawi', 'value': 'MW', 'option': C_NON_EU},
             {'label': 'Malaysia', 'value': 'MY', 'option': C_NON_EU},
             {'label': 'Malediven', 'value': 'MV', 'option': C_NON_EU},
             {'label': 'Mali', 'value': 'ML', 'option': C_NON_EU},
             {'label': 'Malta', 'value': 'MT', 'option': C_EU},
             {'label': 'Marshallinseln', 'value': 'MH', 'option': C_NON_EU},
             {'label': 'Martinique', 'value': 'MQ', 'option': C_NON_EU},
             {'label': 'Mauretanien', 'value': 'MR', 'option': C_NON_EU},
             {'label': 'Mauritius', 'value': 'MU', 'option': C_NON_EU},
             {'label': 'Mayotte', 'value': 'YT', 'option': C_NON_EU},
             {'label': 'Mexiko', 'value': 'MX', 'option': C_NON_EU},
             {'label': 'Mikronesien', 'value': 'FM', 'option': C_NON_EU},
             {'label': 'Moldawien', 'value': 'MD', 'option': C_NON_EU},
             {'label': 'Monaco', 'value': 'MC', 'option': C_NON_EU},
             {'label': 'Mongolei', 'value': 'MN', 'option': C_NON_EU},
             {'label': 'Montenegro', 'value': 'ME', 'option': C_NON_EU},
             {'label': 'Montserrat', 'value': 'MS', 'option': C_NON_EU},
             {'label': 'Marokko', 'value': 'MA', 'option': C_NON_EU},
             {'label': 'Mosambik', 'value': 'MZ', 'option': C_NON_EU},
             {'label': 'Myanmar', 'value': 'MM', 'option': C_NON_EU},
             {'label': 'Namibia', 'value': 'NA', 'option': C_NON_EU},
             {'label': 'Nauru', 'value': 'NR', 'option': C_NON_EU},
             {'label': 'Nepal', 'value': 'NP', 'option': C_NON_EU},
             {'label': 'Niederlande', 'value': 'NL', 'option': C_EU},
             {'label': 'Niederländische Antillen', 'value': 'AN', 'option': C_NON_EU},
             {'label': 'Neukaledonien', 'value': 'NC', 'option': C_NON_EU},
             {'label': 'Neuseeland', 'value': 'NZ', 'option': C_NON_EU},
             {'label': 'Nicaragua', 'value': 'NI', 'option': C_NON_EU},
             {'label': 'Niger', 'value': 'NE', 'option': C_NON_EU},
             {'label': 'Nigeria', 'value': 'NG', 'option': C_NON_EU},
             {'label': 'Niue', 'value': 'NU', 'option': C_NON_EU},
             {'label': 'Norfolkinsel', 'value': 'NF', 'option': C_NON_EU},
             {'label': 'Nördliche Marianen', 'value': 'MP', 'option': C_NON_EU},
             {'label': 'Norwegen', 'value': 'NO', 'option': C_NON_EU},
             {'label': 'Oman', 'value': 'OM', 'option': C_NON_EU},
             {'label': 'Pakistan', 'value': 'PK', 'option': C_NON_EU},
             {'label': 'Palau', 'value': 'PW', 'option': C_NON_EU},
             {'label': 'Palästinensische Autonomiegebiete', 'value': 'PS', 'option': C_NON_EU},
             {'label': 'Panama', 'value': 'PA', 'option': C_NON_EU},
             {'label': 'Papua-Neuguinea', 'value': 'PG', 'option': C_NON_EU},
             {'label': 'Paraguay', 'value': 'PY', 'option': C_NON_EU},
             {'label': 'Peru', 'value': 'PE', 'option': C_NON_EU},
             {'label': 'Philippinen', 'value': 'PH', 'option': C_NON_EU},
             {'label': 'Pitcairn', 'value': 'PN', 'option': C_NON_EU},
             {'label': 'Polen', 'value': 'PL', 'option': C_EU},
             {'label': 'Portugal', 'value': 'PT', 'option': C_EU},
             {'label': 'Puerto Rico', 'value': 'PR', 'option': C_NON_EU},
             {'label': 'Katar', 'value': 'QA', 'option': C_NON_EU},
             {'label': 'Reunion', 'value': 'RE', 'option': C_NON_EU},
             {'label': 'Rumänien', 'value': 'RO', 'option': C_EU},
             {'label': 'Russland', 'value': 'RU', 'option': C_NON_EU},
             {'label': 'Ruanda', 'value': 'RW', 'option': C_NON_EU},
             {'label': 'St. Helena', 'value': 'SH', 'option': C_NON_EU},
             {'label': 'St. Kitts und Nevis', 'value': 'KN', 'option': C_NON_EU},
             {'label': 'St. Lucia', 'value': 'LC', 'option': C_NON_EU},
             {'label': 'Saint-Pierre und Miquelon', 'value': 'PM', 'option': C_NON_EU},
             {'label': 'St. Vincent und die Grenadinen', 'value': 'VC', 'option': C_NON_EU},
             {'label': 'Samoa', 'value': 'WS', 'option': C_NON_EU},
             {'label': 'San Marino', 'value': 'SM', 'option': C_NON_EU},
             {'label': 'São Tomé und Príncipe', 'value': 'ST', 'option': C_NON_EU},
             {'label': 'Saudi-Arabien', 'value': 'SA', 'option': C_NON_EU},
             {'label': 'Senegal', 'value': 'SN', 'option': C_NON_EU},
             {'label': 'Serbien', 'value': 'RS', 'option': C_NON_EU},
             {'label': 'Seychellen', 'value': 'SC', 'option': C_NON_EU},
             {'label': 'Sierra Leone', 'value': 'SL', 'option': C_NON_EU},
             {'label': 'Singapur', 'value': 'SG', 'option': C_NON_EU},
             {'label': 'Slowakei', 'value': 'SK', 'option': C_EU},
             {'label': 'Slowenien', 'value': 'SI', 'option': C_EU},
             {'label': 'Salomonen', 'value': 'SB', 'option': C_NON_EU},
             {'label': 'Somalia', 'value': 'SO', 'option': C_NON_EU},
             {'label': 'Südafrika', 'value': 'ZA', 'option': C_NON_EU},
             {'label': 'Südgeorgien und die Südlichen Sandwichinseln', 'value': 'GS', 'option': C_NON_EU},
             {'label': 'Spanien', 'value': 'ES', 'option': C_NON_EU},
             {'label': 'Sri Lanka', 'value': 'LK', 'option': C_NON_EU},
             {'label': 'Sudan', 'value': 'SD', 'option': C_NON_EU},
             {'label': 'Suriname', 'value': 'SR', 'option': C_NON_EU},
             {'label': 'Spitzbergen und Jan Mayen', 'value': 'SJ', 'option': C_NON_EU},
             {'label': 'Swasiland', 'value': 'SZ', 'option': C_NON_EU},
             {'label': 'Schweden', 'value': 'SE', 'option': C_EU},
             {'label': 'Schweiz', 'value': 'CH', 'option': C_EU},
             {'label': 'Syrien', 'value': 'SY', 'option': C_NON_EU},
             {'label': 'Taiwan', 'value': 'TW', 'option': C_NON_EU},
             {'label': 'Tadschikistan', 'value': 'TJ', 'option': C_NON_EU},
             {'label': 'Tansania', 'value': 'TZ', 'option': C_NON_EU},
             {'label': 'Thailand', 'value': 'TH', 'option': C_NON_EU},
             {'label': 'Togo', 'value': 'TG', 'option': C_NON_EU},
             {'label': 'Tokelau', 'value': 'TK', 'option': C_NON_EU},
             {'label': 'Tonga', 'value': 'TO', 'option': C_NON_EU},
             {'label': 'Trinidad und Tobago', 'value': 'TT', 'option': C_NON_EU},
             {'label': 'Tunesien', 'value': 'TN', 'option': C_NON_EU},
             {'label': 'Türkei', 'value': 'TR', 'option': C_NON_EU},
             {'label': 'Turkmenistan', 'value': 'TM', 'option': C_NON_EU},
             {'label': 'Turks und Caicos-Inseln', 'value': 'TC', 'option': C_NON_EU},
             {'label': 'Tuvalu', 'value': 'TV', 'option': C_NON_EU},
             {'label': 'Uganda', 'value': 'UG', 'option': C_NON_EU},
             {'label': 'Ukraine', 'value': 'UA', 'option': C_NON_EU},
             {'label': 'Vereinigte Arabische Emirate', 'value': 'AE', 'option': C_NON_EU},
             {'label': 'Vereinigtes Königreich', 'value': 'GB', 'option': C_EU},
             {'label': 'Vereinigte Staaten', 'value': 'US', 'option': C_NON_EU},
             {'label': 'Uruguay', 'value': 'UY', 'option': C_NON_EU},
             {'label': 'Usbekistan', 'value': 'UZ', 'option': C_NON_EU},
             {'label': 'Vanuatu', 'value': 'VU', 'option': C_NON_EU},
             {'label': 'Venezuela', 'value': 'VE', 'option': C_NON_EU},
             {'label': 'Vietnam', 'value': 'VN', 'option': C_NON_EU},
             {'label': 'Jungferninseln, Britisch', 'value': 'VG', 'option': C_NON_EU},
             {'label': 'Jungferninseln, U.S.', 'value': 'VI', 'option': C_NON_EU},
             {'label': 'Wallis und Futuna', 'value': 'WF', 'option': C_NON_EU},
             {'label': 'Westsahara', 'value': 'EH', 'option': C_NON_EU},
             {'label': 'Jemen', 'value': 'YE', 'option': C_NON_EU},
             {'label': 'Sambia', 'value': 'ZM', 'option': C_NON_EU},
             {'label': 'Simbabwe', 'value': 'ZW', 'option': C_NON_EU}]


def get_country_by_code(code: str) -> str or None:
    for c in countries:
        if c['value'] == code:
            return c['label']


def make_insurance_date(safe: bool) -> date:
    if safe:
        _new_insurance_date = (date.today() + timedelta(days=random.randint(14, 6 * 30)))
    else:
        # randomize 'too early' and 'too late'
        unsafe_type = random.randint(0, 1)
        # too early
        if unsafe_type == 0:
            _new_insurance_date = (date.today() + timedelta(days=random.randint(0, 14)))
        else:
            _new_insurance_date = (date.today() + timedelta(weeks=random.randint(29, 104)))
    log("Generated new insurance date = {0}".format(_new_insurance_date.strftime("%Y-%m-%d")))
    return _new_insurance_date


class BodyMassIndex(Printable):
    # TODO: Add DOB into BMI
    M_TOO_HIGH = 'severe overweight'
    M_HIGH = 'overweight'
    M_OK = 'healthy'
    M_LOW = 'underweight'
    M_TOO_LOW = 'severe underweight'
    MODES = [M_TOO_HIGH, M_HIGH, M_OK, M_LOW, M_TOO_LOW]
    G_MALE = 'male'
    G_FEMALE = 'female'
    GENDERS = [G_MALE, G_FEMALE]

    genders_summary = {G_MALE: 'Männlich',
                       G_FEMALE: 'Weiblich'}
    genders_summary_inv = {v: k for k, v in genders_summary.items()}

    @staticmethod
    def calculate_bmi(height: int, weight: int) \
            -> float:
        return weight * pow(height * 0.01, -2.0)

    @staticmethod
    def calculate_weight(height: int, bmi: float) \
            -> int:
        return int(bmi * pow(height * 0.01, 2.0))

    @staticmethod
    def calculate_height(weight: int, bmi: float) \
            -> int:
        return int(bmi * pow(weight, -12.0))

    @staticmethod
    def generate_height() \
            -> int:
        # generate a random height in cm
        height = random.randint(150, 200)
        # log something to be traceable
        log("Generated random height of '{0}'cm".format(height))
        return height

    @staticmethod
    def generate_weight_height_bmi(mode: str = "healthy") \
            -> (int, int, float, str):
        _bmi = BodyMassIndex.generate_bmi(mode=mode)
        _height = BodyMassIndex.generate_height()

        if _bmi is None:
            p_e("The BMI is not available but needed for generation of weight.")
            return None

        # generate the corresponding weight: w[kg] = BMI * h²[m]
        _weight = int(round(_bmi * pow(_height * 0.01, 2.0), 0))
        # log something to be traceable
        log("Generated random weight of '{0}'kg".format(_weight))

        return _weight, _height, _bmi, mode

    @staticmethod
    def generate_bmi(mode: str = "healthy") \
            -> float:
        if mode not in BodyMassIndex.MODES:
            p_e("The BMI mode {0} is not supported".format(mode))
        bmi = -1.0
        if mode == BodyMassIndex.M_TOO_LOW:
            bmi = random.randint(0, 160 - 1) * 0.1
        if mode == BodyMassIndex.M_LOW:
            bmi = random.randint(160, 185 - 1) * 0.1
        if mode == BodyMassIndex.M_OK:
            bmi = random.randint(185, 250 - 1) * 0.1
        if mode == BodyMassIndex.M_HIGH:
            bmi = random.randint(250, 300 - 1) * 0.1
        if mode == BodyMassIndex.M_TOO_HIGH:
            bmi = random.randint(300, 500 - 1) * 0.1
        bmi = round(bmi, 1)
        # log something to be traceable
        log("Generated random {1} BMI of '{0}'kg/m2".format(bmi, mode))
        return bmi

    @staticmethod
    def determine_mode_from_bmi(bmi: float) \
            -> str:
        _bmi = round(bmi, 1)
        if 0.0 <= _bmi < 16.0:
            return BodyMassIndex.M_TOO_LOW
        elif 16.0 <= _bmi < 18.5:
            return BodyMassIndex.M_LOW
        elif 18.5 <= _bmi < 25.0:
            return BodyMassIndex.M_OK
        elif 25.0 <= _bmi < 30.0:
            return BodyMassIndex.M_HIGH
        elif 30.0 <= _bmi < 50.0:
            return BodyMassIndex.M_TOO_HIGH

    def make_weight_height_bmi(self, mode: str = M_OK, weight: int = None, height: int = None):
        # prepare the BMI value for further calculations
        self.bmi = BodyMassIndex.generate_bmi(mode=mode)
        if self.bmi is None:
            p_e("The BMI is not available but needed for generation of weight.")
            return None

        # generate the height if not provided
        if height is None:
            self.height = self.generate_height()
        else:
            self.height = height

        # generate or calculate the weight to match the mode
        if weight is None:
            self.weight = self.calculate_weight(height=self.height, bmi=self.bmi)
        else:
            # in case the height/weight fit in the desired BMI-mode, store them
            if self.determine_mode_from_bmi(bmi=self.calculate_bmi(height=height, weight=weight)) == mode:
                self.weight = weight
            else:
                p_w("Weight was also given. It will be ignored for the sake of generating a correct BMI.")
                # generate the corresponding weight: w[kg] = BMI * h²[m]
                self.weight = int(round(self.bmi * pow(self.height * 0.01, 2.0), 0))

        # log something to be traceable
        log("Generated BMI set:\n\tweight: '{0}'kg\n\theight: '{1}'cm\n\tBMI: '{2}'kg/m²".format(
            self.weight,
            self.height,
            self.bmi))

    def __init__(self,
                 gender: str or None,
                 mode: str or None,
                 height: int or None,
                 weight: int or None,
                 bmi: float or None):
        locale.setlocale(locale.LC_NUMERIC, 'de_DE.UTF-8')

        # randomize gender selection if not provided or incorrect
        if gender is None or gender not in self.GENDERS:
            self.gender = random.choice(self.GENDERS)
        else:
            self.gender = gender

        # TODO: Make this generate everything - when mode is given - generate random according to mode and given height
        # If mode is not given, h and w must be given, bmi is calculated and proper mode is established ... etc.
        if mode is not None and mode not in BodyMassIndex.MODES:
            p_e("The mode {0} is not supported!".format(mode))

        if height is not None and weight is not None:
            self.height = height
            self.weight = weight
            # if only the two are given - calculate the bmi and mode
            if mode is None:
                self.bmi = self.calculate_bmi(height=height, weight=weight)
                self.mode = self.determine_mode_from_bmi(bmi=self.bmi)

        if mode is not None and not (height is None and weight is None):
            self.make_weight_height_bmi(mode=mode, weight=weight, height=height)

        if bmi is not None:
            self.bmi = bmi

        self.mode = mode

    @property
    def ui_comparable_gender(self) -> str:
        return self.genders_summary[self.gender]

    @property
    def ui_comparable_height(self) -> str:
        return "{0} m".format(locale.format("%.2f", round(self.height / 100.0, 2)))

    @property
    def ui_comparable_weight(self) -> str:
        return "{0} kg".format(locale.format("%.0f", round(self.weight, 2)))


class HealthImpairment(object):
    def __init__(self,
                 title: str,
                 question: str,
                 number: int,
                 answer: bool or None
                 ):
        self.title = title
        self.question = question
        self.number = number
        self.answer = answer


class NewHealthImpairments(object):
    i1_hearing = HealthImpairment(
        title='Hearing aid',
        question='Trägst du eine Hörhilfe?',
        number=1,
        answer=None)
    i2_implant = HealthImpairment(
        title='Body implant',
        question='Trägst du ein Körperimplantat? (Zahnimplantat zählt nicht)',
        number=2,
        answer=None)
    i3_prosthetic = HealthImpairment(
        title='Prosthetic',
        question='Trägst du eine Prothese? (Zahnprothese zählt nicht)',
        number=3,
        answer=None)
    i4_infertility = HealthImpairment(
        title='Infertility',
        question='Wurde bei dir eine Zeugungsunfähigkeit / Unfruchtbarkeit oder eingeschränkte '
                 'Zeugungsfähigkeit diagnostiziert?',
        number=4,
        answer=None)
    i5_disability = HealthImpairment(
        title='Disability',
        question='Besteht bei dir eine Behinderung, eine Fehlbildung eines Organs oder eine körperliche '
                 'Fehlbildung?',
        number=5,
        answer=None)
    i6_occupational = HealthImpairment(
        title='Occupational disability',
        question='Besteht bei dir eine Erwerbsminderung oder Berufsunfähigkeit?',
        number=6,
        answer=None)
    i7_military = HealthImpairment(
        title='Military injuries',
        question='Besteht bei dir eine Kriegs- oder Wehrdienstbeschädigung?',
        number=7,
        answer=None)
    i8_teeth = HealthImpairment(
        title='Missing teeth',
        question='Fehlen bei dir Zähne, die nicht ersetzt wurden? (Weisheitszähne zählen nicht)',
        number=8,
        answer=None)

    def __init__(self,
                 hearing_aid: bool = False,
                 body_implant: bool = False,
                 prosthetic: bool = False,
                 infertility: bool = False,
                 disability: bool = False,
                 occupational_disability: bool = False,
                 missing_teeth: bool = False,
                 military_injuries: bool = False):
        self.questions = [
            self.i1_hearing,
            self.i2_implant,
            self.i3_prosthetic,
            self.i4_infertility,
            self.i5_disability,
            self.i6_occupational,
            self.i7_military,
            self.i8_teeth
        ]
        self.i1_hearing.answer = hearing_aid
        self.i2_implant.answer = body_implant
        self.i3_prosthetic.answer = prosthetic
        self.i4_infertility.answer = infertility
        self.i5_disability.answer = disability
        self.i6_occupational.answer = occupational_disability
        self.i7_military.answer = military_injuries
        self.i8_teeth.answer = missing_teeth

    @property
    def hearing_aid(self) -> HealthImpairment:
        return self.questions[0]

    @property
    def body_implant(self) -> HealthImpairment:
        return self.questions[1]

    @property
    def prosthetic(self) -> HealthImpairment:
        return self.questions[2]

    @property
    def infertility(self) -> HealthImpairment:
        return self.questions[3]

    @property
    def disability(self) -> HealthImpairment:
        return self.questions[4]

    @property
    def occupational_disability(self) -> HealthImpairment:
        return self.questions[5]

    @property
    def missing_teeth(self) -> HealthImpairment:
        return self.questions[6]

    @property
    def military_injuries(self) -> HealthImpairment:
        return self.questions[7]

    @property
    def any_present(self) -> bool:
        for q in self.questions:
            if q.answer:
                return True
        return False

    @property
    def printable(self) -> str:
        _string = ""
        for q in self.questions:
            _string += "\t\t{0}.{1}\t=\t{2}\n".format(q.number, q.title, q.answer)
        return _string


class HealthImpairments(Printable):
    def __init__(self,
                 hearing_aid: bool = False,
                 body_implant: bool = False,
                 prosthetic: bool = False,
                 infertility: bool = False,
                 disability: bool = False,
                 occupational_disability: bool = False,
                 missing_teeth: bool = False,
                 military_injuries: bool = False):
        self.hearing_aid = hearing_aid
        self.body_implant = body_implant
        self.prosthetic = prosthetic
        self.infertility = infertility
        self.disability = disability
        self.occupational_disability = occupational_disability
        self.missing_teeth = missing_teeth
        self.military_injuries = military_injuries

    @property
    def any_impairments(self) -> bool:
        if self.hearing_aid or self.body_implant or self.prosthetic or self.infertility or \
                self.disability or self.occupational_disability or self.military_injuries or self.missing_teeth:
            return True
        return False


class HealthQuestion(object):
    def __init__(self,
                 title: str,
                 question: str,
                 additional_info: str or None,
                 number: int,
                 risk: bool,
                 answer: bool or None
                 ):
        self.title = title
        self.question = question
        self.additional_info = additional_info
        self.number = number
        self.risk = risk
        self.answer = answer


class HealthQuestions(object):
    answer_map_ui = {True: 'Ja',
                     False: 'Nein'}
    q1_medication = HealthQuestion(
        title='Medication',
        question='Hast du innerhalb der letzten 3 Jahre für mindestens 2 Wochen am Stück Medikamente '
                 'eingenommen?',
        additional_info="Medikamente sind alle Präparate, die du in Deutschland nur in der Apotheke bekommst. "
                        "Ausgenommen sind Verhütungsmittel.",
        number=1,
        risk=False,
        answer=None)
    q2_treatment = HealthQuestion(
        title='Treatment',
        question='Hattest du innerhalb der letzten 3 Jahre Behandlungen oder Untersuchungen (auch Nachsorge) '
                 'durch Ärzte oder Therapeuten?',
        additional_info="Wenn du Behandlungen wegen Husten, Schnupfen, Heiserkeit, Erkältungen oder grippalen "
                        "Infekten hattest und bist jetzt wieder gesund, musst du diese nicht angeben. "
                        "Allgemeine Vorsorgeuntersuchungen (auch Vorsorgeuntersuchungen beim Frauenarzt) müssen "
                        "nur dann angegegen werden, wenn diese einen Befund ergeben haben, der auf eine "
                        "Krankheit hinweist. Kontrolluntersuchungen, wie zum Beispiel Blutzuckerbestimmungen "
                        "bei Diabetes, kardiologische Kontrolluntersuchungen bei Herzklappenfehler oder "
                        "Tumornachsorge solltest du auf jeden Fall angeben.",
        number=2,
        risk=False,
        answer=None)
    q3_allergy = HealthQuestion(
        title='Allergy',
        question='Besteht bzw. bestand innerhalb der letzten 3 Jahre bei dir eine Allergie?',
        additional_info=None,
        number=3,
        risk=False,
        answer=None)
    q4_hospitalization = HealthQuestion(
        title='Hospitalization',
        question='Hattest du innerhalb der letzten 10 Jahre eine Behandlung mit Aufenthalt im Krankenhaus oder '
                 'Operationen ohne Krankenhausaufenthalt?',
        additional_info=None,
        number=4,
        risk=False,
        answer=None)
    q5_psychological = HealthQuestion(
        title='Psychological care',
        question='Hattest du innerhalb der letzten 10 Jahre Behandlungen oder Untersuchungen (auch Nachsorge) '
                 'wegen psychischen oder psychosomatischen Erkrankungen oder Beschwerden?',
        additional_info=None,
        number=5,
        risk=True,
        answer=None)
    q6_malignant = HealthQuestion(
        title='Malignant disease',
        question='Hattest du innerhalb der letzten 10 Jahre Behandlungen oder Untersuchungen (auch Nachsorge) '
                 'wegen bösartigen Krebserkrankungen?',
        additional_info=None,
        number=6,
        risk=True,
        answer=None)
    q7_chronic = HealthQuestion(
        title='Chronic disease',
        question='Besteht bei dir eine chronische Erkrankung?',
        additional_info='Chronisch sind Erkrankungen dann, wenn sie eine dauerhafte und regelmäßige '
                        'medizinische Betreuung notwendig machen. Chronische Erkrankungen treten teilweise in '
                        'Schüben auf und sind in der Regel nicht heilbar.',
        number=7,
        risk=False,
        answer=None)
    q8_hiv = HealthQuestion(
        title='HIV infection',
        question='Wurde bei dir jemals eine HIV-Infektion festgestellt?',
        additional_info='Hier musst du angeben, ob eine Infektion mit dem HI-Virus festgestellt wurde, auch '
                        'wenn es bisher nicht zu der Krankheit AIDS gekommen ist.',
        number=8,
        risk=True,
        answer=None)
    q9_addictions = HealthQuestion(
        title='Addictions',
        question='Warst du jemals wegen Alkohol-, Medikamenten-, Drogenabhängigkeit oder einer sonstigen '
                 'Suchterkrankung in Behandlung?',
        additional_info=None,
        number=9,
        risk=True,
        answer=None)
    q10_impairments = HealthQuestion(
        title='Impairments',
        question='Besteht bei dir eine oder mehrere Beeinträchtigungen der folgenden Liste?',
        additional_info='Bitte setze ein Häkchen, was bei dir zutrifft.',
        number=10,
        risk=True,
        answer=None)
    q11_planned = HealthQuestion(
        title='Planned treatment',
        question='Sind bei dir Behandlungen, Untersuchungen (auch Nachsorge) oder Operationen durch Ärzte oder '
                 'Therapeuten beabsichtigt, angeraten oder geplant?',
        additional_info='Ärzte und Therapeuten sind z.B. Hausärzte, alle Fachärzte, Psychotherapeuten, '
                        'Heilpraktiker, Osteo- und Chirotherapeuten, Zahnärzte, Kieferorthopäden oder '
                        'Kieferchirurgen.',
        number=11,
        risk=False,
        answer=None)

    def __init__(self,
                 medication: bool = False,
                 treatment: bool = False,
                 allergy: bool = False,
                 hospitalization: bool = False,
                 psychological: bool = False,
                 malignant: bool = False,
                 chronic: bool = False,
                 hiv: bool = False,
                 addictions: bool = False,
                 impairments: NewHealthImpairments = NewHealthImpairments(),
                 planned: bool = False
                 ):
        self.questions = [
            self.q1_medication,
            self.q2_treatment,
            self.q3_allergy,
            self.q4_hospitalization,
            self.q5_psychological,
            self.q6_malignant,
            self.q7_chronic,
            self.q8_hiv,
            self.q9_addictions,
            self.q10_impairments,
            self.q11_planned
        ]
        self.impairments_list = impairments
        self.q1_medication.answer = medication
        self.q2_treatment.answer = treatment
        self.q3_allergy.answer = allergy
        self.q4_hospitalization.answer = hospitalization
        self.q5_psychological.answer = psychological
        self.q6_malignant.answer = malignant
        self.q7_chronic.answer = chronic
        self.q8_hiv.answer = hiv
        self.q9_addictions.answer = addictions
        self.q10_impairments.answer = impairments.any_present
        self.q11_planned.answer = planned

    @property
    def printable(self) -> str:
        _string = ""
        for q in self.questions:
            _string += "\t{0}.{1}\t=\t{2}\n".format(q.number, q.title, q.answer)
            if q.number == 10:
                _string += "{0}".format(self.impairments_list.printable)
        return _string

    @property
    def medication(self) -> HealthQuestion:
        return self.questions[0]

    @property
    def treatment(self) -> HealthQuestion:
        return self.questions[1]

    @property
    def allergy(self) -> HealthQuestion:
        return self.questions[2]

    @property
    def hospitalization(self) -> HealthQuestion:
        return self.questions[3]

    @property
    def psychological(self) -> HealthQuestion:
        return self.questions[4]

    @property
    def malignant(self) -> HealthQuestion:
        return self.questions[5]

    @property
    def chronic(self) -> HealthQuestion:
        return self.questions[6]

    @property
    def hiv(self) -> HealthQuestion:
        return self.questions[7]

    @property
    def addictions(self) -> HealthQuestion:
        return self.questions[8]

    @property
    def impairments(self) -> HealthQuestion:
        return self.questions[9]

    @property
    def planned(self) -> HealthQuestion:
        return self.questions[10]

    def question_by_title(self, title: str) -> HealthQuestion or None:
        for q in self.questions:
            if q.title == title:
                return q
        p_e("No question with the title '{0}' was found. Inspect code!".format(title))
        return None


class MedicalPreconditions(Printable):
    def __init__(self,
                 psychological: bool = False,
                 malignant: bool = False,
                 hiv: bool = False,
                 addictions: bool = False):
        self.psychological = psychological
        self.malignant = malignant
        self.hiv = hiv
        self.addictions = addictions


class Address(Printable):
    def __init__(self,
                 postal_code: str,
                 city: str,
                 street: str,
                 nr: str,
                 addendum: str = ""):
        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.nr = nr
        self.addendum = addendum

    # TODO: Add handling of addendum
    @property
    def summary_comparable(self) -> str:
        return "{0} {1}, {2} {3}".format(self.street, self.nr, self.postal_code, self.city)


class Occupation(Printable):
    _INCOME_BOUNDARY = 60750

    O_RANDOM = 'random'
    O_INSURABLE = 'insurable'
    O_NOT_INSURABLE = 'not insurable'

    occupation_kinds = [O_INSURABLE, O_NOT_INSURABLE]

    occupations = [{"id": 101, "value": "Abbrucharbeiter/in"},
                   {"id": 102, "value": "Agraringenieur/in"},
                   {"id": 103, "value": "Agrarwissenschaftler/in"},
                   {"id": 104, "value": "Altenpfleger/in"},
                   {"id": 105, "value": "Ambulante/r H\u00e4ndler/in"},
                   {"id": 106, "value": "Angestellte/r, kaufm\u00e4nnisch"},
                   {"id": 107, "value": "Angestellte/r, technisch"},
                   {"id": 108, "value": "Anlageberater/in"},
                   {"id": 109, "value": "Anstreicher/in (auch Maler/in)"},
                   {"id": 110, "value": "Antennenbauer/in"},
                   {"id": 111, "value": "Antiquar/in"},
                   {"id": 112, "value": "Antiquit\u00e4tenh\u00e4ndler/in"},
                   {"id": 113, "value": "Apothekenhelfer/in"},
                   {"id": 114, "value": "Apotheker/in"},
                   {"id": 115, "value": "Arbeiter/in, chemische Industrie"},
                   {"id": 116, "value": "Arbeiter/in, metallverarbeitende Industrie"},
                   {"id": 117, "value": "Arbeiter/in, sonstige"},
                   {"id": 118, "value": "Arbeits- /Besch\u00e4ftigungstherapeut/in"},
                   {"id": 119, "value": "Arbeitsberater/in (Berufsberater/in)"},
                   {"id": 120, "value": "Arbeitsvermittler/in"},
                   {"id": 121, "value": "Arch\u00e4ologe/Arch\u00e4ologin"},
                   {"id": 122, "value": "Architekt/in"},
                   {"id": 123, "value": "Arzt/\u00c4rztin"},
                   {"id": 124, "value": "Arzthelfer/in"},
                   {"id": 125, "value": "Astronom/in"},
                   {"id": 126, "value": "Aufseher/in"},
                   {"id": 127, "value": "Augenoptiker/in"},
                   {"id": 128, "value": "Auktionator"},
                   {"id": 129, "value": "Auszubildende/r"},
                   {"id": 130, "value": "Automatenaufsteller/in"},
                   {"id": 131, "value": "Automobilkaufmann/-frau"},
                   {"id": 132, "value": "Autopfleger/in"},
                   {"id": 133, "value": "Autor/in"},
                   {"id": 134, "value": "Autotester/in"},
                   {"id": 135, "value": "Autovermieter/in"},
                   {"id": 136, "value": "B\u00e4cker/in"},
                   {"id": 137, "value": "Bademeister/in"},
                   {"id": 138, "value": "Baggerf\u00fchrer/in"},
                   {"id": 139, "value": "Bankkaufmann/-frau"},
                   {"id": 140, "value": "Bauarbeiter/in, Bauhelfer/in"},
                   {"id": 141, "value": "Bauingenieur/in"},
                   {"id": 142, "value": "Bauklempner/in, -schlosser/in"},
                   {"id": 143, "value": "Baumaschinenf\u00fchrer/in"},
                   {"id": 144, "value": "Baustoffhersteller/in"},
                   {"id": 145, "value": "Baustoffpr\u00fcfer/in"},
                   {"id": 146, "value": "Bautechniker/in"},
                   {"id": 147, "value": "Bautischler/in"},
                   {"id": 148, "value": "Beleuchter/in"},
                   {"id": 149, "value": "Bergbauarbeiter/in"},
                   {"id": 150, "value": "Bergbauingenieur/in"},
                   {"id": 151, "value": "Berufsfeuerwehrmann/-frau"},
                   {"id": 152, "value": "Berufskraftfahrer/in"},
                   {"id": 153, "value": "Bestatter/in"},
                   {"id": 154, "value": "Betonbauer/in"},
                   {"id": 155, "value": "Betonhersteller/in"},
                   {"id": 156, "value": "Betriebsleiter/in"},
                   {"id": 157, "value": "Betriebsschlosser/in"},
                   {"id": 158, "value": "Betriebswirt/in"},
                   {"id": 159, "value": "Bewegungstherapeut/in"},
                   {"id": 160, "value": "Bibliothekar/in"},
                   {"id": 161, "value": "Bierbrauer/in, Brauereiarbeiter/in"},
                   {"id": 162, "value": "Bildtechniker/in"},
                   {"id": 163, "value": "Binnenschiffer/in"},
                   {"id": 164, "value": "Biologe/Biologin"},
                   {"id": 165, "value": "biologisch-technische/r Assistent/in"},
                   {"id": 166, "value": "Blumenbinder/in (Florist/in)"},
                   {"id": 167, "value": "Blumenh\u00e4ndler/in"},
                   {"id": 168, "value": "Bohrinselarbeiter/in"},
                   {"id": 169, "value": "Bootsbauer/in"},
                   {"id": 170, "value": "B\u00f6rsenmakler/in"},
                   {"id": 171, "value": "Bote/Botin"},
                   {"id": 172, "value": "Brieftr\u00e4ger/in"},
                   {"id": 173, "value": "Brunnenbauer/in"},
                   {"id": 174, "value": "Buchbinder/in"},
                   {"id": 175, "value": "Buchdrucker/in"},
                   {"id": 176, "value": "Buchhalter/in"},
                   {"id": 177, "value": "Buchh\u00e4ndler/in"},
                   {"id": 178, "value": "B\u00fchnenausstatter/in"},
                   {"id": 179, "value": "Bundesgrenzschutz"},
                   {"id": 180, "value": "Bundeswehr"},
                   {"id": 181, "value": "B\u00fcrokaufmann /-frau"},
                   {"id": 182, "value": "Chauffeur"},
                   {"id": 183, "value": "Chemiearbeiter/in"},
                   {"id": 184, "value": "Chemielaborant/in"},
                   {"id": 185, "value": "Chemiker/in"},
                   {"id": 186, "value": "Chiropraktiker/in"},
                   {"id": 187, "value": "Chirurg/in"},
                   {"id": 188, "value": "Choreograph/in"},
                   {"id": 189, "value": "Chorleiter/in"},
                   {"id": 190, "value": "Co-Pilot/in"},
                   {"id": 191, "value": "Cutter/in"},
                   {"id": 192, "value": "Dachdecker/in"},
                   {"id": 193, "value": "Datentypist/in"},
                   {"id": 194, "value": "Datenverarbeitungskaufmann/-frau"},
                   {"id": 195, "value": "Dekorateur/in"},
                   {"id": 196, "value": "Designer/in"},
                   {"id": 197, "value": "Detektiv/in"},
                   {"id": 198, "value": "Diplomkaufmann/-frau"},
                   {"id": 199, "value": "Dirigent/in"},
                   {"id": 200, "value": "Dolmetscher/in"},
                   {"id": 201, "value": "Dorfhelfer/in"},
                   {"id": 202, "value": "Dramaturg/in"},
                   {"id": 203, "value": "Drechsler/in"},
                   {"id": 204, "value": "Dreher/in"},
                   {"id": 205, "value": "Drogist/in"},
                   {"id": 206, "value": "Drucker/in"},
                   {"id": 207, "value": "Druckvorlagenhersteller/in"},
                   {"id": 208, "value": "Eheberater/in"},
                   {"id": 209, "value": "Einzelhandelskaufmann/-frau"},
                   {"id": 210, "value": "Einzelh\u00e4ndler/in"},
                   {"id": 211, "value": "Elektriker/in"},
                   {"id": 212, "value": "Elektroingenieur/in"},
                   {"id": 213, "value": "Elektroinstallateur/in"},
                   {"id": 214, "value": "Elektromechaniker/in"},
                   {"id": 215, "value": "Elektroniker/in"},
                   {"id": 216, "value": "Elektrotechniker/in"},
                   {"id": 217, "value": "Energieanlagenelektroniker/in"},
                   {"id": 218, "value": "Ergotherapeut/in"},
                   {"id": 219, "value": "Ern\u00e4hrungsberater/in"},
                   {"id": 220, "value": "Erzieher/in"},
                   {"id": 221, "value": "Erziehungsberater/in"},
                   {"id": 222, "value": "Estrichleger/in"},
                   {"id": 223, "value": "Fahrlehrer/in"},
                   {"id": 224, "value": "Familienpfleger/in"},
                   {"id": 225, "value": "Feinmechaniker/in"},
                   {"id": 226, "value": "Fensterputzer/in"},
                   {"id": 227, "value": "Fernmeldemonteur/in"},
                   {"id": 228, "value": "Fernsehtechniker/in"},
                   {"id": 229, "value": "Feuerwehrmann/-frau"},
                   {"id": 230, "value": "Feuerwerker/in"},
                   {"id": 231, "value": "Filmvorf\u00fchrer/in"},
                   {"id": 232, "value": "Fischer/in"},
                   {"id": 233, "value": "Fitne\u00dfstudiobetreiber/in"},
                   {"id": 234, "value": "Fleischer/in"},
                   {"id": 236, "value": "Fliesenleger/in"},
                   {"id": 237, "value": "Florist/in"},
                   {"id": 239, "value": "Flugzeugingenieur/in"},
                   {"id": 240, "value": "Flugzeugmechaniker/in"},
                   {"id": 241, "value": "Forstarbeiter/in"},
                   {"id": 242, "value": "F\u00f6rster/in"},
                   {"id": 243, "value": "Fotograf/in"},
                   {"id": 244, "value": "Fremdenf\u00fchrer/in"},
                   {"id": 245, "value": "Fremdsprachenkorrespondent/in"},
                   {"id": 246, "value": "Friseur/in"},
                   {"id": 247, "value": "Fuhrunternehmer/in"},
                   {"id": 248, "value": "Fu\u00dfbodenleger/in"},
                   {"id": 249, "value": "Fu\u00dfpfleger/in"},
                   {"id": 250, "value": "Gabelstaplerfahrer/in"},
                   {"id": 251, "value": "Gartenbauingenieur/in"},
                   {"id": 252, "value": "G\u00e4rtner/in"},
                   {"id": 253, "value": "Gasinstallateur/in"},
                   {"id": 254, "value": "Gastronom/in"},
                   {"id": 255, "value": "Geb\u00e4udereiniger/in"},
                   {"id": 256, "value": "Gef\u00e4ngnisaufseher/in"},
                   {"id": 257, "value": "Gefl\u00fcgelz\u00fcchter/in"},
                   {"id": 258, "value": "Geisteswissenschaftler/in"},
                   {"id": 259, "value": "Gelegenheitsarbeiter/in"},
                   {"id": 260, "value": "Gemeindepfleger/ -schwester"},
                   {"id": 261, "value": "Gem\u00fcseh\u00e4ndler/in"},
                   {"id": 262, "value": "Geowissenschaftler/in"},
                   {"id": 263, "value": "Gerber/in"},
                   {"id": 264, "value": "Germanist/in"},
                   {"id": 265, "value": "Ger\u00fcstbauer/in"},
                   {"id": 266, "value": "Gesch\u00e4ftsf\u00fchrer/in (kfm.)"},
                   {"id": 267, "value": "Gesch\u00e4ftsf\u00fchrer/in (techn.)"},
                   {"id": 268, "value": "Gie\u00dfer/in"},
                   {"id": 269, "value": "Glaser/in"},
                   {"id": 270, "value": "Gleisbauer/in"},
                   {"id": 271, "value": "Goldschmied/in"},
                   {"id": 272, "value": "Grafiker/in"},
                   {"id": 273, "value": "Gro\u00dfhandelskaufmann/-frau"},
                   {"id": 274, "value": "Handelsreisende/r"},
                   {"id": 275, "value": "Handelsvertreter/in"},
                   {"id": 276, "value": "Handwerker"},
                   {"id": 277, "value": "Hauswart/in"},
                   {"id": 278, "value": "Hauswirtschafter/in"},
                   {"id": 279, "value": "Hebamme"},
                   {"id": 280, "value": "Heilpraktiker/in"},
                   {"id": 281, "value": "Heizungsmonteur/in"},
                   {"id": 282, "value": "Hilfsarbeiter/in"},
                   {"id": 283, "value": "Hilfspersonal (\u00e4rztliches)"},
                   {"id": 284, "value": "Historiker/in"},
                   {"id": 285, "value": "Holzarbeiter/in"},
                   {"id": 286, "value": "Hom\u00f6opath/in"},
                   {"id": 287, "value": "H\u00f6rger\u00e4teakustiker/in"},
                   {"id": 288, "value": "Hotelfachmann/-frau"},
                   {"id": 289, "value": "Hotelier"},
                   {"id": 290, "value": "Hotelkaufmann/-frau"},
                   {"id": 291, "value": "Hufschmied/in"},
                   {"id": 292, "value": "Hutmacher/in"},
                   {"id": 293, "value": "Illustrator/in"},
                   {"id": 294, "value": "Imbissstand (selbst.)"},
                   {"id": 295, "value": "Imker/in"},
                   {"id": 296, "value": "Immobilienmakler/in"},
                   {"id": 297, "value": "Industriemechaniker/in"},
                   {"id": 298, "value": "Informatiker/in"},
                   {"id": 299, "value": "Ingenieur/in"},
                   {"id": 300, "value": "Innenarchitekt/in"},
                   {"id": 301, "value": "Installateur/in"},
                   {"id": 302, "value": "Internist/in"},
                   {"id": 303, "value": "Isolierer/in"},
                   {"id": 304, "value": "J\u00e4ger/in"},
                   {"id": 305, "value": "Journalist/in"},
                   {"id": 306, "value": "Jugendpfleger/in"},
                   {"id": 307, "value": "Jurist/in"},
                   {"id": 308, "value": "Juwelier/in"},
                   {"id": 309, "value": "Kabelmonteur/in"},
                   {"id": 310, "value": "K\u00e4ltemechaniker/in"},
                   {"id": 311, "value": "Kameramann/-frau"},
                   {"id": 312, "value": "Kaminbauer/in"},
                   {"id": 313, "value": "Karosseriebauer/in"},
                   {"id": 314, "value": "Kassierer/in"},
                   {"id": 315, "value": "Kaufmann/-frau"},
                   {"id": 316, "value": "kaufm\u00e4nnische/r Angestellte/r"},
                   {"id": 317, "value": "Kellner/in"},
                   {"id": 318, "value": "Kerntechniker/in"},
                   {"id": 319, "value": "Kfz-H\u00e4ndler/in"},
                   {"id": 320, "value": "Kfz-Mechaniker/in"},
                   {"id": 321, "value": "Kfz-Schlosser/in"},
                   {"id": 322, "value": "Kinderg\u00e4rtner/in"},
                   {"id": 323, "value": "Kioskbesitzer/in"},
                   {"id": 324, "value": "Klavierlehrer/in"},
                   {"id": 325, "value": "Klempner/in"},
                   {"id": 326, "value": "Koch/K\u00f6chin"},
                   {"id": 327, "value": "Konstrukteur/in"},
                   {"id": 328, "value": "Kosmetiker/in"},
                   {"id": 329, "value": "Kost\u00fcmbildner/in"},
                   {"id": 330, "value": "Kranf\u00fchrer/in"},
                   {"id": 331, "value": "Krankengymnast/in"},
                   {"id": 332, "value": "Krankenschwester /-pfleger"},
                   {"id": 333, "value": "K\u00fcchenhilfe"},
                   {"id": 334, "value": "K\u00fcnstler/in"},
                   {"id": 335, "value": "Kunstmaler/in"},
                   {"id": 336, "value": "Kunststoffverarbeiter/in"},
                   {"id": 337, "value": "Kurier/in"},
                   {"id": 338, "value": "Laborant/in"},
                   {"id": 339, "value": "Lackierer/in"},
                   {"id": 340, "value": "Lagerarbeiter/in"},
                   {"id": 341, "value": "Landmaschinenmechaniker/in"},
                   {"id": 342, "value": "Landschaftsarchitekt/in"},
                   {"id": 343, "value": "Landwirt/in"},
                   {"id": 344, "value": "landwirtschaftl.-techn. Assistent/in"},
                   {"id": 345, "value": "Layouter/in"},
                   {"id": 346, "value": "Lederwarenhersteller/in"},
                   {"id": 347, "value": "Lektor/in"},
                   {"id": 348, "value": "Logop\u00e4de/Logop\u00e4din"},
                   {"id": 349, "value": "Makler/in"},
                   {"id": 350, "value": "Maler (Anstreicher)"},
                   {"id": 351, "value": "Maschinenbauingenieur/in"},
                   {"id": 352, "value": "Maschinenschlosser/in"},
                   {"id": 353, "value": "Maskenbildner/in"},
                   {"id": 354, "value": "Masseur/in"},
                   {"id": 355, "value": "Mathematiker/in"},
                   {"id": 356, "value": "Maurer/in"},
                   {"id": 357, "value": "Mechaniker/in"},
                   {"id": 358, "value": "medizinische/r Bademeister/in"},
                   {"id": 359, "value": "medizinisch-techn. Assistent/in"},
                   {"id": 360, "value": "Messebauer/Messebauerin"},
                   {"id": 361, "value": "Meteorologe/Meteorologin"},
                   {"id": 362, "value": "M\u00f6belh\u00e4ndler/in"},
                   {"id": 363, "value": "M\u00f6belpacker/in"},
                   {"id": 364, "value": "Modedesigner/in"},
                   {"id": 365, "value": "Modellbauer/in"},
                   {"id": 366, "value": "Museumsleiter/in"},
                   {"id": 367, "value": "Musiker/in"},
                   {"id": 368, "value": "Musiklehrer/in"},
                   {"id": 369, "value": "N\u00e4her/in"},
                   {"id": 370, "value": "Nahrungsmittelchemiker/in"},
                   {"id": 371, "value": "Notar/in"},
                   {"id": 372, "value": "Obsth\u00e4ndler/in"},
                   {"id": 373, "value": "Ofenbauer /-setzer"},
                   {"id": 374, "value": "\u00f6ffentlicher Dienst"},
                   {"id": 375, "value": "\u00d6konom/in (Dipl.)"},
                   {"id": 376, "value": "Operns\u00e4nger/in"},
                   {"id": 377, "value": "Orthop\u00e4de/Orthop\u00e4din"},
                   {"id": 378, "value": "orthop\u00e4dische/r Schuhmacher/in"},
                   {"id": 379, "value": "P\u00e4dagoge/P\u00e4dagogin"},
                   {"id": 380, "value": "Paketbote/-botin"},
                   {"id": 381, "value": "Parf\u00fcmeriemitarbeiter/in"},
                   {"id": 382, "value": "Pastor/in, Pfarrer/in"},
                   {"id": 383, "value": "Personensch\u00fctzer/in"},
                   {"id": 384, "value": "Pferdewirt/in"},
                   {"id": 385, "value": "Pfleger/in"},
                   {"id": 386, "value": "Pf\u00f6rtner/in"},
                   {"id": 387, "value": "Pharmareferent/in"},
                   {"id": 388, "value": "Pharmazeut/in"},
                   {"id": 389, "value": "pharmazeutisch-techn. Assistent/in"},
                   {"id": 390, "value": "physikal.-techn. Assistent/in"},
                   {"id": 391, "value": "Physiker/in"},
                   {"id": 393, "value": "Plakatierer/in"},
                   {"id": 394, "value": "Polierer/in"},
                   {"id": 395, "value": "Polizeibedienstete/r"},
                   {"id": 396, "value": "Polsterer/Polsterin"},
                   {"id": 397, "value": "Professor/in"},
                   {"id": 398, "value": "Programmierer/in"},
                   {"id": 399, "value": "Prokurist/in"},
                   {"id": 400, "value": "Psychologe/Psychologin"},
                   {"id": 401, "value": "Psychotherapeut/in"},
                   {"id": 402, "value": "Pyrotechniker/in"},
                   {"id": 403, "value": "Radiologe/Radiologin"},
                   {"id": 404, "value": "Raumpfleger/in"},
                   {"id": 405, "value": "Rechtsanwalt/-anw\u00e4ltin"},
                   {"id": 406, "value": "Rechtsberater/in"},
                   {"id": 407, "value": "Redakteur/in"},
                   {"id": 408, "value": "Referendar/in"},
                   {"id": 409, "value": "Regisseur/in"},
                   {"id": 410, "value": "Reparateur/in"},
                   {"id": 411, "value": "Restaurantfachmann/-frau"},
                   {"id": 412, "value": "Restaurator/in"},
                   {"id": 413, "value": "Rettungsassistent/in"},
                   {"id": 414, "value": "Richter/in"},
                   {"id": 415, "value": "Rohrreiniger/in"},
                   {"id": 416, "value": "Rolladenbauer/in"},
                   {"id": 417, "value": "R\u00f6ntgenassistent/in"},
                   {"id": 418, "value": "Rundfunkmechaniker/in"},
                   {"id": 419, "value": "S\u00e4nger/in"},
                   {"id": 420, "value": "Sanit\u00e4ter/in"},
                   {"id": 421, "value": "Sch\u00e4dlingsbek\u00e4mpfer/in"},
                   {"id": 422, "value": "Sch\u00e4fer/in"},
                   {"id": 423, "value": "Schaffner/in"},
                   {"id": 424, "value": "Schauspieler/in"},
                   {"id": 425, "value": "Schauwerbegestalter/in"},
                   {"id": 426, "value": "Schiffer/in"},
                   {"id": 427, "value": "Schiffsbauer/in"},
                   {"id": 428, "value": "Schiffsingenieur/in"},
                   {"id": 429, "value": "Schleifer/in"},
                   {"id": 430, "value": "Schlosser/in"},
                   {"id": 431, "value": "Schl\u00fcsseldienst (selbst.)"},
                   {"id": 432, "value": "Schmied/in"},
                   {"id": 433, "value": "Schneider/in"},
                   {"id": 434, "value": "Schornsteinfeger/in"},
                   {"id": 435, "value": "Schreibwarenh\u00e4ndler/in"},
                   {"id": 436, "value": "Schriftsetzer/in"},
                   {"id": 437, "value": "Schriftsteller/in"},
                   {"id": 438, "value": "Schrotth\u00e4ndler/in"},
                   {"id": 439, "value": "Schuhmacher/in, Schuster/in"},
                   {"id": 440, "value": "Schwei\u00dfer/in"},
                   {"id": 441, "value": "Seelsorger/in"},
                   {"id": 442, "value": "Sekret\u00e4r/-in"},
                   {"id": 443, "value": "Sicherheitsdienst (selbst.)"},
                   {"id": 444, "value": "Silberschmied/in"},
                   {"id": 445, "value": "Sozialarbeiter/in"},
                   {"id": 446, "value": "Sozialp\u00e4dagoge/-p\u00e4dagogin"},
                   {"id": 447, "value": "Sozialversicherungsfachangestellte/r"},
                   {"id": 448, "value": "Soziologe/Soziologin"},
                   {"id": 449, "value": "Spediteur/in"},
                   {"id": 450, "value": "Speditionsarbeiter/in"},
                   {"id": 451, "value": "Speditionskaufmann/-frau"},
                   {"id": 452, "value": "Spielbudenbesitzer/in"},
                   {"id": 453, "value": "Spirituosenh\u00e4ndler/in"},
                   {"id": 454, "value": "Sprechstundenhelfer/in"},
                   {"id": 455, "value": "Sprengmeister/in"},
                   {"id": 456, "value": "Staatsanwalt/-anw\u00e4ltin"},
                   {"id": 457, "value": "Stadtplaner/in"},
                   {"id": 458, "value": "Stahlarbeiter/in"},
                   {"id": 459, "value": "Statiker/in"},
                   {"id": 460, "value": "Steinmetz/in"},
                   {"id": 461, "value": "Stenotypist/in"},
                   {"id": 462, "value": "Steuerberater/in"},
                   {"id": 463, "value": "Steuergehilfe/-gehilfin"},
                   {"id": 464, "value": "Stra\u00dfenbahnfahrer/in"},
                   {"id": 465, "value": "Stra\u00dfenbauer/in"},
                   {"id": 466, "value": "Stra\u00dfenreiniger/in"},
                   {"id": 467, "value": "Studienberater/in"},
                   {"id": 468, "value": "Subunternehmer/in"},
                   {"id": 469, "value": "Systemkaufmann/-frau"},
                   {"id": 470, "value": "Tabakh\u00e4ndler/in"},
                   {"id": 471, "value": "Tankstellenp\u00e4chter/in"},
                   {"id": 472, "value": "Tankwart/in"},
                   {"id": 473, "value": "T\u00e4nzer/T\u00e4nzerin"},
                   {"id": 474, "value": "Tanzlehrer/in"},
                   {"id": 475, "value": "Taxifahrer/in"},
                   {"id": 476, "value": "Techniker/in"},
                   {"id": 477, "value": "Technische/r Zeichner/in"},
                   {"id": 478, "value": "Telefonist/in"},
                   {"id": 479, "value": "Teppichh\u00e4ndler/in"},
                   {"id": 480, "value": "Testfahrer/in"},
                   {"id": 481, "value": "Texter/in"},
                   {"id": 482, "value": "Textilarbeiter/in"},
                   {"id": 483, "value": "Textilreiniger/in"},
                   {"id": 484, "value": "Tierarzt/-\u00e4rztin"},
                   {"id": 485, "value": "Tierpfleger/in"},
                   {"id": 486, "value": "Tierz\u00fcchter/in"},
                   {"id": 487, "value": "Tischler/in"},
                   {"id": 488, "value": "Tontechniker/in"},
                   {"id": 489, "value": "T\u00f6pfer/in"},
                   {"id": 490, "value": "Transportarbeiter/in"},
                   {"id": 491, "value": "Transportunternehmer/in"},
                   {"id": 492, "value": "Treppenbauer/in"},
                   {"id": 493, "value": "Treuh\u00e4nder/in"},
                   {"id": 494, "value": "Uebersetzer/in"},
                   {"id": 495, "value": "Uhrmacher/in"},
                   {"id": 496, "value": "Unternehmensberater/in"},
                   {"id": 497, "value": "Unternehmer/in"},
                   {"id": 498, "value": "Verfuger/in"},
                   {"id": 499, "value": "Verk\u00e4ufer/in"},
                   {"id": 500, "value": "Verkaufsfahrer/in"},
                   {"id": 501, "value": "Verlagskaufmann/-frau"},
                   {"id": 502, "value": "Verleger/in"},
                   {"id": 503, "value": "Vermessungstechniker/in"},
                   {"id": 504, "value": "Verm\u00f6gensverwalter/in"},
                   {"id": 505, "value": "Verputzer/in"},
                   {"id": 506, "value": "Versicherungsagent/in"},
                   {"id": 507, "value": "Versicherungsfachmann/-frau"},
                   {"id": 508, "value": "Versicherungskaufmann/-frau"},
                   {"id": 509, "value": "Verwaltungsangestellte/r"},
                   {"id": 510, "value": "Viehh\u00e4ndler/in"},
                   {"id": 511, "value": "Volkswirt/in"},
                   {"id": 512, "value": "W\u00e4rter/in"},
                   {"id": 513, "value": "Weber/in"},
                   {"id": 514, "value": "Weinh\u00e4ndler/in"},
                   {"id": 515, "value": "Werbefachmann/-frau"},
                   {"id": 516, "value": "Werbekaufmann/-frau"},
                   {"id": 517, "value": "Werkmeister/in"},
                   {"id": 518, "value": "Werkstoffpr\u00fcfer/in"},
                   {"id": 519, "value": "Werkzeugmacher/in"},
                   {"id": 520, "value": "Wirtschaftsberater/in"},
                   {"id": 521, "value": "Wirtschaftsingenieur/in"},
                   {"id": 522, "value": "Wirtschaftspr\u00fcfer/in"},
                   {"id": 523, "value": "wissenschaftl. Mitarbeiter/in"},
                   {"id": 524, "value": "Zahnarzt/-\u00e4rztin"},
                   {"id": 525, "value": "Zahnarzthelfer/in"},
                   {"id": 526, "value": "Zahntechniker/in"},
                   {"id": 527, "value": "Zimmerer"},
                   {"id": 528, "value": "Zugf\u00fchrer/in"},
                   {"id": 529, "value": "Patentanwalt/-anw\u00e4ltin"},
                   {"id": 994, "value": "Rentner/in"},
                   {"id": 997, "value": "Hausfrau/-mann"}]

    not_insurable_occupation_ids = [134, 140, 149, 151, 152, 163, 168, 188, 190, 197, 226, 230, 232, 241, 250, 259, 265,
                                    282, 283, 294, 323, 333, 334, 337, 340, 367, 380, 383, 402, 421, 426, 443, 452, 453,
                                    455, 473, 474, 480, 997]

    O_EMPLOYEE = "Arbeitnehmer"
    O_SELF_EMPLOYED = "Selbstständig"
    O_STUDENT = "Student"
    # O_CIVIL_SERVANT = "Beamter"
    # O_CIVIL_SERVANT_APPLICANT = "Beamtenanwärter"

    # Abbreviations expanded
    job_types_UI_Summary = {O_EMPLOYEE: 'Angestellter',
                            O_SELF_EMPLOYED: 'Selbstständig',
                            O_STUDENT: 'Student'}

    job_types_UI_AdminApp = {'Angestellt': O_EMPLOYEE,
                             'Selbstständig': O_SELF_EMPLOYED,
                             'Student': O_STUDENT}

    insurable_occupations = None
    not_insurable_occupations = None

    @staticmethod
    def generate_income(safe: bool = True) -> int:
        if not safe:
            return random.randint(0, Occupation._INCOME_BOUNDARY - 1)
        else:
            # TODO: remember the change of lower value from 2019.01
            return random.randint(Occupation._INCOME_BOUNDARY, 300000)

    @staticmethod
    def split_jobs() -> ([], []):
        insurable_occupations = []
        not_insurable_occupations = []

        for job in Occupation.occupations:
            if int(job['id']) in Occupation.not_insurable_occupation_ids:
                not_insurable_occupations.append(job)
            else:
                insurable_occupations.append(job)
        return insurable_occupations, not_insurable_occupations

    @staticmethod
    def get_occupation_by_id(oid: int):
        for o in Occupation.occupations:
            if o['id'] == oid:
                return o
        return None

    @staticmethod
    def random_occupation(insurable: bool or str or None) -> (int, str):
        _occupation_ids = [o['id'] for o in Occupation.occupations]
        _safe_ids = [_id for _id in _occupation_ids if _id not in Occupation.not_insurable_occupation_ids]

        _id = None
        if insurable is True or insurable == Occupation.O_INSURABLE:
            _id = random.choice(_safe_ids)
        elif insurable is False or insurable == Occupation.O_NOT_INSURABLE:
            _id = random.choice(Occupation.not_insurable_occupation_ids)
        elif insurable is None:
            _id = random.choice(_occupation_ids)

        o = Occupation.get_occupation_by_id(oid=_id)
        if o is not None:
            _name = o['value']
        else:
            _name = None

        return _id, _name

    @staticmethod
    def get_random_occupation(kind: str):
        if kind not in Occupation.occupation_kinds:
            p_e("The type '{0}' is not supported".format(kind))

        insurable_occupations, not_insurable_occupations = Occupation.split_jobs()
        if kind == Occupation.occupation_kinds[0]:
            amount = len(insurable_occupations)
            occupation = insurable_occupations[random.randint(0, amount - 1)]['value']
        else:
            amount = len(not_insurable_occupations)
            occupation = not_insurable_occupations[random.randint(0, amount - 1)]['value']
        return occupation

    def __init__(self,
                 _name: str or None,
                 _type: str,
                 _income: int,
                 _randomize: bool=False):
        self.o_name = _name
        self.o_type = _type
        self.o_income = _income
        locale.setlocale(locale.LC_MONETARY, 'de_DE.UTF-8')

    @property
    def ui_comparable_income(self) -> str:
        return locale.currency(self.o_income, grouping=True)

    @property
    def ui_comparable_type(self) -> str:
        return self.job_types_UI_Summary[self.o_type]


class AgeContributionRelief(Printable):
    BEK_NONE = None
    BEK___64 = 64
    BEK___67 = 67
    bek_start_options = {BEK_NONE: 'Keine Beitragsentlastung',
                         BEK___64: 'ab dem 64. Lebensjahr',
                         BEK___67: 'ab dem 67. Lebensjahr'
                         }

    def __init__(self,
                 _year: int or None,
                 _amount: int or None,
                 _requested: bool or None,
                 _randomize: bool=False):
        # None in case of CIVIL_SERVANT
        self.bek_year = _year
        self.bek_amount = _amount
        self.bek_requested = _requested
        self.bek_randomize = _randomize
        locale.setlocale(locale.LC_MONETARY, 'de_DE.UTF-8')

    @property
    def ui_comparable_year(self) -> str:
        return str(self.bek_start_options[self.bek_year])

    @property
    def ui_comparable_amount(self) -> str:
        return locale.currency(self.bek_amount)

    @staticmethod
    def bek_expected(age: int) -> bool:
        if age < 18:
            p_w("The user should not be able to continue with insurance as they're under 18")
        elif 18 <= age < 21:
            log("The user should NOT have a BeitragsEntlastungsKomponente (too young)")
            # TODO: Consider using this
            return False
        elif 21 <= age < 50:
            log("The user SHOULD have a BeitragsEntlastungsKomponente")
            # TODO: Consider using this
            return True
        elif 50 <= age:
            log("The user should NOT have a BeitragsEntlastungsKomponente (too old)")
            # TODO: Consider using this
            return False


class DailySicknessAllowance(Printable):
    KTG_NONE = None
    KTG___43 = 43
    KTG___92 = 92
    KTG__183 = 183
    ktg_start_options = {KTG_NONE: 'Kein Krankentagegeld',
                         KTG___43: 'ab dem 43. Tag',
                         KTG___92: 'ab dem 92. Tag',
                         KTG__183: 'ab dem 183. Tag'
                         }

    def __init__(self,
                 _from: int or None,
                 _amount: int or None,
                 _requested: bool or None,
                 _randomize: bool=False):
        # None in case of CIVIL_SERVANT
        self.ktg_from = _from
        self.ktg_amount = _amount
        self.ktg_requested = _requested
        self.ktg_randomize = _randomize
        locale.setlocale(locale.LC_MONETARY, 'de_DE.UTF-8')

    @property
    def ui_comparable_from(self) -> str:
        return str(self.ktg_start_options[self.ktg_from])

    @property
    def ui_comparable_amount(self) -> str:
        return locale.currency(self.ktg_amount)


class PreviousInsurance(Printable):
    _default_insurer_name = "TEST INSURANCE COMPANY"

    # Has the insurance been cancelled
    S_____CANCELLED = 'gekündigt'
    S_NOT_CANCELLED = 'nicht gekündigt'
    s_cancelled_UI = {S_____CANCELLED: 'Ja',
                      S_NOT_CANCELLED: 'Nein'}

    fees_UI = {True: 'Ja',
               False: 'Nein'}

    emergency_tariff_UI = {True: 'Ja',
                           False: 'Nein'}

    # Insurance types
    AKV = 'AKV'
    PKV = 'PKV'
    GKV = 'GKV'
    NONE = 'None'
    RANDOM = 'RANDOM'
    _supported_insurance_types = [PKV, GKV, AKV]
    full_types = [PKV, GKV, AKV, NONE]
    topup_types = [PKV, GKV, NONE]
    # Abbreviations expanded
    insurance_types = {PKV: 'Private Krankenversicherung',
                       GKV: 'Gesetzliche Versicherung',
                       AKV: 'Ausländische Versicherung',
                       NONE: 'Keine Versicherung'}

    insurance_types_UI = {PKV: 'privat versichert',
                          GKV: 'gesetzlich versichert',
                          AKV: 'Ausländische Versicherung'}

    __pi_type = None

    def __init__(self,
                 _type: str or None,
                 _name: str or None,
                 _country: str or None,
                 _date: date,
                 _state: str,
                 _fees: bool,
                 _emergency_tariff: bool,
                 _randomize: bool=False):

        # Name MUST be set before Type
        # in case GKV/PKV + no name => the name should get randomized by UI - DO NOT CLEAN IT
        self.pi_name = _name
        self.pi_type = _type
        self.pi_country = _country
        self.pi_date = _date
        self.pi_state = _state
        self.pi_fees = _fees
        self.pi_emergency_tariff = _emergency_tariff
        self.pi_randomize = _randomize

    @property
    def ui_comparable_type(self) -> str:
        return str(self.insurance_types_UI[self.pi_type])

    @property
    def ui_comparable_state(self) -> str:
        return str(self.s_cancelled_UI[self.pi_state])

    @property
    def ui_comparable_fees(self) -> str:
        return str(self.fees_UI[self.pi_fees])

    @property
    def ui_comparable_emergency_tariff(self) -> str:
        return str(self.emergency_tariff_UI[self.pi_emergency_tariff])

    @property
    def pi_type(self):
        return self.__pi_type

    @pi_type.setter
    def pi_type(self, _type: str or None):
        # if previous insurance type is None - randomize it
        if _type is None:
            _type = random.choice(self._supported_insurance_types)
            log("Randomized 'previous_insurance_type' to '{0}'".format(_type))

        # in case AKV + no name => take default
        if self.pi_type == self.AKV and self.pi_name is None:
            self.pi_name = self._default_insurer_name
            log("Set 'previous_insurance_name' to  default: '{0}'".format(self.pi_name))

        # in case GKV/PKV + no name => the name should get randomized by UI - DO NOT CLEAN IT
        self.__pi_type = _type

    @staticmethod
    def generate_date(date_of_birth: date, safe: bool = True):
        timespan_in_days = timedelta(days=random.randint(0, int(10 * 365.25) - 1))
        # generate ages 0-18 and 18-120
        if not safe:
            # TODO: There should be some more cases of unsafe results - insurance with another company made yesterday?
            timespan_in_days *= -1
        contract_date = date_of_birth + timespan_in_days
        return contract_date


class IBAN(Printable):
    @staticmethod
    def generate_valid_iban(prefix: str = "DE") -> (str, str):
        ba = ""
        for char in prefix:
            ba += str(ord(char) - 55)
        i = str(random.randint(0, 999999999999999999)).zfill(18)
        mod = int(i + ba) * 100 % 97
        n = str(98 - mod).zfill(2)
        ban = ba + n
        mod = int(i + ban) % 97
        iban = prefix + n + i
        print("IBAN = {0}\nMod = {1}".format(iban, mod))
        return iban[:2], iban[2:]

    @staticmethod
    def verify_iban(iban_str: str, prefix: str = "DE") -> bool:
        if len(iban_str) != 20:
            p_w("The IBAN provided ['{0}'] doesn't have 18 digits! "
                "Verify the input in case it's not a negative test!".format(iban_str))
        if not iban_str.isdigit():
            p_w("The IBAN provided ['{0}'] is not an integer! "
                "Verify the input in case it's not a negative test!".format(iban_str))
        i = iban_str[:2]
        ban = iban_str[2:]
        for char in prefix:
            ban += str(ord(char) - 55)
        ban += i
        mod = int(ban) % 97
        return mod == 1

    def __init__(self, prefix: str = "", control: str = "", number: str = "", iban: str = ""):
        _control = ""
        _number = ""
        _prefix = ""

        # if a complete iban is NOT provided...
        if iban == "":
            # if control and number are missing - generate a random one
            if control == "" and number == "":
                p_w("IBAN received no setup data. Generating a random one!")
                # if a prefix is provided - use it, if not, take default one
                if prefix == "":
                    _prefix, random_iban = self.generate_valid_iban()
                else:
                    _prefix, random_iban = self.generate_valid_iban(prefix=prefix)
                _control = random_iban[:2]
                _number = random_iban[2:]
            # otherwise use them if they make up a valid IBAN
            elif self.verify_iban(iban_str=control + number, prefix=prefix):
                _prefix = prefix
                _control = control
                _number = number
            else:
                p_e("The provided IBAN '{0}' was invalid!".format(iban))

            if self.verify_iban(iban_str=_control + _number, prefix=_prefix):
                self.full = _prefix + _control + _number
            else:
                p_e("The provided IBAN '{0}' was invalid!".format(self.full))

        # if an iban IS provided - verify it and use it
        else:
            _iban = iban.replace(" ", "")
            if self.verify_iban(iban_str=_iban[2:], prefix=_iban[:2]):
                self.full = _iban
            else:
                p_e("The provided IBAN '{0}' was invalid!".format(_iban))

    @property
    def prefixless(self):
        return self.full[2:]

    @property
    def prefix(self):
        return self.full[:2]

    @property
    def control(self):
        return self.full[2:4]

    @property
    def controlless(self):
        return self.full[4:]


class CivilServantConfig(object):
    # request_base = "https://{0}/api/tariff/otto/civil-servant/quotes?".format(_ENV_TEST)

    @staticmethod
    def request_base(env: str = E_TEST):
        env_base_url = {E_STAGING: "staging.on.ag",
                        E_TEST: "test.on.ag"}
        return "https://{0}/api/tariff/otto/civil-servant/quotes?".format(env_base_url[env])

    # from onSeleniumLess.TariffChecker.TariffChecker import tariff_file_path
    # filename = "/home/bartoszchmura/PycharmProjects/web-tests/onSeleniumLess/TariffChecker/Beitraege-v6.xlsx"

    bhtraeger_keys = ('A', 'B', 'C', 'D', 'E')
    SPECIAL_CASE = 'C'

    SERVANT = 'civil-servant'
    APPLICANT = 'civil-servant-applicant'
    STUDENT = 'civil-servant-student-child'
    CHILD = 'child'

    civ_serv_types = {SERVANT: "Beamter",
                      APPLICANT: "Beamtenanwärter"}
    # those have special logic to be selected...
    #              ['child', 'civil-servant-student-child']
    beihilfetraeger = {'A': ['Bund',
                             'Bayern',
                             'Nordrhein-Westfalen',
                             'Rheinland-Pfalz',
                             'Sachsen',
                             'Sachsen-Anhalt',
                             'Thüringen'],
                       'B': ['Berlin',
                             'Brandenburg',
                             'Hamburg',
                             'Mecklenburg-Vorpommern',
                             'Niedersachsen',
                             'Saarland',
                             'Schleswig-Holstein'],
                       'C': ['Baden-Württemberg'],
                       'D': ['Bremen'],
                       'E': ['Hessen']}
    SUPPORTER_SPECIAL_CASE = beihilfetraeger[SPECIAL_CASE][0]
    since_traeger = beihilfetraeger['C'][0]

    type_age_range = {'civil-servant': range(21, 103, 1),
                      # TODO: The original range is commented out - otherwise the FE 18YO validation catches...
                      # 'civil-servant-applicant': range(16, 37, 1),
                      'civil-servant-applicant': range(18, 37, 1),
                      'civil-servant-student-child': range(21, 28, 1),
                      'child': range(0, 21, 1)}

    since_values = ['2012-12-31', '2013-01-01']

    since_values_ui = {'2012-12-31': 'Vor dem oder am 31.12.2012',
                       '2013-01-01': 'Nach dem 31.12.2012'}

    case_letters = {SERVANT: 'E ',
                    APPLICANT: 'W ',
                    CHILD: 'K ',
                    STUDENT: 'A '
                    }

    bht_type_bhs = {'A': {SERVANT: [50, 70],
                          APPLICANT: [50, 70],
                          STUDENT: [80],
                          CHILD: [80]},
                    'B': {SERVANT: [50, 70],
                          APPLICANT: [50, 70],
                          STUDENT: [80],
                          CHILD: [80]},
                    'C': {SERVANT: [50, 70],
                          APPLICANT: [50, 70],
                          STUDENT: [80],
                          CHILD: [80]},
                    'D': {SERVANT: [50, 55, 60, 65, 70],
                          APPLICANT: [50, 55, 60, 65, 70],
                          STUDENT: [50, 55, 60, 65, 70],
                          CHILD: [50, 55, 60, 65, 70]},
                    'E': {SERVANT: [50, 55, 60, 65, 70],
                          APPLICANT: [50, 55, 60, 65, 70],
                          STUDENT: [50, 55, 60, 65, 70],
                          CHILD: [50, 55, 60, 65, 70]}
                    }

    @staticmethod
    def find_class(bht: str):
        for bht_class in CivilServantConfig.beihilfetraeger:
            if bht in CivilServantConfig.beihilfetraeger[bht_class]:
                return bht_class


class CivilServant(Printable):
    # job title in the signup selection : summary screen

    __provider = None
    provider_case = None
    __since = None
    __support = None
    __type = None

    def __init__(self,
                 _type: str or None,
                 _provider: str or None,
                 _since: str or None,
                 _support: int or None):
        # randomization handled by setter
        self.type = _type

        # randomization handled by setter
        self.provider = _provider

        # randomization handled by setter
        self.since = _since

        # randomization handled by setter
        self.support = _support

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, _type: str or None):
        # if servant type is None - randomize it
        if _type is None:
            _type = random.choice(list(CivilServantConfig.civ_serv_types.keys()))
            log("Randomized 'civil-servant' type = {0}".format(_type))

        # Handle possible errors
        if _type not in CivilServantConfig.civ_serv_types:
            p_e("Customer type '{0}' not supported. Check code!".format(_type))
            raise ValueError

        self.__type = _type

    @property
    def provider(self):
        return self.__provider

    @provider.setter
    def provider(self, _provider: str or None):
        # Make a random choice
        if _provider is None:
            # choose the provider_case first - that way each case is equally probable
            _provider_case = random.choice(list(CivilServantConfig.beihilfetraeger.keys()))
            # choose a random provider for the selected case.
            _provider = random.choice(CivilServantConfig.beihilfetraeger[_provider_case])
            log("Randomized 'civil-servant' provider = {0}, {1}".format(_provider_case, _provider))

        # Handle possible errors
        if not any(_provider in v for v in CivilServantConfig.beihilfetraeger.values()):
            p_e("Support provider '{0}' not supported. Check code!".format(_provider))
            raise ValueError
        self.__provider = _provider
        self.provider_case = CivilServantConfig.find_class(_provider)

    @property
    def since(self):
        return self.__since

    @since.setter
    def since(self, _since: str or None):
        # Make a random choice
        if _since is None:
            # just take first value. No randomization necessary
            if self.provider_case != CivilServantConfig.SPECIAL_CASE:
                _since = CivilServantConfig.since_values[0]
            # randomize
            else:
                _since = random.choice(CivilServantConfig.since_values)
                log("Randomized 'civil-servant' since = {0}".format(_since))

        # Handle possible errors
        if _since not in CivilServantConfig.since_values_ui:
            p_e("Since value '{0}' not supported. Check code!".format(_since))
            raise ValueError

        self.__since = _since

    @property
    def support(self):
        return self.__support

    @support.setter
    def support(self, _support: int or None):
        # Make a random choice
        if _support is None:
            _support = random.choice(CivilServantConfig.bht_type_bhs[self.provider_case][self.type])
            log("Randomized 'civil-servant' support = {0}".format(_support))
        else:
            # make sure it's an integer...
            _support = int(_support)

        # Handle possible errors
        if _support not in CivilServantConfig.bht_type_bhs[self.provider_case][self.type]:
            p_e("Support value '{0}' not supported for case '{1}' and type '{2}'. "
                "Check code!".format(_support,
                                     self.provider_case,
                                     self.type))
            raise ValueError

        self.__support = int(_support)

    @property
    def ui_comparable_support(self) -> str:
        return "{0}%".format(self.support)

    @property
    def ui_comparable_since(self) -> str:
        return CivilServantConfig.since_values_ui[self.since]

    @property
    def ui_comparable_type(self) -> str:
        return CivilServantConfig.civ_serv_types[self.type]


class User(object):
    # _INCOME_BOUNDARY = 60750

    # Full - Civil Servant
    T_PREMIUM = "Premium Economy Class"
    T_ECONOMY = "Economy Class"
    # Full - Civil Servant, Comprehensive
    T_BUSINESS = "Business Class"
    T_FIRST = "First Class"
    T_EXPAT = "Expat"
    # Topup Clinic
    T_EINBETT = "Klinik Einbett"
    T_ZWEIBETT = "Klinik Zweibett"
    T_ZWEIBETT_TWEN = "Klinik Zweibett Twen"

    P_COMPREHENSIVE_INSURANCE = "Vollversicherung"
    P_CIVIL_SERVANT_INSURANCE = "Beihilfeversicherung"
    P_TOPUP_DENTAL__INSURANCE = "Zahnzusatzversicherung"
    P_TOPUP_CLINIC__INSURANCE = "Krankenhauszusatzversicherung"



    SB_10 = "10 %"
    SB_25 = "25 %"

    tax_data_consent_dict = {True: 'erteilt',
                             False: 'nicht erteilt'}
    debit_auth_ui_summary = {True: 'Ja',
                             False: 'Nein'}

    consultation_status_ui_summary = {True: 'ist erfolgt',
                                      False: 'ZONK'}
    environment = None
    tariff_price = None
    consultation_appointment = None
    __date_of_birth = None
    age = None
    __nationality = None
    nationality_type = None
    nationality_id = None
    __permanent_residency = None
    __in_germany_since = None
    __visa_valid_until = None

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth
        self.age = self.age_in_years(date_of_birth=date_of_birth)

    @property
    def nationality(self):
        return self.__nationality

    @nationality.setter
    def nationality(self, nationality: str):
        self.__nationality = nationality
        if nationality is not None:
            self.__nationality, self.nationality_type, self.nationality_id = \
                User.check_nationality(nationality=nationality)

    @property
    def permanent_residency(self):
        return self.__permanent_residency

    @permanent_residency.setter
    def permanent_residency(self, permanent_residency):
        # in case not provided - Randomize, else just set
        if permanent_residency is None and self.nationality_type == C_NON_EU:
            self.__permanent_residency = random.choice([True, False])
        else:
            self.__permanent_residency = permanent_residency

    @property
    def in_germany_since(self):
        return self.__in_germany_since

    @in_germany_since.setter
    def in_germany_since(self, in_germany_since):
        # in case not provided - Randomize, else just set
        if in_germany_since is None and (self.nationality_type == C_NON_EU or self.nationality_type == C_EU):
            self.__in_germany_since = self.generate_in_germany_since(date_of_birth=self.date_of_birth)
        else:
            self.__in_germany_since = in_germany_since

    @property
    def visa_valid_until(self):
        return self.__visa_valid_until

    @visa_valid_until.setter
    def visa_valid_until(self, visa_valid_until):
        # in case not provided - Randomize, else just set
        if visa_valid_until is None and self.nationality_type == C_NON_EU and not self.permanent_residency:
            self.__visa_valid_until = self.generate_visa_valid()
        else:
            self.__visa_valid_until = visa_valid_until

    @staticmethod
    def insurance_date(date_of_birth: date, safe: bool = True):

        timespan_in_days = timedelta(days=random.randint(0, int(10 * 365.25) - 1))
        # generate ages 0-18 and 18-120
        if not safe:
            # TODO: There should be some more cases of unsafe results - insurance with another company made yesterday?
            timespan_in_days *= -1
        contract_date = date_of_birth + timespan_in_days
        return contract_date

    @staticmethod
    def generate_dob(safe: bool = True, too_young: bool = True, too_old: bool = False, low: int = 18, high: int = 120) \
            -> date:
        age_in_days = 0
        # generate ages 0-18 and 18-120
        if not safe:
            if too_young:
                age_in_days = timedelta(days=random.randint(0, int(18 * 365.25) - 1))
            elif too_old:
                age_in_days = timedelta(days=random.randint(int(87 * 365.25), int(120 * 365.25)))
        else:
            age_in_days = timedelta(days=random.randint(int(low * 365.25) + 1, int(high * 365.25)))
        now = date.today()
        date_of_birth = now - age_in_days
        log("Generated DOB, age: {0}, {1}".format(date_of_birth.strftime(DATE_YMD), User.age_in_years(date_of_birth)))
        return date_of_birth

    @staticmethod
    def generate_in_germany_since(date_of_birth: date, safe: bool = True) \
            -> date:
        _LO = 'too low'
        _HI = 'too high'
        options = [_HI, _LO]
        safe_days_interval = (date.today() - date_of_birth).days
        dob = User.generate_dob(safe=True, low=21, high=50)
        if safe:
            in_germany_since_date = date.today() - timedelta(days=random.randint(0, safe_days_interval))
        else:
            option = random.choice(options)
            if option == _HI:
                in_germany_since_date = date.today() + timedelta(days=random.randint(1, 50*365.25))
            else:
                in_germany_since_date = dob - timedelta(days=random.randint(1, 50*365.25))
        log("Generated in-Germany-since date: {0}".format(in_germany_since_date))
        return in_germany_since_date

    @staticmethod
    def generate_visa_valid(safe: bool = True) \
            -> date:

        safe_days_interval = ((datetime.date.today() + relativedelta(years=10)) - datetime.date.today()).days
        if safe:
            visa_valid_date = date.today() + timedelta(days=random.randint(0, safe_days_interval))
        else:
            visa_valid_date = date.today() + timedelta(days=random.randint(safe_days_interval+1, 3*safe_days_interval))
        log("Generated VISA-valid date: {0}".format(visa_valid_date))
        return visa_valid_date

    @staticmethod
    def generate_dob_age_away_from_date(reference_date: date, age: int) \
            -> date:
        age_in_days = timedelta(days=random.randint(int(age * 365.25) + 1, int((age + 1) * 365.25)))
        date_of_birth = reference_date - age_in_days
        print("Generated DOB, age: {0}, {1}".format(date_of_birth.strftime(DATE_YMD),
                                                    User.age_in_years_at_date(date_of_birth, reference_date)))
        return date_of_birth

    @staticmethod
    def age_in_years(date_of_birth: date) -> int:
        now = date.today()
        time_delta = now - date_of_birth
        return int(abs(time_delta.days / 365.25))

    @staticmethod
    def age_in_years_at_date(date_of_birth: date, reference_date: date) -> int:
        time_delta = reference_date - date_of_birth
        return int(abs(time_delta.days / 365.25))

    @staticmethod
    def age_in_years_at_insurance_date(date_of_birth: date, insurance_date: date) -> int:
        time_delta = insurance_date - date_of_birth
        return int(abs(time_delta.days / 365.25))

    @staticmethod
    def age_in_years_at_insurance_date_pvb(date_of_birth: date, insurance_date: date) -> int:
        return int(insurance_date.year - date_of_birth.year)

    @property
    def is_age_diff_pvb(self) -> bool:
        _result = False
        if self.date_of_birth.month == self.insurance_start_date.month:
            if self.date_of_birth.day >= self.insurance_start_date.day:
                _result = True
        elif self.date_of_birth.month > self.insurance_start_date.month:
            _result = True
        else:
            _result = False
        log("Customer age_diff for PVB={0}".format(_result))
        return _result

    @staticmethod
    def generate_nationality(option: str = C_DE) -> {}:
        if option == C_ANY:
            return random.choice(countries)
        if option not in C_OPTIONS:
            p_d("Country option '{0}' not supported. Check code!".format(option))
        for country in countries:
            if country['option'] == option:
                return country

    @staticmethod
    def check_nationality(nationality: str) -> (str, str, str):
        """

        :param nationality:
        :return:
            country-label (i.e. 'Deutschland')
            country-option (i.e. C_DE)
            country-value (i.e. 'DE')
        """
        for country in countries:
            if country['label'] == nationality or country['value'] == nationality or country['option'] == nationality:
                return country['label'], country['option'], country['value']
        p_d("Could not find country '{0}' in supported country list. Check code!".format(nationality))
        raise ValueError

    def __init__(self,
                 date_of_birth: date,
                 nationality: str,

                 forename: str,
                 lastname: str,
                 title: str or None,
                 mobile: str,
                 email: str,
                 address: Address,

                 bmi_parameters: BodyMassIndex,
                 previous_insurance: PreviousInsurance,
                 occupation: Occupation,
                 civil_servant: CivilServant or None,
                 # None in case of CIVIL_SERVANT
                 age_contribution_relief: AgeContributionRelief or None,
                 # None in case of CIVIL_SERVANT
                 daily_sickness_allowance: DailySicknessAllowance or None,
                 health_questions: HealthQuestions,

                 transfer_value: int or None,
                 transfer_value_known: bool,
                 transfer_requested: bool,

                 iban: IBAN,
                 direct_debit_authorization: bool,

                 insurance_start_date: date or None,
                 consultation_requested_date: datetime or None,
                 request_consultation: bool,

                 # provide_tax_id: str,
                 # tax_id: str or None,
                 # tax_id_permission: bool,

                 product: str,
                 tariff: str,
                 # None in case of CIVIL_SERVANT
                 cost_participation: str or None,
                 # health_box: str or None,

                 # DEFAULT PARAMETERS
                 permanent_residency: bool or None = None,
                 visa_valid_until: date or None = None,
                 in_germany_since: date or None = None,

                 account_created: bool = False,
                 last_signup_stage_completed: int = 0,
                 signup_completed: bool = False,
                 consultation_completed: bool = False,
                 underwriting_completed: bool = False,
                 offer_to_be_accepted: bool = True,
                 offer_accepted: bool = False,
                 # TODO: check if 'offer_accepted' isn't the same as 'contract_signed'
                 contract_signed: bool = False,
                 expected_rejection: bool = False,
                 signup_rejected: bool = False,

                 crm_id: str = None,
                 _password: str = "7Zeichen"
                 ):
        locale.setlocale(locale.LC_MONETARY, 'de_DE.UTF-8')

        # === personal information
        self.date_of_birth = date_of_birth
        self.bmi_parameters = bmi_parameters
        self.nationality = nationality
        self.permanent_residency = permanent_residency
        self.in_germany_since = in_germany_since
        self.visa_valid_until = visa_valid_until
        self.occupation = occupation

        # === payments details
        self.iban = iban
        self.direct_debit_authorization = direct_debit_authorization

        # === contact information
        self.forename = forename
        self.lastname = lastname
        self.title = title
        self.email = email.lower()
        log("Email was lowered to '{0}'".format(self.email))
        # this is the case for mobile numbers inside the DE network
        if mobile.startswith("0"):
            # replaces the starting '0' with the DE direction number
            mobile = re.sub('^%s' % "0", "+49", mobile)
        self.mobile = mobile
        # TODO: consider adding checks for the dictionary
        self.address = address

        self.expected_rejection = expected_rejection
        self.signup_rejected = signup_rejected

        self.previous_insurance = previous_insurance

        self.transfer_value = transfer_value
        self.transfer_value_known = transfer_value_known
        self.transfer_requested = transfer_requested

        self.age_contribution_relief = age_contribution_relief
        self.daily_sickness_allowance = daily_sickness_allowance

        # === beihilfe
        # TODO: Write a setter for this
        self.civil_servant = civil_servant
        if self.civil_servant is not None:
            if self.civil_servant.type in CivilServantConfig.civ_serv_types:
                self.occupation_type = CivilServantConfig.civ_serv_types[self.civil_servant.type]
            else:
                p_d("The civil servant type: {0} - is not supported. Inspect code!".
                    format(self.civil_servant.type))

        # === medical information
        self.health_questions = health_questions

        # === new insurance data
        self.insurance_start_date = insurance_start_date
        # TODO: Write a setter for this
        self.request_consultation = request_consultation
        if consultation_requested_date is not None:
            self.consultation_requested_date = consultation_requested_date
            self.consultation_requested = True
        else:
            self.consultation_requested = False
        self.product = product
        self.tariff = tariff
        self.cost_participation = cost_participation

        self.account_created = account_created
        self.last_signup_stage_completed = last_signup_stage_completed
        self.signup_completed = signup_completed
        self.consultation_completed = consultation_completed
        self.underwriting_completed = underwriting_completed
        self.offer_to_be_accepted = offer_to_be_accepted
        self.offer_accepted = offer_accepted
        self.contract_signed = contract_signed

        # === CRM data
        self.crm_id = crm_id

        self.password = _password

    crm_id = None

    def set_dob_and_age(self, date_of_birth: datetime.date):
        self.date_of_birth = date_of_birth
        self.age = self.age_in_years(date_of_birth=date_of_birth)

    def set_consultation_requested_date(self, _date: date or None):
        self.consultation_requested_date = _date
        if _date is None:
            self.consultation_requested = False
        else:
            self.consultation_requested = True

    # TODO: What if the user has a title?
    @property
    def fullname(self) -> str:
        return "{0} {1}".format(self.forename, self.lastname)

    @property
    def ui_comparable_consultation(self) -> str:
        return self.consultation_status_ui_summary[self.consultation_completed]

    @property
    def ui_comparable_debit_authorization(self) -> str:
        return self.debit_auth_ui_summary[self.direct_debit_authorization]

    @property
    def transfer_value_expected(self) -> bool:
        if self.previous_insurance.pi_type == PreviousInsurance.PKV:
            log("The user should have a transfer value")
            if int(self.previous_insurance.pi_date.strftime("%Y")) >= 2009:
                if self.age < 21:
                    log("The transfer value should be zero - due to age < 21")
                    return False
                else:
                    log("The transfer value should be non-zero")
                    return True
            else:
                log("The transfer value should be zero - due to insurance date < 2009")
                return False
        else:
            log("The user should NOT have a transfer value - due to insurance type != privat")
            return False

#
# class ConsultationUser(object):
#     environment = None
#
#     def __init__(self,
#                  _forename: str,
#                  _lastname: str,
#                  _telephone: str,
#                  _email: str,
#                  _interested_in: str,
#                  _consent: bool):
#         # === contact information
#         self.forename = _forename
#         self.lastname = _lastname
#         self.email = _email
#         # this is the case for mobile numbers inside the DE network
#         if _telephone.startswith("0"):
#             # replaces the starting '0' with the DE direction number
#             _telephone = re.sub('^%s' % "0", "+49", _telephone)
#         self.telephone = _telephone
#         if _interested_in == "RANDOM" or _interested_in == "":
#             _interested_in = "RANDOM"
#         self.interested_in = _interested_in
#         self.consent = _consent
#
#
# def generate_consultation_user(number_string: str) -> ConsultationUser:
#     letter_string = ""
#     for c in number_string:
#         letter_string += chr(ord('A') + int(c))
#     # _forename, _lastname, _email = generate_user_name_from_number(number_string, "bchmura+AT-OA-Consultation-")
#     _forename, _lastname, _email = generate_user_name_from_number(number_string, "bc+AT-OA-Consultation-")
#     u = ConsultationUser(_forename=_forename,
#                          _lastname=_lastname,
#                          _email=_email,
#                          _telephone=telephone,
#                          _interested_in="",
#                          _consent=True)
#     return u
#
#
# bmi_params = BodyMassIndex.generate_weight_height_bmi(mode=BodyMassIndex.M_OK)
# dob = User.generate_dob(safe=True, low=21, high=50)
#
#
# def generate_user(number_string: str,
#                   age: int = None,
#                   previous_insurance_type: str = None,
#                   nationality_group: str = C_DE,
#                   permanent_residency: bool or None = None,
#                   product: str = User.P_COMPREHENSIVE_INSURANCE) -> User:
#     letter_string = ""
#     for c in number_string:
#         letter_string += chr(ord('A') + int(c))
#     _bmi_params = BodyMassIndex.generate_weight_height_bmi(mode=BodyMassIndex.M_OK)
#     _forename, _lastname, _email = generate_user_name_from_number(number_string, "bc+AUTO-comprehensive-")
#
#     if age is None:
#         _dob = User.generate_dob(safe=True, low=21, high=50)
#     else:
#         _dob = User.generate_dob(safe=True, low=age, high=age + 1)
#
#     _nationality = User.generate_nationality(option=nationality_group)['label']
#
#     u = User(forename=_forename,
#              lastname=_lastname,
#              title=None,
#
#              mobile=telephone,
#              email=_email,
#              address=Address(postal_code="85748",
#                              city="Garching b München",
#                              street="Schrödingerweg",
#                              nr="2"),
#
#              # RANDOMIZED if =None, though obsolete in this case
#              civil_servant=None,
#
#              date_of_birth=_dob,
#              bmi_parameters=BodyMassIndex(weight=_bmi_params[0],
#                                           height=_bmi_params[1],
#                                           bmi=_bmi_params[2],
#                                           mode=_bmi_params[3],
#                                           # if set to None = will be randomized
#                                           gender=None),
#              nationality=_nationality,
#              # will be randomized to a safe value based on nationality, or left as None if not needed
#              permanent_residency=permanent_residency,
#              # will be randomized to a safe value based on nationality, or left as None if not needed
#              in_germany_since=None,
#              # will be randomized to a safe value based on nationality, or left as None if not needed
#              visa_valid_until=None,
#              # RANDOMIZED VIA UI if =None
#              occupation=Occupation(_name=None,
#                                    _type=Occupation.O_EMPLOYEE,
#                                    _income=Occupation.generate_income(safe=True),
#                                    _randomize=True),
#
#              # will be randomized
#              iban=IBAN(),
#              direct_debit_authorization=True,
#
#              previous_insurance=PreviousInsurance(_type=previous_insurance_type,
#                                                   # will be randomized (if AKV path taken)
#                                                   _country=None,
#                                                   # will be randomized, or defaulted if AKV
#                                                   _name=None,
#                                                   # will be randomized
#                                                   _date=PreviousInsurance.generate_date(date_of_birth=_dob,
#                                                                                         safe=True),
#                                                   _state=PreviousInsurance.S_____CANCELLED,
#                                                   _fees=False,
#                                                   _emergency_tariff=False),
#
#              transfer_value=None,
#              transfer_value_known=False,
#              transfer_requested=True,
#              age_contribution_relief=AgeContributionRelief(_year=None,
#                                                            _amount=None,
#                                                            _requested=True,
#                                                            _randomize=True),
#              daily_sickness_allowance=DailySicknessAllowance(_from=None,
#                                                              _amount=None,
#                                                              _requested=True,
#                                                              _randomize=True),
#
#              health_questions=HealthQuestions(medication=False,
#                                               treatment=False,
#                                               allergy=False,
#                                               hospitalization=False,
#                                               psychological=False,
#                                               malignant=False,
#                                               chronic=False,
#                                               hiv=False,
#                                               addictions=False,
#                                               impairments=NewHealthImpairments(hearing_aid=False,
#                                                                                body_implant=False,
#                                                                                prosthetic=False,
#                                                                                infertility=False,
#                                                                                disability=False,
#                                                                                occupational_disability=False,
#                                                                                military_injuries=False,
#                                                                                missing_teeth=False),
#                                               planned=False),
#              insurance_start_date=None,
#              # TODO: Add randomization
#              request_consultation=True,
#              # will be set
#              consultation_requested_date=None,
#              # provide_tax_id="nachreichen",
#              # tax_id=None,
#              # # TODO: Add randomization
#              # tax_id_permission=False,
#              product=product,
#              tariff=User.T_BUSINESS,
#              cost_participation=User.SB_25,
#
#              # will be randomized
#              # health_box=None,
#
#              account_created=False,
#              last_signup_stage_completed=0,
#              signup_completed=False,
#              consultation_completed=False,
#              underwriting_completed=False,
#              offer_accepted=False,
#              expected_rejection=False,
#              signup_rejected=False,
#
#              _password="7Zeichen")
#     u.terminate_at_end_of_stage = 10
#
#     return u
#
#
# def generate_user_name_from_number(number_string: str, email_prefix: str) -> (str, str, str):
#     letter_string = ""
#     for c in number_string:
#         letter_string += chr(ord('A') + int(c))
#     # return "Tab1_Passender_Tariff " + letter_string + " V", "Tab1_Passender_Tariff " + letter_string + " N", email_prefix + number_string + "@gmail.com"
#     return "Tab1_Passender_Tariff " + letter_string + " V", \
#            "Tab1_Passender_Tariff " + letter_string + " N", \
#            email_prefix + number_string + "@on-testing.de"
#
#
# def generate_number_from_ordinal_string(ordinal_string: str) -> int:
#     number = 0
#     for o in ordinal_string:
#         number *= 10
#         number += ord(o) - ord('A') + 1
#     return number
#
#
# def generate_user_beihilfe(number_string: str,
#                            age: int = None,
#                            previous_insurance_type: str = None,
#                            nationality_group: str = C_DE,
#                            permanent_residency: bool or None = None,
#                            product: str = User.P_CIVIL_SERVANT_INSURANCE) -> User:
#     log("Generating BEIHILFE user {0}".format(number_string))
#
#     civil_servant = CivilServant(_type=None,
#                                  _provider=None,
#                                  _since=None,
#                                  _support=None)
#
#     _bmi_params = BodyMassIndex.generate_weight_height_bmi(mode=BodyMassIndex.M_OK)
#     _forename, _lastname, _email = generate_user_name_from_number(number_string, "bc+AUTO-beihilfe-")
#
#     if age is None:
#         _dob = User.generate_dob(safe=True,
#                                  low=CivilServantConfig.type_age_range[civil_servant.type].start,
#                                  # This should turn off the failing cases of >70 aged
#                                  # TODO: Remove the min, once the bug is fixed!
#                                  high=min(CivilServantConfig.type_age_range[civil_servant.type].stop - 1, 70))
#     else:
#         _dob = User.generate_dob(safe=True, low=age, high=age + 1)
#
#     _nationality = User.generate_nationality(option=nationality_group)['label']
#
#     u = User(forename=_forename,
#              lastname=_lastname,
#              title=None,
#
#              mobile=telephone,
#              email=_email,
#              address=Address(postal_code="85748",
#                              city="Garching b München",
#                              street="Schrödingerweg",
#                              nr="2"),
#
#              # RANDOMIZED if =None
#              civil_servant=civil_servant,
#
#              # RANDOMIZED if =None
#              date_of_birth=_dob,
#              bmi_parameters=BodyMassIndex(weight=_bmi_params[0],
#                                           height=_bmi_params[1],
#                                           bmi=_bmi_params[2],
#                                           mode=_bmi_params[3],
#                                           # if set to None = will be randomized
#                                           gender=None),
#              nationality=_nationality,
#              # will be randomized to a safe value based on nationality, or left as None if not needed
#              permanent_residency=permanent_residency,
#              # will be randomized to a safe value based on nationality, or left as None if not needed
#              in_germany_since=None,
#              # will be randomized to a safe value based on nationality, or left as None if not needed
#              visa_valid_until=None,
#              # RANDOMIZED VIA UI if =None
#              occupation=Occupation(_name=None,
#                                    _type=civil_servant.ui_comparable_type,
#                                    _income=Occupation.generate_income(safe=True),
#                                    _randomize=True),
#
#              # will be randomized
#              iban=IBAN(),
#              direct_debit_authorization=True,
#
#              previous_insurance=PreviousInsurance(_type=previous_insurance_type,
#                                                   # will be randomized (if AKV path taken)
#                                                   _country=None,
#                                                   # will be randomized, or defaulted if AKV
#                                                   _name=None,
#                                                   # will be randomized
#                                                   _date=PreviousInsurance.generate_date(date_of_birth=_dob,
#                                                                                         safe=True),
#                                                   _state=PreviousInsurance.S_____CANCELLED,
#                                                   _fees=False,
#                                                   _emergency_tariff=False),
#
#              transfer_value=None,
#              transfer_value_known=False,
#              transfer_requested=True,
#              age_contribution_relief=AgeContributionRelief(_year=None,
#                                                            _amount=None,
#                                                            _requested=True,
#                                                            _randomize=True),
#              daily_sickness_allowance=DailySicknessAllowance(_from=None,
#                                                              _amount=None,
#                                                              _requested=True,
#                                                              _randomize=True),
#
#              health_questions=HealthQuestions(medication=False,
#                                               treatment=False,
#                                               allergy=False,
#                                               hospitalization=False,
#                                               psychological=False,
#                                               malignant=False,
#                                               chronic=False,
#                                               hiv=False,
#                                               addictions=False,
#                                               impairments=NewHealthImpairments(hearing_aid=False,
#                                                                                body_implant=False,
#                                                                                prosthetic=False,
#                                                                                infertility=False,
#                                                                                disability=False,
#                                                                                occupational_disability=False,
#                                                                                military_injuries=False,
#                                                                                missing_teeth=False),
#                                               planned=False),
#              # TODO: check the difference between this and comprehensive
#              insurance_start_date=make_insurance_date(safe=True),
#              request_consultation=True,
#              consultation_requested_date=None,
#              # provide_tax_id="nachreichen",
#              # tax_id=None,
#              # # TODO: Add randomization
#              # tax_id_permission=False,
#              product=product,
#              tariff=User.T_BUSINESS,
#              cost_participation=User.SB_10,
#
#              # will be randomized
#              # health_box=None,
#
#              account_created=False,
#              last_signup_stage_completed=0,
#              signup_completed=False,
#              consultation_completed=False,
#              underwriting_completed=False,
#              offer_accepted=False,
#              expected_rejection=False,
#              signup_rejected=False)
#     u.terminate_at_end_of_stage = 10
#
#     return u
#
#
# def generate_user_beihilfe_foreign(number_string: str) -> User:
#     log("Generating BEIHILFE user {0}".format(number_string))
#
#     letter_string = ""
#     for c in number_string:
#         letter_string += chr(ord('A') + int(c))
#
#     civil_servant = CivilServant(_type=None,
#                                  _provider=None,
#                                  _since=None,
#                                  _support=None)
#
#     _bmi_params = BodyMassIndex.generate_weight_height_bmi(mode=BodyMassIndex.M_OK)
#     _forename, _lastname, _email = generate_user_name_from_number(number_string, "bc+AUTO-beihilfe-")
#
#     _dob = User.generate_dob(safe=True,
#                              low=CivilServantConfig.type_age_range[civil_servant.type].start,
#                              # This should turn off the failing cases of >70 aged
#                              # TODO: Remove the min, once the bug is fixed!
#                              high=min(CivilServantConfig.type_age_range[civil_servant.type].stop - 1, 70))
#
#     # TODO: Consider making a separate method for C_NON_EU
#     _nationality = User.generate_nationality(option=C_EU)['label']
#     permanent_residency = True
#
#     u = User(forename=_forename,
#              lastname=_lastname,
#              title=None,
#
#              mobile=telephone,
#              email=_email,
#              address=Address(postal_code="85748",
#                              city="Garching b München",
#                              street="Schrödingerweg",
#                              nr="2"),
#
#              # RANDOMIZED if =None
#              civil_servant=civil_servant,
#
#              # RANDOMIZED if =None
#              date_of_birth=_dob,
#              bmi_parameters=BodyMassIndex(weight=_bmi_params[0],
#                                           height=_bmi_params[1],
#                                           bmi=_bmi_params[2],
#                                           mode=_bmi_params[3],
#                                           gender=None),
#              nationality=_nationality,
#              # will be randomized to a safe value based on nationality, or left as None if not needed
#              permanent_residency=permanent_residency,
#              # will be randomized to a safe value based on nationality, or left as None if not needed
#              in_germany_since=None,
#              # will be randomized to a safe value based on nationality, or left as None if not needed
#              visa_valid_until=None,
#              # RANDOMIZED VIA UI if =None
#              occupation=Occupation(_name=None,
#                                    _type=random.choice(list(CivilServantConfig.civ_serv_types.values())),
#                                    _income=Occupation.generate_income(safe=True),
#                                    _randomize=True),
#
#              # will be randomized
#              iban=IBAN(),
#              direct_debit_authorization=True,
#
#              previous_insurance=PreviousInsurance(_type=PreviousInsurance.AKV,
#                                                   # will be randomized (if AKV path taken)
#                                                   _country=None,
#                                                   # will be randomized, or defaulted if AKV
#                                                   _name=None,
#                                                   # will be randomized
#                                                   _date=PreviousInsurance.generate_date(date_of_birth=_dob,
#                                                                                         safe=True),
#                                                   _state=PreviousInsurance.S_____CANCELLED,
#                                                   _fees=False,
#                                                   _emergency_tariff=False),
#
#              transfer_value=None,
#              transfer_value_known=False,
#              transfer_requested=True,
#              age_contribution_relief=AgeContributionRelief(_year=AgeContributionRelief.BEK___64,
#                                                            _amount=None,
#                                                            _requested=True,
#                                                            _randomize=True),
#              daily_sickness_allowance=DailySicknessAllowance(_from=None,
#                                                              _amount=None,
#                                                              _requested=True,
#                                                              _randomize=True),
#              health_questions=HealthQuestions(medication=False,
#                                               treatment=False,
#                                               allergy=False,
#                                               hospitalization=False,
#                                               psychological=False,
#                                               malignant=False,
#                                               chronic=False,
#                                               hiv=False,
#                                               addictions=False,
#                                               impairments=NewHealthImpairments(hearing_aid=False,
#                                                                                body_implant=False,
#                                                                                prosthetic=False,
#                                                                                infertility=False,
#                                                                                disability=False,
#                                                                                occupational_disability=False,
#                                                                                military_injuries=False,
#                                                                                missing_teeth=False),
#                                               planned=False),
#              insurance_start_date=make_insurance_date(safe=True),
#              request_consultation=True,
#              consultation_requested_date=None,
#              # provide_tax_id="nachreichen",
#              # tax_id=None,
#              # # TODO: Add randomization
#              # tax_id_permission=False,
#              product=User.P_CIVIL_SERVANT_INSURANCE,
#              tariff=User.T_BUSINESS,
#              cost_participation=User.SB_10,
#
#              # will be randomized
#              # health_box=None,
#
#              account_created=False,
#              last_signup_stage_completed=0,
#              signup_completed=False,
#              consultation_completed=False,
#              underwriting_completed=False,
#              offer_accepted=False,
#              expected_rejection=False,
#              signup_rejected=False)
#     return u
#
#
# def generate_user_beihilfe_foreign_bawu(number_string: str) -> User:
#     log("Generating BEIHILFE user {0}".format(number_string))
#     letter_string = ""
#     for c in number_string:
#         letter_string += chr(ord('A') + int(c))
#     _bmi_params = BodyMassIndex.generate_weight_height_bmi(mode=BodyMassIndex.M_OK)
#     _forename, _lastname, _email = generate_user_name_from_number(number_string, "bc+AUTO-beihilfe-")
#     civil_servant = CivilServant(_type="civil-servant",
#                                  _provider="Baden-Württemberg",
#                                  _since=None,
#                                  _support=50)
#
#     _dob = User.generate_dob(safe=True,
#                              low=CivilServantConfig.type_age_range[civil_servant.type].start,
#                              # This should turn off the failing cases of >70 aged
#                              # TODO: Remove the min, once the bug is fixed!
#                              high=min(CivilServantConfig.type_age_range[civil_servant.type].stop - 1, 70))
#     u = User(forename=_forename,
#              lastname=_lastname,
#              title=None,
#
#              mobile=telephone,
#              email=_email,
#              address=Address(postal_code="85748",
#                              city="Garching b München",
#                              street="Schrödingerweg",
#                              nr="2"),
#
#              # RANDOMIZED if =None
#              civil_servant=civil_servant,
#
#              # RANDOMIZED if =None
#              date_of_birth=_dob,
#              bmi_parameters=BodyMassIndex(weight=_bmi_params[0],
#                                           height=_bmi_params[1],
#                                           bmi=_bmi_params[2],
#                                           mode=_bmi_params[3],
#                                           gender=None),
#              nationality=C_DE,
#              # RANDOMIZED VIA UI if =None
#              occupation=Occupation(_name=None,
#                                    _type=random.choice(list(CivilServantConfig.civ_serv_types.values())),
#                                    _income=Occupation.generate_income(safe=True),
#                                    _randomize=True),
#
#              # will be randomized
#              iban=IBAN(),
#              direct_debit_authorization=True,
#
#              previous_insurance=PreviousInsurance(_type=PreviousInsurance.AKV,
#                                                   # will be randomized (if AKV path taken)
#                                                   _country=None,
#                                                   # will be randomized, or defaulted if AKV
#                                                   _name=None,
#                                                   # will be randomized
#                                                   _date=PreviousInsurance.generate_date(date_of_birth=_dob,
#                                                                                         safe=True),
#                                                   _state=PreviousInsurance.S_____CANCELLED,
#                                                   _fees=False,
#                                                   _emergency_tariff=False),
#              transfer_value=None,
#              transfer_value_known=False,
#              transfer_requested=True,
#              age_contribution_relief=AgeContributionRelief(_year=AgeContributionRelief.BEK___64,
#                                                            _amount=None,
#                                                            _requested=True,
#                                                            _randomize=True),
#              daily_sickness_allowance=DailySicknessAllowance(_from=None,
#                                                              _amount=None,
#                                                              _requested=True,
#                                                              _randomize=True),
#              health_questions=HealthQuestions(medication=False,
#                                               treatment=False,
#                                               allergy=False,
#                                               hospitalization=False,
#                                               psychological=False,
#                                               malignant=False,
#                                               chronic=False,
#                                               hiv=False,
#                                               addictions=False,
#                                               impairments=NewHealthImpairments(hearing_aid=False,
#                                                                                body_implant=False,
#                                                                                prosthetic=False,
#                                                                                infertility=False,
#                                                                                disability=False,
#                                                                                occupational_disability=False,
#                                                                                military_injuries=False,
#                                                                                missing_teeth=False),
#                                               planned=False),
#              insurance_start_date=make_insurance_date(safe=True),
#              request_consultation=True,
#              consultation_requested_date=None,
#              # provide_tax_id="nachreichen",
#              # tax_id=None,
#              # # TODO: Add randomization
#              # tax_id_permission=False,
#              product=User.P_CIVIL_SERVANT_INSURANCE,
#              tariff=User.T_BUSINESS,
#              cost_participation=User.SB_10,
#
#              # will be randomized
#              # health_box=None,
#
#              account_created=False,
#              last_signup_stage_completed=0,
#              signup_completed=False,
#              consultation_completed=False,
#              underwriting_completed=False,
#              offer_accepted=False,
#              expected_rejection=False,
#              signup_rejected=False)
#     u.terminate_at_end_of_stage = 10
#
#     return u
#
#
# def generate_user_beihilfe_sachsen_bug(number_string: str) -> User:
#     log("Generating BEIHILFE user {0}".format(number_string))
#     letter_string = ""
#     for c in number_string:
#         letter_string += chr(ord('A') + int(c))
#     _bmi_params = BodyMassIndex.generate_weight_height_bmi(mode=BodyMassIndex.M_OK)
#     _forename, _lastname, _email = generate_user_name_from_number(number_string, "bc+AUTO-beihilfe-")
#     civil_servant = CivilServant(_type=CivilServantConfig.APPLICANT,
#                                  _provider="Sachsen",
#                                  _since=None,
#                                  _support=70)
#
#     _dob = User.generate_dob(safe=True,
#                              low=CivilServantConfig.type_age_range[civil_servant.type].start,
#                              # This should turn off the failing cases of >70 aged
#                              # TODO: Remove the min, once the bug is fixed!
#                              high=min(CivilServantConfig.type_age_range[civil_servant.type].stop - 1, 70))
#     u = User(forename=_forename,
#              lastname=_lastname,
#              title=None,
#
#              mobile=telephone,
#              email=_email,
#              address=Address(postal_code="85748",
#                              city="Garching b München",
#                              street="Schrödingerweg",
#                              nr="2"),
#
#              # RANDOMIZED if =None
#              civil_servant=civil_servant,
#
#              # RANDOMIZED if =None
#              date_of_birth=_dob,
#              bmi_parameters=BodyMassIndex(weight=_bmi_params[0],
#                                           height=_bmi_params[1],
#                                           bmi=_bmi_params[2],
#                                           mode=_bmi_params[3],
#                                           gender=None),
#              nationality=C_DE,
#              # RANDOMIZED VIA UI if =None
#              occupation=Occupation(_name=CivilServantConfig.civ_serv_types[civil_servant.type],
#                                    _type=civil_servant.type,
#                                    _income=Occupation.generate_income(safe=True),
#                                    _randomize=True),
#              # will be randomized
#              iban=IBAN(),
#              direct_debit_authorization=True,
#
#              previous_insurance=PreviousInsurance(_type=PreviousInsurance.GKV,
#                                                   # will be randomized (if AKV path taken)
#                                                   _country=None,
#                                                   # will be randomized, or defaulted if AKV
#                                                   _name=None,
#                                                   # will be randomized
#                                                   _date=PreviousInsurance.generate_date(date_of_birth=_dob,
#                                                                                         safe=True),
#                                                   _state=PreviousInsurance.S_____CANCELLED,
#                                                   _fees=False,
#                                                   _emergency_tariff=False),
#              transfer_value=None,
#              transfer_value_known=False,
#              transfer_requested=True,
#              age_contribution_relief=AgeContributionRelief(_year=AgeContributionRelief.BEK___64,
#                                                            _amount=None,
#                                                            _requested=True,
#                                                            _randomize=True),
#              daily_sickness_allowance=DailySicknessAllowance(_from=None,
#                                                              _amount=None,
#                                                              _requested=True,
#                                                              _randomize=True),
#              health_questions=HealthQuestions(medication=False,
#                                               treatment=False,
#                                               allergy=False,
#                                               hospitalization=False,
#                                               psychological=False,
#                                               malignant=False,
#                                               chronic=False,
#                                               hiv=False,
#                                               addictions=False,
#                                               impairments=NewHealthImpairments(hearing_aid=False,
#                                                                                body_implant=False,
#                                                                                prosthetic=False,
#                                                                                infertility=False,
#                                                                                disability=False,
#                                                                                occupational_disability=False,
#                                                                                military_injuries=False,
#                                                                                missing_teeth=False),
#                                               planned=False),
#              insurance_start_date=make_insurance_date(safe=True),
#              request_consultation=True,
#              consultation_requested_date=None,
#              # provide_tax_id="nachreichen",
#              # tax_id=None,
#              # # TODO: Add randomization
#              # tax_id_permission=False,
#              product=User.P_CIVIL_SERVANT_INSURANCE,
#              tariff=User.T_BUSINESS,
#              cost_participation=User.SB_10,
#
#              # will be randomized
#              # health_box=None,
#
#              account_created=False,
#              last_signup_stage_completed=0,
#              signup_completed=False,
#              consultation_completed=False,
#              underwriting_completed=False,
#              offer_accepted=False,
#              expected_rejection=False,
#              signup_rejected=False)
#     u.terminate_at_end_of_stage = 10
#
#     return u
#
#
# def generate_user_beihilfe_6424(number_string: str) -> User:
#     log("Generating BEIHILFE user {0}".format(number_string))
#     letter_string = ""
#     for c in number_string:
#         letter_string += chr(ord('A') + int(c))
#     _bmi_params = BodyMassIndex.generate_weight_height_bmi(mode=BodyMassIndex.M_OK)
#     # _forename, _lastname, _email = generate_user_name_from_number(number_string, "bchmura+AUTO-beihilfe-")
#     _forename, _lastname, _email = generate_user_name_from_number(number_string, "bc+AUTO-beihilfe-")
#     civil_servant = CivilServant(_type=CivilServantConfig.SERVANT,
#                                  _provider="Baden-Württemberg",
#                                  _since='2013-01-01',
#                                  _support=70)
#
#     _dob = User.generate_dob(safe=True,
#                              low=CivilServantConfig.type_age_range[civil_servant.type].start,
#                              # This should turn off the failing cases of >70 aged
#                              # TODO: Remove the min, once the bug is fixed!
#                              high=min(CivilServantConfig.type_age_range[civil_servant.type].stop - 1, 70))
#     u = User(forename=_forename,
#              lastname=_lastname,
#              title=None,
#
#              mobile=telephone,
#              email=_email,
#              address=Address(postal_code="85748",
#                              city="Garching b München",
#                              street="Schrödingerweg",
#                              nr="2"),
#
#              # RANDOMIZED if =None
#              civil_servant=civil_servant,
#              date_of_birth=_dob,
#              bmi_parameters=BodyMassIndex(weight=_bmi_params[0],
#                                           height=_bmi_params[1],
#                                           bmi=_bmi_params[2],
#                                           mode=_bmi_params[3],
#                                           gender=None),
#              nationality=C_DE,
#              # RANDOMIZED VIA UI if =None
#              occupation=Occupation(_name=None,
#                                    _type=random.choice(list(CivilServantConfig.civ_serv_types.values())),
#                                    _income=Occupation.generate_income(safe=True),
#                                    _randomize=True),
#              # will be randomized
#              iban=IBAN(),
#              direct_debit_authorization=True,
#
#              previous_insurance=PreviousInsurance(_type=PreviousInsurance.AKV,
#                                                   # will be randomized (if AKV path taken)
#                                                   _country=None,
#                                                   # will be randomized, or defaulted if AKV
#                                                   _name=None,
#                                                   # will be randomized
#                                                   _date=PreviousInsurance.generate_date(date_of_birth=_dob,
#                                                                                         safe=True),
#                                                   _state=PreviousInsurance.S_____CANCELLED,
#                                                   _fees=False,
#                                                   _emergency_tariff=False),
#              transfer_value=None,
#              transfer_value_known=False,
#              transfer_requested=True,
#              age_contribution_relief=AgeContributionRelief(_year=None,
#                                                            _amount=None,
#                                                            _requested=True,
#                                                            _randomize=True),
#              daily_sickness_allowance=DailySicknessAllowance(_from=None,
#                                                              _amount=None,
#                                                              _requested=True,
#                                                              _randomize=True),
#              health_questions=HealthQuestions(medication=False,
#                                               treatment=False,
#                                               allergy=False,
#                                               hospitalization=False,
#                                               psychological=False,
#                                               malignant=False,
#                                               chronic=False,
#                                               hiv=False,
#                                               addictions=False,
#                                               impairments=NewHealthImpairments(hearing_aid=False,
#                                                                                body_implant=False,
#                                                                                prosthetic=False,
#                                                                                infertility=False,
#                                                                                disability=False,
#                                                                                occupational_disability=False,
#                                                                                military_injuries=False,
#                                                                                missing_teeth=False),
#                                               planned=False),
#              insurance_start_date=make_insurance_date(safe=True),
#              request_consultation=True,
#              consultation_requested_date=None,
#              # provide_tax_id="nachreichen",
#              # tax_id=None,
#              # # TODO: Add randomization
#              # tax_id_permission=False,
#              product=User.P_CIVIL_SERVANT_INSURANCE,
#              tariff=User.T_BUSINESS,
#              cost_participation=User.SB_10,
#
#              # will be randomized
#              # health_box=None,
#
#              account_created=False,
#              last_signup_stage_completed=0,
#              signup_completed=False,
#              consultation_completed=False,
#              underwriting_completed=False,
#              offer_accepted=False,
#              expected_rejection=False,
#              signup_rejected=False)
#     return u
#
#
# def comprehensive_user(number_string: str) -> User:
#     letter_string = ""
#     for c in number_string:
#         letter_string += chr(ord('A') + int(c))
#     _forename, _lastname, _email = generate_user_name_from_number(number_string, "bc+AUTO-comprehensive-")
#     u = User(forename=_forename,
#              lastname=_lastname,
#              title=None,
#
#              mobile=telephone,
#              email=_email,
#              address=Address(postal_code="85748",
#                              city="Garching b München",
#                              street="Schrödingerweg",
#                              nr="2"),
#
#              date_of_birth=date(year=1987, month=4, day=29),
#              bmi_parameters=BodyMassIndex(weight=50,
#                                           height=153,
#                                           bmi=21.2,
#                                           mode=BodyMassIndex.M_OK,
#                                           gender=BodyMassIndex.G_FEMALE),
#              nationality=C_DE,
#              occupation=Occupation(_name="Schreibwarenhändler/in",
#                                    _type=Occupation.O_EMPLOYEE,
#                                    _income=215013,
#                                    _randomize=False),
#              civil_servant=None,
#
#              # will be randomized
#              iban=IBAN(iban="DE15998088659753884442"),
#              direct_debit_authorization=True,
#
#              previous_insurance=PreviousInsurance(_type=PreviousInsurance.PKV,
#                                                   # will be randomized (if AKV path taken)
#                                                   _country=None,
#                                                   # will be randomized, or defaulted if AKV
#                                                   _name="INTER Krankenversicherung aG",
#                                                   # will be randomized
#                                                   _date=date(year=1991, month=9, day=5),
#                                                   _state=PreviousInsurance.S_____CANCELLED,
#                                                   _fees=False,
#                                                   _emergency_tariff=False),
#              transfer_value=None,
#              transfer_value_known=False,
#              transfer_requested=True,
#              age_contribution_relief=AgeContributionRelief(_year=None,
#                                                            _amount=None,
#                                                            _requested=True,
#                                                            _randomize=True),
#              daily_sickness_allowance=DailySicknessAllowance(_from=None,
#                                                              _amount=None,
#                                                              _requested=True,
#                                                              _randomize=True),
#              health_questions=HealthQuestions(medication=False,
#                                               treatment=False,
#                                               allergy=False,
#                                               hospitalization=False,
#                                               psychological=False,
#                                               malignant=False,
#                                               chronic=False,
#                                               hiv=False,
#                                               addictions=False,
#                                               impairments=NewHealthImpairments(hearing_aid=False,
#                                                                                body_implant=False,
#                                                                                prosthetic=False,
#                                                                                infertility=False,
#                                                                                disability=False,
#                                                                                occupational_disability=False,
#                                                                                military_injuries=False,
#                                                                                missing_teeth=False),
#                                               planned=False),
#              insurance_start_date=date(year=2018, month=10, day=1),
#              request_consultation=True,
#              # will be set
#              consultation_requested_date=date(year=2018, month=7, day=19),
#              # provide_tax_id="nachreichen",
#              # tax_id=None,
#              # # TODO: Add randomization
#              # tax_id_permission=False,
#              product=User.P_COMPREHENSIVE_INSURANCE,
#              tariff=User.T_BUSINESS,
#              cost_participation=User.SB_10,
#
#              # will be randomized
#              # health_box=None,
#
#              account_created=True,
#              last_signup_stage_completed=4,
#              signup_completed=False,
#              consultation_completed=False,
#              underwriting_completed=False,
#              offer_accepted=False,
#              expected_rejection=False,
#              signup_rejected=False)
#     return u
#
#
# def generate_user_clinic(
#         number_string: str,
#         age: int = None,
#         previous_insurance_type: str = PreviousInsurance.GKV) -> User:
#     letter_string = ""
#     for c in number_string:
#         letter_string += chr(ord('A') + int(c))
#     _bmi_params = BodyMassIndex.generate_weight_height_bmi(mode=BodyMassIndex.M_OK)
#     _forename, _lastname, _email = generate_user_name_from_number(number_string, "bc+AUTO-clinic-")
#     if age is None:
#         _dob = User.generate_dob(safe=True, low=21, high=50)
#     else:
#         _dob = User.generate_dob(safe=True, low=age, high=age + 1)
#     u = User(forename=_forename,
#              lastname=_lastname,
#              title=None,
#
#              mobile=telephone,
#              email=_email,
#              address=Address(postal_code="85748",
#                              city="Garching b München",
#                              street="Schrödingerweg",
#                              nr="2"),
#
#              # if set to None = will be randomized
#              date_of_birth=_dob,
#              bmi_parameters=BodyMassIndex(weight=_bmi_params[0],
#                                           height=_bmi_params[1],
#                                           bmi=_bmi_params[2],
#                                           mode=_bmi_params[3],
#                                           gender=None),
#              nationality=C_DE,
#              occupation=Occupation(_name=None,
#                                    _type=Occupation.O_EMPLOYEE,
#                                    _income=Occupation.generate_income(safe=True),
#                                    _randomize=True),
#              civil_servant=None,
#
#              # will be randomized
#              iban=IBAN(),
#              direct_debit_authorization=True,
#
#              previous_insurance=PreviousInsurance(_type=previous_insurance_type,
#                                                   # will be randomized (if AKV path taken)
#                                                   _country=None,
#                                                   # will be randomized, or defaulted if AKV
#                                                   _name=None,
#                                                   # will be randomized
#                                                   _date=PreviousInsurance.generate_date(date_of_birth=_dob,
#                                                                                         safe=True),
#                                                   _state=PreviousInsurance.S_____CANCELLED,
#                                                   _fees=False,
#                                                   _emergency_tariff=False,
#                                                   _randomize=True),
#              transfer_value=None,
#              transfer_value_known=False,
#              transfer_requested=True,
#              age_contribution_relief=None,
#              daily_sickness_allowance=None,
#              health_questions=HealthQuestions(medication=False,
#                                               treatment=False,
#                                               allergy=False,
#                                               hospitalization=False,
#                                               psychological=False,
#                                               malignant=False,
#                                               chronic=False,
#                                               hiv=False,
#                                               addictions=False,
#                                               impairments=NewHealthImpairments(hearing_aid=False,
#                                                                                body_implant=False,
#                                                                                prosthetic=False,
#                                                                                infertility=False,
#                                                                                disability=False,
#                                                                                occupational_disability=False,
#                                                                                military_injuries=False,
#                                                                                missing_teeth=False),
#                                               planned=False),
#              insurance_start_date=None,
#              request_consultation=True,
#              # will be set
#              consultation_requested_date=None,
#              # provide_tax_id="nachreichen",
#              # tax_id=None,
#              # # TODO: Add randomization
#              # tax_id_permission=False,
#              product=User.P_TOPUP_CLINIC__INSURANCE,
#              tariff=User.T_EINBETT,
#              cost_participation=None,
#
#              # will be randomized
#              # health_box=None,
#
#              account_created=False,
#              last_signup_stage_completed=0,
#              signup_completed=False,
#              consultation_completed=False,
#              underwriting_completed=False,
#              offer_accepted=False,
#              expected_rejection=False,
#              signup_rejected=False)
#     return u
#
#
# def regression_user_clinic() -> User:
#     u = User(forename="Tab1_Passender_Tariff BJADBEBFFJFD V",
#              lastname="Tab1_Passender_Tariff BJADBEBFFJFD N",
#              title=None,
#
#              mobile=telephone,
#              email="bc+auto-clinic-190314155953@on-testing.de",
#              address=Address(postal_code="85748",
#                              city="Garching b München",
#                              street="Schrödingerweg",
#                              nr="2"),
#
#              # if set to None = will be randomized
#              date_of_birth=date(year=1975, month=12, day=16),
#              bmi_parameters=BodyMassIndex(weight=51,
#                                           height=150,
#                                           bmi=22.5,
#                                           mode=BodyMassIndex.M_OK,
#                                           gender=BodyMassIndex.G_MALE),
#              nationality=C_DE,
#              occupation=Occupation(_name="Programmierer/in",
#                                    _type=Occupation.O_EMPLOYEE,
#                                    _income=283063,
#                                    _randomize=False),
#              # will be randomized
#              iban=IBAN(iban="DE95400465386704209669"),
#              direct_debit_authorization=True,
#
#              previous_insurance=PreviousInsurance(_type=PreviousInsurance.GKV,
#                                                   # will be randomized (if AKV path taken)
#                                                   _country=None,
#                                                   # will be randomized, or defaulted if AKV
#                                                   _name="BKK firmus",
#                                                   # will be randomized
#                                                   _date=date(year=1982, month=9, day=21),
#                                                   _state=PreviousInsurance.S_____CANCELLED,
#                                                   _fees=False,
#                                                   _emergency_tariff=False,
#                                                   _randomize=True),
#              transfer_value=None,
#              transfer_value_known=False,
#              transfer_requested=True,
#              civil_servant=None,
#              age_contribution_relief=None,
#              daily_sickness_allowance=None,
#              health_questions=HealthQuestions(medication=False,
#                                               treatment=False,
#                                               allergy=False,
#                                               hospitalization=False,
#                                               psychological=False,
#                                               malignant=False,
#                                               chronic=False,
#                                               hiv=False,
#                                               addictions=False,
#                                               impairments=NewHealthImpairments(hearing_aid=False,
#                                                                                body_implant=False,
#                                                                                prosthetic=False,
#                                                                                infertility=False,
#                                                                                disability=False,
#                                                                                occupational_disability=False,
#                                                                                military_injuries=False,
#                                                                                missing_teeth=False),
#                                               planned=False),
#              insurance_start_date=date(year=2019, month=5, day=1),
#              request_consultation=True,
#              # will be set
#              consultation_requested_date=datetime(year=2019, month=3, day=14, hour=16, minute=2, second=48),
#              # provide_tax_id="nachreichen",
#              # tax_id=None,
#              # # TODO: Add randomization
#              # tax_id_permission=False,
#              product=User.P_TOPUP_CLINIC__INSURANCE,
#              tariff=User.T_EINBETT,
#              cost_participation=None,
#
#              # will be randomized
#              # health_box=None,
#
#              account_created=False,
#              last_signup_stage_completed=5,
#              signup_completed=False,
#              consultation_completed=True,
#              underwriting_completed=True,
#              offer_accepted=False,
#              expected_rejection=False,
#              signup_rejected=False)
#
#     u.consultation_appointment = datetime(year=2019, month=3, day=20, hour=16, minute=0, second=0),
#     return u
#
#     # return generate_user_clinic(number_string=str(190228091728),
#     #                             age=23)
