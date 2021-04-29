N = int(input())
S = list(input())
Q = int(input())

flipped = False
for _ in range(Q):
    Ti, Ai, Bi = map(lambda s: int(s) - 1, input().split())
    if Ti == 0:
        if flipped:
            Ai = (Ai + N) % (2 * N)
            Bi = (Bi + N) % (2 * N)
        S[Ai], S[Bi] = S[Bi], S[Ai]
    else:
        flipped = not flipped

if flipped:
    s0, s1, s2, s3 = N, 2 * N, 0, N
else:
    s0, s1, s2, s3 = 0, N, N, 2 * N
print(''.join(S[s0:s1] + S[s2:s3]))
