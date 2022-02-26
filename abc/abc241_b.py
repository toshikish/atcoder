from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ca = Counter(A)
cb = Counter(B)
print('Yes' if all(ca[b] >= cb[b] for b in cb.keys()) else 'No')
