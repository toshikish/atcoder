from collections import Counter

N = int(input())
r = input()

c = Counter(r)
T = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
print(sum([c[t] * T[t] for t in T]) / N)
