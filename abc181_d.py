from collections import Counter
from itertools import permutations

S = input()

ans = False
if len(S) <= 3:
    for p in permutations(S, len(S)):
        if int(''.join(p)) % 8 == 0:
            ans = True
            break
else:
    C = Counter(S)
    n = 104
    while n < 1000:
        sn = str(n)
        if '0' in sn:
            n += 8
            continue
        c = Counter(sn)
        if all([C[k] >= v for k, v in c.items()]):
            ans = True
            break
        n += 8

print('Yes' if ans else 'No')
