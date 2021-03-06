from collections import defaultdict

N = int(input())
A = []
B = []
revA = defaultdict(list)
revB = defaultdict(list)
for i in range(N):
    Ai, Bi = map(int, input().split())
    A.append(Ai)
    B.append(Bi)
    revA[Ai].append(i)
    revB[Bi].append(i)

A.sort()
B.sort()
if len(revA[A[0]]) == len(revB[B[0]]) == 1 and revA[A[0]][0] == revB[B[0]][0]:
    ans = min(A[0] + B[0], max(A[0], B[1]), max(A[1], B[0]))
else:
    ans = max(A[0], B[0])
print(ans)
