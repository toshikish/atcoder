L, H = map(int, input().split())
N = int(input())
A = [int(input()) for i in range(N)]

for Ai in A:
    if Ai < L:
        ans = L - Ai
    elif Ai <= H:
        ans = 0
    else:
        ans = -1
    print(ans)
