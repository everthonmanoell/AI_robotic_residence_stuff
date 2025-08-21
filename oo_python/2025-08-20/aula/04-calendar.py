import calendar as cal

cal.setfirstweekday(cal.SUNDAY)
# calendario = cal.TextCalendar()
# print(calendario.formatmonth(2025,8))
print(cal.LocaleTextCalendar(locale = 'pt_BR').formatmonth(2025,8))
print(cal.weekday ( 2038, 12, 25 ) )
print(cal.day_name[ cal.weekday ( 2038, 12, 25 ) ])