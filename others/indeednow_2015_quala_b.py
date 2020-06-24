from collections import Counter

N = int(input())
S = [input() for i in range(N)]

c = Counter('indeednow')
for Si in S:
    ci = Counter(Si)
    print('YES' if ci == c else 'NO')
