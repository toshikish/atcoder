n = int(input())

s = n * (n + 1) // 2
prime = True if s > 1 else False
i = 2
while i * i <= s:
    if s % i == 0:
        prime = False
        break
    i += 1 if i == 2 else 2
print('WANWAN' if prime else 'BOWWOW')
