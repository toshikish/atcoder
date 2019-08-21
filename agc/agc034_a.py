N, A, B, C, D = map(int, input().split())
A -= 1
B -= 1
C -= 1
D -= 1
S = input()

c = [1 if S[0] == '#' else -1]
for i in range(1, N):
    if c[-1] > 0:
        if S[i] == '#':
            c.append(c[-1] + 1)
        else:
            c.append(-1)
    else:
        if S[i] == '#':
            c.append(1)
        else:
            c.append(c[-1] - 1)

if A < B < C < D:
    ans = max(c[A:D + 1]) <= 1
elif A < B < D < C:
    ans = max(c[A:C + 1]) <= 1 and min(c[B + 1:D + 2]) <= -3
elif A < C < B < D:
    ans = max(c[A:C + 1]) <= 1 and max(c[B:D + 1]) <= 1
print('Yes' if ans else 'No')
