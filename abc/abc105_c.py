N = int(input())

res = N
S = ''
divisor = 1
i = 0
while res != 0:
    divisor *= 2
    remainder = abs(res) % divisor
    bit = 0 if remainder == 0 else 1
    S = str(bit) + S
    if i % 2 == 0:
        res -= divisor * bit // 2
    else:
        res += divisor * bit // 2
    i += 1
print(S or '0')
