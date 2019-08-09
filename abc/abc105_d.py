from collections import defaultdict

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))

B = 0
n = defaultdict(int)
for i in range(N + 1):
    B += A[i]
    B %= M
    n[B] += 1

ans = 0
for ni in n.values():
    ans += ni * (ni - 1) // 2
print(ans)
