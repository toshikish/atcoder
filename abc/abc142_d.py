import math

A, B = map(int, input().split())

while B > 0:
    A, B = B, A % B
N = A

ans = 1
i = 2
for i in [2] + list(range(3, int(math.sqrt(N)) + 2, 2)):
    if N % i == 0:
        while N % i == 0:
            N //= i
        ans += 1
if N > 1:
    ans += 1
print(ans)
