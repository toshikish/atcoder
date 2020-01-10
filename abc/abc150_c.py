from itertools import permutations

N = int(input())
P = input().replace(' ', '')
Q = input().replace(' ', '')

index = {}
i = 0
for l in permutations(list(map(str, range(1, N + 1)))):
    i += 1
    index[''.join(l)] = i
print(abs(index[P] - index[Q]))
