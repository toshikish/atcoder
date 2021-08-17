from itertools import accumulate

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

aS = list(accumulate(S[::-1]))
t = min([aS[N - i - 1] + T[i]
         for i in range(1, N)]) if N > 1 else T[-1] + S[-1]
for i in range(N):
    t = min(t, T[i])
    print(t)
    t += S[i]
