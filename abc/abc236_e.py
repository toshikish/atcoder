N = int(input())
A = list(map(int, input().split()))

low = 0
high = 1_000_000_001
while high - low > 0.001:
    mid = (high + low) / 2
    B = [Ai - mid for Ai in A]
    dp0 = 0
    dp1 = B[0]
    for i in range(1, N):
        dp0, dp1 = dp1, max(dp0, dp1) + B[i]
    if max(dp0, dp1) >= 0:
        low = mid
    else:
        high = mid
print(low)

low = 0
high = 1_000_000_001
while high - low > 1:
    mid = (high + low) // 2
    B = [1 if Ai >= mid else -1 for Ai in A]
    dp0 = 0
    dp1 = B[0]
    for i in range(1, N):
        dp0, dp1 = dp1, max(dp0, dp1) + B[i]
    if max(dp0, dp1) > 0:
        low = mid
    else:
        high = mid
print(low)
