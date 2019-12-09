from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

max_A = max(A)
j = 0
while max_A >> j > 0:
    j += 1
max_j = j

ans = 0
MOD = 10 ** 9 + 7
for j in range(max_j):
    c = [0] * 2
    for i in range(N):
        c[A[i] >> j & 1] += 1
    ans += c[0] * c[1] * (1 << j)
    ans %= MOD
print(ans)
