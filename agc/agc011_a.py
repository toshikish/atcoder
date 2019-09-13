N, C, K = map(int, input().split())
T = [int(input()) for i in range(N)]

T.sort(reverse=True)
ans = 0
while T:
    t = T.pop()
    ans += 1
    for i in range(C - 1):
        if not T or T[-1] > t + K:
            break
        T.pop()
print(ans)
