S = input()

N = len(S)
zero = S.count('0')
one = S.count('1')
print(N - abs(zero - one))
