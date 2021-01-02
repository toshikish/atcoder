from itertools import combinations

N = int(input())
P = [tuple(map(int, input().split())) for i in range(N)]

ans = 0
for i, j in combinations(range(N), 2):
    if -1 <= (P[j][1] - P[i][1]) / (P[j][0] - P[i][0]) <= 1:
        ans += 1

print(ans)
