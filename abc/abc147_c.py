from collections import defaultdict

N = int(input())
S = defaultdict(dict)
for i in range(N):
    Ai = int(input())
    for j in range(Ai):
        xi, yi = map(int, input().split())
        S[i][xi - 1] = yi

ans = 0
for i in range(1 << N):
    possible = True
    c = 0
    for j in range(N):
        if i >> j & 1:
            c += 1
            for xi, yi in S[j].items():
                if i >> xi & 1 != yi:
                    possible = False
                    break
    if possible:
        ans = max(ans, c)
print(ans)
