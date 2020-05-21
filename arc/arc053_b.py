from collections import Counter

S = input()

c = Counter(S)
o = e = 0
for n in c.values():
    o += n % 2
    e += n - n % 2

if o == 0:
    ans = e
else:
    p = e // 2
    ans = 1 + p // o * 2
print(ans)
