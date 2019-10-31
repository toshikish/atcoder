N, M = map(int, input().split())

red = [True] + [False] * (N - 1)
total = [1] * N
ans = 1
for i in range(M):
    xi, yi = map(int, input().split())
    if red[xi - 1]:
        red[yi - 1] = True
    total[xi - 1] -= 1
    total[yi - 1] += 1
    if total[xi - 1] == 0:
        red[xi - 1] = False
print(red.count(True))
