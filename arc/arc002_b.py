from datetime import date, timedelta

Y, M, D = map(int, input().split('/'))
d = date(Y, M, D)
while d.year % (d.month * d.day) != 0:
    d += timedelta(days=1)
print(d.strftime('%Y/%m/%d'))
