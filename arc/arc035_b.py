N = int(input())
T = [int(input()) for i in range(N)]
MOD = 1000000007

T.sort()
t = T[0]
p = t
s = 1
c = 1
for i in range(1, N):
    t += T[i]
    p += t
    if T[i] == T[i - 1]:
        c += 1
    else:
        c = 1
    s *= c
    s %= MOD

print(p)
print(s)
