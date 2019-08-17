from collections import Counter

N = int(input())
a = list(map(int, input().split()))

c = Counter(a)
k = list(c.keys())
v = list(c.values())
if k == [0]:
    able = True
elif len(c) == 2 and 0 in c and c[0] == N // 3:
    able = True
elif len(c) == 3 and k[0] ^ k[1] == k[2] and v[0] == v[1] == v[2]:
    able = True
else:
    able = False
print('Yes' if able else 'No')
