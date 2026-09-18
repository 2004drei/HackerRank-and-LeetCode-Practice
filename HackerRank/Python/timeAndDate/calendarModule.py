import calendar

dayName = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 1:'SUNDAY',}

month, day, year = map(int, input().split())

if calendar.isleap(year):
  print(dayName[calendar.weekday(year, month, day)])