N = int(input())

if N == 1:
    is_prime = False
else:
    is_prime = True
    i = 2
    while i * i <= N:
        if N % i == 0:
            is_prime = False
            break
        i += 1

if N != 1 and not is_prime and N % 10 % 2 != 0 and N % 10 != 5:
    sum_of_digits = 0
    while N > 0:
        sum_of_digits += N % 10
        N //= 10
    if sum_of_digits % 3 != 0:
        is_prime = True

print('Prime' if is_prime else 'Not Prime')
