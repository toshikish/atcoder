from collections import Counter

N = int(input())
S = [input() for i in range(N)]

c = Counter(S)
print(c.most_common()[0][0])
