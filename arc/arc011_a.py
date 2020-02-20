m, n, N = map(int, input().split())

n_made = N
n_res = 0
n_material = n_made + n_res
ans = N
while n_material >= m:
    n_made = n_material // m * n
    n_res = n_material % m
    n_material = n_made + n_res
    ans += n_made
print(ans)
