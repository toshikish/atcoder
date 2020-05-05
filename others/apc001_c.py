import sys

N = int(input())

S = [''] * N


def query(i):
    print(i)
    s = input()
    if s == 'Vacant':
        print(i)
        sys.exit()
    S[i] = s
    return s


query(0)
query(N - 1)
l = 0
r = N - 1
while r - l >= 2:
    m = (l + r) // 2
    if r - l == 2 and S[l] != S[r]:
        break
    query(m)
    if (m - l) % 2 == 0 and S[l] != S[m] or (m - l) % 2 == 1 and S[l] == S[m]:
        r = m
    else:
        l = m

for i in range(l, r + 1):
    if S[i] == '':
        print(i)
        break
