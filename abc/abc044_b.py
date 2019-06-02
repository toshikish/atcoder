from collections import defaultdict

w = input()
d = defaultdict(int)
for l in w:
    d[l] += 1
ans = True
for n in d.values():
    if n % 2 == 1:
        ans = False
print('Yes' if ans else 'No')
