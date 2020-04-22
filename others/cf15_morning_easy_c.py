N, K, M, R = map(int, input().split())
S = [int(input()) for i in range(N - 1)]

if N == 1:
    ans = R
else:
    S.sort(reverse=True)
    if K == N:
        diff = K * R - sum(S)
        if diff <= 0:
            ans = 0
        elif diff > M:
            ans = -1
        else:
            ans = diff
    else:
        diff = K * R - sum(S[:K - 1])
        if diff - S[K - 1] <= 0:
            ans = 0
        elif diff > M:
            ans = -1
        else:
            ans = diff

print(ans)
