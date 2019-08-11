D, G = map(int, input().split())
problems = [tuple(map(int, input().split())) for i in range(D)]

ans = 1000
for i in range(1 << D):
    S = G
    P = 0
    max_j = 0
    for j in range(D):
        if i >> j & 1 == 1:
            P += problems[j][0]
            S -= 100 * (j + 1) * problems[j][0] + problems[j][1]
        else:
            max_j = j
    if S > 0:
        p = 100 * (max_j + 1)
        need = (S + p - 1) // p
        if need >= problems[max_j][0]:
            continue
        P += need
    ans = min(P, ans)
print(ans)
