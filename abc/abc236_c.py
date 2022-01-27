N, M = map(int, input().split())
S = input().split()
T = input().split()

j = 0
for i in range(N):
    if j < M and S[i] == T[j]:
        print('Yes')
        j += 1
    else:
        print('No')
