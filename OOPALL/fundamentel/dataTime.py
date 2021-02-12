import datetime

current_date = datetime.datetime.now()
print(current_date)

today = datetime.date.today()
print(today)

t = current_date.strftime('%m/%d/%Y %H:%M:%S')
print(t)

da = '21 June 2020'
d = datetime.datetime.strptime(da,'%d %B %Y')

print(d)

de = datetime.date(2020,9,21)

print(de)
