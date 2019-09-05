import bisect

S = input()

N = len(S)
if S == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
elif N < 26:
    t = [False] * 26
    for i in range(N):
        t[ord(S[i]) - 97] = True
    print(S + chr(t.index(False) + 97))
else:
    t = [S[-1]]
    for i in range(N - 2, -1, -1):
        if S[i] < S[i + 1]:
            break
        bisect.insort_left(t, S[i])
    print(S[:i] + t[bisect.bisect_left(t, S[i])])
