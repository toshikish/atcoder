N, M = map(int, input().split())
C = [0] * N
for i in range(M):
    ai, bi = map(int, input().split())
    C[ai - 1] += 1
    C[bi - 1] += 1

print('YES' if len(list(filter(lambda i: i % 2 == 1, C))) == 0 else 'NO')
