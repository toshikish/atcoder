K, A, B = map(int, input().rstrip().split())

if B - A <= 2 or K <= A:
    print(K + 1)
else:
    print(A + (B - A) * int((K - A + 1) / 2) + (K - A + 1) % 2)