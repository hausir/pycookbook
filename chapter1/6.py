# -*- coding: utf-8 -*-

from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)


d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)


d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)


pairs = [
    ('a', 1),
    ('b', 2),
    ('c', 3),
    ('b', 4),
    ('a', 5),
]
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)


d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)
