import bisect
A, B, Q = map(int, input().split())
INF = 10 ** 18
s = [-INF] + [int(input()) for i in range(A)] + [INF]
t = [-INF] + [int(input()) for i in range(B)] + [INF]
x = [int(input()) for i in range(Q)]

for xi in x:
    b, d = bisect.bisect_right(s, xi), bisect.bisect_right(t, xi)
    min_d = INF
    for S in [s[b - 1], s[b]]:
        for T in [t[d - 1], t[d]]:
            d1 = abs(S - xi) + abs(T - S)
            d2 = abs(T - xi) + abs(S - T)
            min_d = min(min_d, d1, d2)
    print(min_d)
