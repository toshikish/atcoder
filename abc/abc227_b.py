N = int(input())
S = list(map(int, input().split()))

A = [False] * 1001
for a in range(1, 150):
    for b in range(1, 150):
        s = 4 * a * b + 3 * a + 3 * b
        if s > 1000:
            break
        A[s] = True

print([A[Si] == False for Si in S].count(True))
