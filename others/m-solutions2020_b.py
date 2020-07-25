A, B, C = map(int, input().split())
K = int(input())

k = 0
while A >= B:
    B *= 2
    k += 1
while B >= C:
    C *= 2
    k += 1
print('Yes' if k <= K else 'No')
