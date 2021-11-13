N, K = map(int, input().split())
A = list(map(int, input().split()))

low = 1
high = 200_000_000_000_000_001
mid = (high + low) // 2
while high - low > 1:
    S = sum(min(Ai, mid) for Ai in A)
    if S >= mid * K:
        low = mid
    else:
        high = mid
    mid = (high + low) // 2
print(mid)
