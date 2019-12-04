N, K = map(int, input().split())
t = [int(input()) for i in range(N)]

ans = -1
for i in range(2, N):
    if sum(t[i - 2:i + 1]) < K:
        ans = i + 1
        break
print(ans)
