N = int(input())
h = [int(input()) for i in range(N)]

if N <= 2:
    ans = N
else:
    ans = 2
    t = 2
    for i in range(2, N):
        if h[i - 2] > h[i - 1] and h[i - 1] < h[i]:
            ans = max(ans, t)
            t = 2
        else:
            t += 1
    ans = max(ans, t)
print(ans)
