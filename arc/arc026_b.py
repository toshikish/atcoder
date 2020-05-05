from math import sqrt

N = int(input())

S = 0
for i in range(1, int(sqrt(N)) + 1):
    if N % i == 0:
        S += i
        p = N // i
        if i != 1 and i != p:
            S += p
print('Deficient' if N == 1 or S < N else 'Abundant' if S > N else 'Perfect')
