X, Y = map(int, input().split())

a = X
ans = 0
while a <= Y:
    ans += 1
    a *= 2
print(ans)
