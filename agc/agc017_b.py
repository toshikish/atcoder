N, A, B, C, D = map(int, input().split())

S = B - A
ans = False
for m in range(N):
    n = N - 1 - m
    if C * m - D * n <= S <= D * m - C * n:
        ans = True
print('YES' if ans else 'NO')
