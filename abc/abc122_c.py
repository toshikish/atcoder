N, Q = map(int, input().split())
S = input()

c = [0]
for j in range(1, N):
    if S[j - 1] == 'A' and S[j] == 'C':
        c.append(c[-1] + 1)
    else:
        c.append(c[-1])

# 0 1 1 1 2 2 3
# A C A A C A C
# 1 2 3 4 5 6 7
for i in range(Q):
    l, r = map(int, input().split())
    print(c[r - 1] - c[l - 1])
