from itertools import permutations

N, M, L = map(int, input().split())
C = list(map(int, input().split()))

print(max([(N // c[0]) * (M // c[1]) * (L // c[2])
           for c in permutations(C, 3)]))
