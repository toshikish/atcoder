from collections import Counter

N = input()

c = Counter(N)
n = [0] * 3
for k, v in c.items():
    n[int(k) % 3] += v

if n[0] == 0 and ((n[1] <= 2 and n[2] == 0) or (n[1] == 0 and n[2] <= 2)):
    ans = -1
else:
    res = (n[1] * 1 + n[2] * 2) % 3
    if res == 0:
        ans = 0
    elif res == 1 and n[1] >= 1 or res == 2 and n[2] >= 1:
        ans = 1
    else:
        ans = 2

print(ans)
