from math import gcd

N, M = map(int, input().split())
S = input()
T = input()

G = gcd(N, M)
L = N * M // G
n = N // G
m = M // G

ans = True
for k in range(G):
    if S[k * n] != T[k * m]:
        ans = False
        break
print(L if ans else -1)
