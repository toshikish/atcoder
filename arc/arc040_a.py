N = int(input())
S = [input() for i in range(N)]

r = b = 0
for s in S:
    r += s.count('R')
    b += s.count('B')
print('TAKAHASHI' if r > b else 'AOKI' if r < b else 'DRAW')
