N = int(input())

def S(n):
    if n % 10 == n:
        return n
    return n % 10 + S(n // 10)

print('Yes' if N % S(N) == 0 else 'No')
