N = int(input())
s = [int(input()) for i in range(N)]
Q = int(input())
k = [int(input()) for i in range(Q)]

s.sort(reverse=True)
for ki in k:
    m = s[N - 1] if ki == N else s[ki] + 1
    print(0 if m == 1 else m)
