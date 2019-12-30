N = int(input())

prime = True
i = 2
while i * i <= N:
    if N % i == 0:
        prime = False
        break
    i += 1

print('YES' if prime else 'NO')
