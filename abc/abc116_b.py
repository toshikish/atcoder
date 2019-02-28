s = int(input())

def f(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1

a = [s]
i = 2
ai = s
while True:
    ai = f(ai)
    if ai in a:
        break
    a.append(ai)
    i += 1
print(i)