N = int(input())

L = []
cards = list(map(str, range(1, 7)))
L.append(''.join(cards))
for i in range(29):
    cards[i % 5], cards[i % 5 + 1] = cards[i % 5 + 1], cards[i % 5]
    L.append(''.join(cards))
print(L[N % 30])
