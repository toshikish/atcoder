A, B, C = map(int, input().split())

if A % 2 * B % 2 * C % 2 == 0:
    ans = 0
else:
    ans = min(A * B, B * C, C * A)
print(ans)
