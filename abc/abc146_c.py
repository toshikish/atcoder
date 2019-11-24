A, B, X = map(int, input().split())

d = 1
N = 1
while A * N + B * d <= X:
    d += 1
    N *= 10

d -= 1
if d == 0:
    ans = 0
else:
    ans = min((X - B * d) // A, 10 ** d - 1, 10 ** 9)
print(ans)
