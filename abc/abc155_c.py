from collections import Counter

N = int(input())
S = [input() for i in range(N)]

c = Counter(S)
mc = c.most_common()
L = []
for p in mc:
    if p[1] < mc[0][1]:
        break
    L.append(p[0])
L.sort()
for l in L:
    print(l)
