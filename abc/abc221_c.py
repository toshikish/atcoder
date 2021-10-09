N = input()

z = N.count('0')
N = list(N.replace('0', ''))
N.sort(reverse=True)
L = len(N)

ans = 0
for b in range(1, 1 << L - 1):
    n = [0] * 2
    for i in range(L):
        j = b >> i & 1
        n[j] *= 10
        n[j] += int(N[i])
    ans = max(ans, n[0] * n[1])

print(ans * 10 ** z)
