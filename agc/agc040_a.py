S = input()

n = len(S)
N = n + 1

l = [0] * N
r = [0] * N
for i in range(1, N):
    if S[i - 1] == '<':
        l[i] = l[i - 1] + 1
for i in range(N - 1, 0, -1):
    if S[i - 1] == '>':
        r[i - 1] = r[i] + 1
print(sum([max(l[i], r[i]) for i in range(N)]))
