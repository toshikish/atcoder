from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
for i in range(N):
    print(c[i + 1])
