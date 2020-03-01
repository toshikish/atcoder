A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
b = [int(input()) for i in range(N)]

C = [[False] * 3 for i in range(3)]
for bi in b:
    for j in range(3):
        for i in range(3):
            if A[j][i] == bi:
                C[j][i] = True

ans = False
for j in range(3):
    if C[j][0] == C[j][1] == C[j][2] == True:
        ans = True
for i in range(3):
    if C[0][i] == C[1][i] == C[2][i] == True:
        ans = True
if C[0][0] == C[1][1] == C[2][2] == True:
    ans = True
if C[0][2] == C[1][1] == C[2][0] == True:
    ans = True
print('Yes' if ans else 'No')
