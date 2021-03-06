from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
ans = 0
for i in range(-200, 200):
    for j in range(i + 1, 201):
        ans += c[i] * c[j] * (i - j) * (i - j)
print(ans)
