from collections import defaultdict
N, M = map(int, input().split())
cities = []
prefs = defaultdict(list)
for i in range(M):
    city = tuple(map(int, input().split()))
    cities.append(city)
    prefs[city[0]].append(city[1])

for pref in prefs.values():
    pref.sort()
for c in cities:
    x = prefs[c[0]].index(c[1]) + 1
    print('{:06}{:06}'.format(c[0], x))
