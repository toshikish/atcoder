N = int(input())

n = len(str(N))
m = (n - 1) // 3
if m == 0:
    ans = 0
else:
    ans = m * (N - 10 ** (3 * m) + 1) \
        + sum([(i - 1) * (10 ** (3 * i) - 10 ** (3 * (i - 1)))
               for i in range(1, m + 1)])
print(ans)
