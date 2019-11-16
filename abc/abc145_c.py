import math

N = int(input())
T = [tuple(map(int, input().split())) for i in range(N)]

S = 0
for i in range(N - 1):
    for j in range(i, N):
        S += math.sqrt((T[i][0] - T[j][0]) ** 2 + (T[i][1] - T[j][1]) ** 2)
print(S * 2 / N)
