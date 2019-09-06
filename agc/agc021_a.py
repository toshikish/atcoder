N = list(map(int, list(input())))

n = len(N)
if n == 1:
    ans = N[0]
else:
    ans = sum(N) if min(N[1:]) == 9 else N[0] - 1 + 9 * (n - 1)
print(ans)
