y = int(input())
m = int(input())
d = int(input())

if m == 1 or m == 2:
    y, m = y - 1, m + 12


def days(Y, M, D):
    return 365 * Y + Y // 4 - Y // 100 + Y // 400 + 306 * (M + 1) // 10 + D - 429


print(days(2014, 5, 17) - days(y, m, d))
