A = int(input())
print('YES' if A in [i * i * i for i in range(1, 101)] else 'NO')
