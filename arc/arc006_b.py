N, L = map(int, input().split())
F = [input() for i in range(L)]
p = input().find('o')

for i in range(L - 1, -1, -1):
    if p > 0 and F[i][p - 1] == '-':
        p -= 2
    elif p < 2 * N - 2 and F[i][p + 1] == '-':
        p += 2
print(p // 2 + 1)
