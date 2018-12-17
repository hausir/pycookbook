# -*- coding: utf-8 -*-

p = (4, 5)
x, y = p
print(x)
print(y)


data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)


name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)


p = (4, 5)
try:
    x, y, z = p
except ValueError as e:
    print(e)


s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(e)


data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)
