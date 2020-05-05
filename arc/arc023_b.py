R, C, D = map(int, input().split())
A = [list(map(int, input().split())) for i in range(R)]

ans = 0
for i in range(min(R, D)):
    ans = max(ans, max(A[i][(D + i) % 2:min(D - i + 1, C):2], default=0))
print(ans)
