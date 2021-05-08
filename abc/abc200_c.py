from collections import Counter

N = int(input())
A = list(map(int, input().split()))

R = [Ai % 200 for Ai in A]
C = Counter(R)
ans = sum([v * (v - 1) // 2 if v > 0 else 0 for v in C.values()])
print(ans)
