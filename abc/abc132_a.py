from collections import defaultdict

S = input()

d = defaultdict(int)
for i in range(4):
    d[S[i]] += 1
print('Yes' if set(d.values()) == set([2, 2]) else 'No')
