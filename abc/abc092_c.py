N = int(input())
A = [0] + list(map(int, input().split())) + [0]

total = 0
for i in range(N + 1):
    total += abs(A[i + 1] - A[i])

for i in range(1, N + 1):
    if A[i - 1] <= A[i] <= A[i + 1] or A[i + 1] <= A[i] <= A[i - 1]:
        print(total)
    else:
        print(total - min(abs(A[i] - A[i - 1]), abs(A[i] - A[i + 1])) * 2)
