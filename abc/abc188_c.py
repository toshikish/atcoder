N = int(input())
A = list(map(int, input().split()))

B = [(A[i], i + 1) for i in range(2 ** N)]
for i in range(N - 1):
    C = []
    for j in range(2 ** (N - i - 1)):
        C.append(max(B[2 * j], B[2 * j + 1]))
    B = C

print(sorted(B)[0][1])
