N, K = map(int, input().split())
H = list(map(int, input().split()))

if N <= K:
    ans = 0
else:
    H.sort()
    ans = sum(H[:N - K])
print(ans)
