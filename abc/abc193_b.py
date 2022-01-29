N = int(input())
M = 1_000_000_001
ans = M
for _ in range(N):
    Ai, Pi, Xi = map(int, input().split())
    if Xi - Ai > 0:
        ans = min(ans, Pi)

print(ans if ans < M else -1)
