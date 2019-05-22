N, x = map(int, input().split())
a = [0] + list(map(int, input().split()))

ans = 0
for i in range(N):
    if a[i] + a[i + 1] > x:
        tmp = a[i] + a[i + 1] - x
        ans += tmp
        a[i + 1] -= tmp
print(ans)
