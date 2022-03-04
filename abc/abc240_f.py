T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        xi, yi = map(int, input().split())
        x[i] = xi
        y[i] = yi
    if max(x) <= 0:
        print(x[0])
        continue
    ans = x[0]
    Bi = 0
    Ai = 0
    for i in range(N):
        nBi = Bi + x[i] * y[i]
        nAi = Ai + Bi * y[i] + x[i] * y[i] * (y[i] + 1) // 2
        if x[i] < 0 and Bi > 0:
            n = Bi // -x[i]
            if n < y[i]:
                ans = max(ans, Ai + Bi * n + x[i] * n * (n + 1) // 2)
        ans = max(ans, nAi)
        Bi = nBi
        Ai = nAi
    print(ans)
