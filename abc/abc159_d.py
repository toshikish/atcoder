from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
S = sum([n * (n - 1) // 2 for n in c.values()])
for i in range(N):
    print(S - (c[A[i]] - 1))
