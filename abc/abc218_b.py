P = list(map(int, input().split()))
print(''.join(chr(ord('a') + Pi - 1) for Pi in P))
