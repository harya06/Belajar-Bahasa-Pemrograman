import datetime as dt

x = dt.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

x = dt.datetime(2020, 5, 17)
print(x)

print(x.strftime("%B"))