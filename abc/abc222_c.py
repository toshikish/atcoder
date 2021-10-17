N, M = map(int, input().split())
A = [input() for _ in range(2 * N)]

T = {'G': 0, 'C': 1, 'P': 2}


def judge(a, b):
    if a == b:
        return -1
    if (T[a] - T[b]) % 3 == 2:
        return 0
    else:
        return 1


S = [(0, i) for i in range(2 * N)]
for i in range(M):
    nS = []
    for k in range(N):
        S0, S1 = S[2 * k], S[2 * k + 1]
        j = judge(A[S0[1]][i], A[S1[1]][i])
        if j == 0:
            nS.append((S0[0] - 1, S0[1]))
            nS.append(S1)
        elif j == 1:
            nS.append(S0)
            nS.append((S1[0] - 1, S1[1]))
        else:
            nS.append(S0)
            nS.append(S1)
    nS.sort()
    S = nS

for Si in S:
    print(Si[1] + 1)
