from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
ans = N * (N - 1) // 2
ans -= sum([k * (k - 1) // 2 for k in c.values() if k >= 2])
print(ans)
