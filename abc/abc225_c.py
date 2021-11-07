N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

ans = M == 1 \
    or all(B[0][j + 1] == B[0][j] + 1 for j in range(M - 1)) and (B[0][0] - 1) % 7 < (B[0][M - 1] - 1) % 7
if ans:
    ans = all(B[i + 1][j] == B[i][j] + 7
              for i in range(N - 1) for j in range(M))
print('Yes' if ans else 'No')
