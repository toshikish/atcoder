from itertools import combinations

N = int(input())
L = list(map(int, input().split()))

ans = 0
for i, j, k in combinations(range(N), 3):
    Li, Lj, Lk = sorted([L[i], L[j], L[k]])
    if Li != Lj and Lj != Lk and Lk != Li and Li + Lj > Lk:
        ans += 1

print(ans)
