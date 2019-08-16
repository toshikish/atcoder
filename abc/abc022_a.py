N, S, T = map(int, input().split())
W = int(input())
ans = 1 if S <= W <= T else 0
for i in range(N - 1):
    A = int(input())
    W += A
    if S <= W <= T:
        ans += 1
print(ans)
