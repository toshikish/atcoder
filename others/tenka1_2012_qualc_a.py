n = int(input())

prime = [True] * 10001
prime[1] = False
ans = 0
i = 2
while i < n:
    if prime[i]:
        ans += 1
    for j in range(i * 2, 10001, i):
        prime[j] = False
    i += 1
print(ans)
