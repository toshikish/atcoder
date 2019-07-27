N = int(input())
p = list(map(int, input().split()))

c = 0
for i in range(N):
    if p[i] != i + 1:
        c += 1
print('YES' if c == 2 or c == 0 else 'NO')
