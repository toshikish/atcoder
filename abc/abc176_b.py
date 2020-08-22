N = input()
print('Yes' if sum([int(n) for n in list(N)]) % 9 == 0 else 'No')
