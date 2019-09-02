N = int(input())
a = list(map(int, input().split()))

ans = 0
c = 1
for i in range(1, N):
    if a[i] == a[i - 1]:
        c += 1
    else:
        ans += c // 2
        c = 1
ans += c // 2
print(ans)
