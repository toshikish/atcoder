N = int(input())
B = list(map(int, input().split()))

C = [B[0]] + B + [B[N - 2]]
print(sum([min(C[i], C[i + 1]) for i in range(N)]))
