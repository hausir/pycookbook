# -*- coding: utf-8 -*-

record = '....................100.......513.25..........'
cost = int(record[20:22]) * float(record[30:36])
print(cost)


SHARES = slice(20, 22)
PRICE = slice(30, 36)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)


items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])

items[a] = [10, 11]
print(items)
del items[a]
print(items)


a = slice(10, 50, 2)
print(a.start)
print(a.stop)
print(a.step)
