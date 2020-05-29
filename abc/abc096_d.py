from math import sqrt

N = int(input())


def is_prime(x):
    if x == 2:
        return True
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


ans = []
n = 2
while len(ans) < N:
    if is_prime(n):
        ans.append(n)
    n += 5

print(' '.join(list(map(str, ans))))
