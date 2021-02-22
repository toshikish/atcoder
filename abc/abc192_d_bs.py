X = input()
M = int(input())

l = len(X)
d = int(sorted(X)[-1])


def Base_n_to_10(n):
    return sum([int(X[l - 1 - i]) * n ** i for i in range(l)])


if l == 1:
    ans = 1 if d <= M else 0
else:
    low = d
    high = M + 1
    while high - low > 1:
        mid = (low + high) // 2
        if Base_n_to_10(mid) <= M:
            low = mid
        else:
            high = mid
    ans = max(low - d, 0)
print(ans)
