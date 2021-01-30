import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())
P = [list(map(int, input().split())) for i in range(N)]
M = int(input())
ops = [list(map(int, input().split())) for i in range(M)]
Q = int(input())
queries = [tuple(map(int, input().split())) for i in range(Q)]

cum_op = [(1, 0, 0, 0, 1, 0)]
for op in ops:
    a, b, c, d, e, f = cum_op[-1]
    if op[0] == 1:
        op_matrix = (d, e, f, -a, -b, -c)
    elif op[0] == 2:
        op_matrix = (-d, -e, -f, a, b, c)
    elif op[0] == 3:
        op_matrix = (-a, -b, -c + 2 * op[1], d, e, f)
    elif op[0] == 4:
        op_matrix = (a, b, c, -d, -e, -f + 2 * op[1])
    cum_op.append(op_matrix)

for Ai, Bi in queries:
    x, y = P[Bi - 1]
    a, b, c, d, e, f = cum_op[Ai]
    print(a * x + b * y + c, d * x + e * y + f)
