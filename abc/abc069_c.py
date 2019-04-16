N = int(input())
a = list(map(int, input().split()))

n0 = n2 = n4 = 0
for ai in a:
    if ai % 4 == 0:
        n4 += 1
    elif ai % 2 == 0:
        n2 += 1
    else:
        n0 += 1

print('Yes' if n0 <= n4 or n2 == 0 and n0 <= n4 + 1 else 'No')
