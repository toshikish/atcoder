from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))

c = defaultdict(int)
for ai in a:
    c[ai] += 1

m = 0
for n in c.keys():
    sum_c = c[n]
    if n - 1 in c: sum_c += c[n - 1]
    if n + 1 in c: sum_c += c[n + 1]
    m = max(m, sum_c)
print(m)
