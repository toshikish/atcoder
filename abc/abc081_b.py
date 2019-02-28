N = int(input())
A = list(map(int, input().split()))
powers = []
for a in A:
    power = 0
    while a % 2 == 0:
        a /= 2
        power += 1
    powers.append(power)
print(min(powers))