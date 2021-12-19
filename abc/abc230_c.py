N, A, B = map(lambda s: int(s) - 1, input().split())
P, Q, R, S = map(lambda s: int(s) - 1, input().split())

s = A + B
d = A - B
for i in range(P, Q + 1):
    line = ['#' if i + j == s or i - j == d else '.' for j in range(R, S + 1)]
    print(''.join(line))
