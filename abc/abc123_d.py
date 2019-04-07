X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
ABC = []
for a in range(X):
    for b in range(Y):
        if (a + 1) * (b + 1) > K: break
        for c in range(Z):
            if (a + 1) * (b + 1) * (c + 1) > K: break
            ABC.append(A[a] + B[b] + C[c])
ABC.sort(reverse=True)
for i in range(K):
    print(ABC[i])
