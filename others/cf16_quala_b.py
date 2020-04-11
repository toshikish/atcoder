N = int(input())
a = list(map(lambda s: int(s) - 1, input().split()))

ans = 0
for i in range(N):
    if a[a[i]] == i:
        ans += 1
print(ans // 2)
