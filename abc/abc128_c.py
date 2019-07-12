N, M = map(int, input().split())
ks = [list(map(int, input().split())) for i in range(M)]
p = list(map(int, input().split()))

ans = 0
for i in range(1 << N):
    all_on = True
    for j in range(M):
        n_on = 0
        for s in ks[j][1:]:
            if (i >> (s - 1)) & 1:
                n_on += 1
        if n_on % 2 != p[j]:
            all_on = False
    if all_on:
        ans += 1
print(ans)
