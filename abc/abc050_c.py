from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

c = defaultdict(int)
for a in A:
    c[a] += 1

if N % 2 == 0:
    probable = True
    for i in range(1, N, 2):
        if c[i] != 2:
            probable = False
    ans = 2 ** (N // 2) % (10 ** 9 + 7) if probable else 0
else:
    probable = True
    if c[0] != 1:
        probable = False
    for i in range(2, N, 2):
        if c[i] != 2:
            probable = False
    ans = 2 ** ((N - 1) // 2) % (10 ** 9 + 7) if probable else 0
print(ans)
