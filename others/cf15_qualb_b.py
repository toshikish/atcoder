from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))

c = Counter(A)
mc = c.most_common(1)[0]
print(mc[0] if mc[1] > N // 2 else '?')
