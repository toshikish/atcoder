H = int(input())


def attack(x):
    if x == 1:
        return 1
    return 1 + attack(x // 2) * 2


print(attack(H))
