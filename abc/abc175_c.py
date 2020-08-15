X, K, D = map(int, input().split())

aX = abs(X)
if aX >= K * D:
    ans = aX - K * D
else:
    x = aX % D
    k = K - aX // D
    ans = x if k % 2 == 0 else D - x
print(ans)
