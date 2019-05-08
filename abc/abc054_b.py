N, M = map(int, input().split())
A = [input() for i in range(N)]
B = [input() for i in range(M)]

includes = False
for r in range(N - M + 1):
    for c in range(N - M + 1):
        for i in range(M):
            for j in range(M):
                if A[r + i][c + j] != B[i][j]:
                    break
            else:
                continue
            break
        else:
            includes = True

print('Yes' if includes else 'No')
