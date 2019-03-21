from collections import defaultdict
cards = defaultdict(int)
N = int(input())
for i in range(N):
    s = input()
    cards[s] += 1
M = int(input())
for i in range(M):
    t = input()
    cards[t] -= 1

print(max(0, max(list(cards.values()))))
