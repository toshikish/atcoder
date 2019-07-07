N = int(input())
A = list(map(int, input().split()))
double_X = [0] * N

double_X_0 = 0
for i in range(N):
    if i % 2 == 0:
        double_X_0 += A[i]
    else:
        double_X_0 -= A[i]
double_X[0] = double_X_0
for i in range(1, N):
    double_X[i] = A[i - 1] * 2 - double_X[i - 1]
print(' '.join(map(str, double_X)))
