from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

ans = 0
X = defaultdict(int)
for i in range(1, N):
    X[i + A[i - 1]] += 1
    ans += X[i + 1 - A[i]]
print(ans)
