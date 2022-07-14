import datetime as d

s = d.datetime.now() + d.timedelta(hours=9)

print(s.year)
print('{0:02d}'.format(s.month))
print('{0:02d}'.format(s.day))

