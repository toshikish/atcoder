S = input()

p = 0
T = list('ict')
for s in S:
    if s.lower() == T[p]:
        p += 1
        if p == 3:
            break
print('YES' if p == 3 else 'NO')
