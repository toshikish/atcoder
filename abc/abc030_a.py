A, B, C, D = map(int, input().split())
t, a = B / A, D / C
print('TAKAHASHI' if t > a else 'AOKI' if t < a else 'DRAW')
