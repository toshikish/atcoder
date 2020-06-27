N = int(input())

f = [1] + [2] * (N - 1)
ans = 1
for i in range(1, N):
    k = i + 1
    ans += k * f[i]
    for j in range(k * 2 - 1, N, k):
        f[j] += 1
print(ans)
