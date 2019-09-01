N = int(input())
H = list(map(int, input().split()))

c = 0
ans = 0
for i in range(N - 1):
    if H[i] >= H[i + 1]:
        c += 1
        ans = max(ans, c)
    else:
        c = 0
print(ans)
