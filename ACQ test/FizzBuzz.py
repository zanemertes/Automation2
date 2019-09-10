import datetime


delta = 99
days = 365.25
deltadays = delta*days
print(deltadays)

tday = datetime.date.today()
tdelta = datetime.timedelta(days=deltadays)

finaldate =tday-tdelta
print(finaldate)
print(finaldate.day)

# d = datetime.date(year=2019, month=8, day=5)
#
# year = tyear-99
# d.strftime("%d.%m.%Y")
# '05.08.2019'
#
# day_field.send_keys(31)
# month_field.send_keys(12)
# # Year 0019 - waaaay over a 100 years => we expect a validation error message and Weiter button to REMAIN disabled
# year_field.send_keys(19)






# import math
#
# for i in range(1,101):
#     x = i/3
#     y = i/5
#     fracx, wholex = math.modf(x)
#     fracy, wholey = math.modf(y)
#     if fracx == 0.0 and fracy == 0.0:
#         print('FizzBuzz')
#     elif fracx == 0.0:
#         print('Fizz')
#     elif fracy == 0.0:
#         print('Buzz')
#     else:
#         print(i)


