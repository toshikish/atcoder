K = int(input())
A, B = map(int, input().split())
print('OK' if A // K < B // K or (A % K) * (B % K) == 0 else 'NG')
