import math

N = int(input())

ans = N - 1
for i in range(2, int(math.sqrt(N)) + 1):
    q = N // i
    if i * q == N:
        ans = min(ans, i + q - 2)
print(ans)
