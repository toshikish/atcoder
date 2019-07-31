import math

N = int(input())
R = [int(input()) for i in range(N)]

R.sort(reverse=True)
sq = 0
for i in range(N):
    sq += R[i] * R[i] * (-1) ** (i % 2)
print(sq * math.pi)
