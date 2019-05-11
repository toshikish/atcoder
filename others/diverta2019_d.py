import math

N = int(input())

ans = 0
for Q in range(1, int(math.sqrt(N)) + 2):
    M = N // Q
    if M * Q != N or M - Q < 2:
        continue
    ans += M - 1
print(ans)
