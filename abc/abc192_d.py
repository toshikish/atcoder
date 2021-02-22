X = input()
M = int(input())

l = len(X)
d = int(sorted(X)[-1])


def Base_n_to_10(n):
    return sum([int(X[l - 1 - i]) * n ** i for i in range(l)])


if l == 1:
    ans = 1 if d <= M else 0
else:
    n = int((M / int(X[0])) ** (1 / (l - 1)))
    while Base_n_to_10(n) > M:
        n -= 1
    ans = max(n - d, 0)
print(ans)
