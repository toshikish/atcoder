N, K = map(int, input().split())
s = [int(input()) for i in range(N)]

if 0 in s:
    ans = N
else:
    ans = 0
    r = 0
    p = 1
    for l in range(N):
        while r < N and p * s[r] <= K:
            p *= s[r]
            r += 1
        ans = max(ans, r - l)
        if l < r:
            p //= s[l]
        else:
            r += 1
print(ans)
