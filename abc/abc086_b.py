N = int(input().replace(' ', ''))

def isSquare(n):
    for i in range(1000):
        if i ** 2 == n:
            return True
    return False

print('Yes' if isSquare(N) else 'No')
