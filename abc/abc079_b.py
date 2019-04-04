N = int(input())

d_l = {0: 2, 1: 1}
def l(n):
    if n in d_l:
        return d_l[n]
    d_l[n] = l(n - 2) + l(n - 1)
    return d_l[n]

print(l(N))
