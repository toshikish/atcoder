N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ans = 0
for i in range(N):
    if i == N - 1:
        if a[i] == x:
            ans += 1
    else:
        if a[i] <= x:
            x -= a[i]
            ans += 1
        else:
            break
print(ans)
