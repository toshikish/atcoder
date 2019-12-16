N, A, B = map(int, input().split())

N %= A + B
print('Ant' if 0 < N <= A else 'Bug')
