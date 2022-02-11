N = int(input())
A = list(map(int, input().split()))

cut = set()
cut.add(0)
t = 0
for Ai in A:
    t += Ai
    t %= 360
    cut.add(t)

B = sorted(list(cut)) + [360]
print(max(B[i + 1] - B[i] for i in range(N + 1)))
