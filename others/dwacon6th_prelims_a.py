N = int(input())
S = []
T = []
for i in range(N):
    si, ti = tuple(input().split())
    S.append(si)
    T.append(int(ti))
X = input()

i = S.index(X)
print(sum(T[i + 1:]))
