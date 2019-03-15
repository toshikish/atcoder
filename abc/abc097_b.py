X = int(input())

expos = {1}
for i in range(2, 40):
    e = i ** 2
    while e <= 1000:
        expos.add(e)
        e *= i
print(max(filter(lambda x: x <= X, sorted(expos))))
