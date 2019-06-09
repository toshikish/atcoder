import math

n = int(input())

ans = 3 * n
for i in range(1, int(math.sqrt(n)) + 1):
    j = n // i
    ans = min(ans, (j - i) + (n - i * j))
print(ans)
