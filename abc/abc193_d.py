K = int(input())
S = list(map(int, list(input()[:4])))
T = list(map(int, list(input()[:4])))


def calc(deck):
    return sum([(i + 1) * (10 ** deck[i]) for i in range(9)])


field = [K] * 9
deck_t = [0] * 9
for i in S:
    deck_t[i - 1] += 1
    field[i - 1] -= 1
deck_a = [0] * 9
for i in T:
    deck_a[i - 1] += 1
    field[i - 1] -= 1

ans = 0
for i in range(9):
    if field[i] == 0:
        continue
    t = 0
    field[i] -= 1
    deck_a[i] += 1
    score_a = calc(deck_a)
    for j in range(9):
        if field[j] == 0:
            continue
        deck_t[j] += 1
        if calc(deck_t) > score_a:
            t += field[j]
        deck_t[j] -= 1
    field[i] += 1
    deck_a[i] -= 1
    ans += t * field[i]

print(ans / ((9 * K - 8) * (9 * K - 9)))
