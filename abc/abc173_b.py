from collections import Counter

N = int(input())
S = [input() for i in range(N)]

c = Counter(S)
for i in ['AC', 'WA', 'TLE', 'RE']:
    print('{} x {}'.format(i, c[i]))
