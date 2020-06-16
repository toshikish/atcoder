from collections import Counter

A = input()

c = Counter(A)
N = len(A)
ans = N * (N - 1) // 2 + 1
for i in c.values():
    ans -= i * (i - 1) // 2
print(ans)
