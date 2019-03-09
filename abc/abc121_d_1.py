A, B = map(int, input().split())

def calcXorSum(a):
    if a % 2 == 1:
        n_ones = int((a + 1) / 2)
        return n_ones % 2
    else:
        n_ones = int(a / 2)
        return n_ones % 2 ^ a

print(calcXorSum(B) ^ calcXorSum(A - 1))
