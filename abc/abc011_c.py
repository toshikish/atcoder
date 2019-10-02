N = int(input())
ng = [int(input()) for i in range(3)]

achievable = True
c = 0
while N > 0:
    if N in ng:
        achievable = False
        break
    for i in range(3, 0, -1):
        if N - i not in ng:
            N -= i
            break
    else:
        achievable = False
        break
    c += 1
    continue
print('YES' if achievable and c <= 100 else 'NO')
