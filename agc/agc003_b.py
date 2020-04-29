N = int(input())
A = [int(input()) for i in range(N)]

ans = 0
t = 0
for i in range(N):
    if A[i] == 0:
        ans += t // 2
        t = 0
    else:
        t += A[i]
ans += t // 2
print(ans)
