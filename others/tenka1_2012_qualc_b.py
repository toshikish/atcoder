from collections import defaultdict

s = input()

N = len(s)
i = 0
D = defaultdict(list)
T = defaultdict(list)
ans = ''
while i < N:
    m = s[i]
    n = '10'
    if s[i + 1] == '1':
        n = '10'
        i += 3
    else:
        n = s[i + 1]
        i += 2
    for M in ['S', 'H', 'D', 'C']:
        if m == M and n in ['10', 'J', 'Q', 'K', 'A']:
            D[M].append(n)
            if len(D[M]) == 5:
                ans = M
                break
        else:
            T[M].append(m + n)
    else:
        continue
    break

if len(T[ans]) == 0:
    print(0)
else:
    print(''.join(T[ans]))
