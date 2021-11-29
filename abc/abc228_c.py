N, K = map(int, input().split())
P = [(sum(list(map(int, input().split()))), i) for i in range(N)]

P.sort(reverse=True)
border = P[K - 1][0]
ans = [False] * N
for score, i in P:
    if score + 300 >= border:
        ans[i] = True

for i in range(N):
    print('Yes' if ans[i] else 'No')
