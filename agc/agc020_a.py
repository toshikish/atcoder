N, A, B = map(int, input().split())
print('Alice' if (abs(A - B) - 1) % 2 == 1 else 'Borys')
