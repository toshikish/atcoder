N = int(input())
A = list(map(int, input().rstrip().split()))

def gcd(X):
    if len(X) == 1:
        return X[0]
    X.sort()
    residue = set(map(lambda x: x % X[0], X[1:]))
    if 0 in residue:
        residue.remove(0)

    if len(residue) == 0:
        return X[0]
    elif len(residue) == 1:
        return gcd([X[0], residue.pop()])
    return gcd(list(residue))

print(gcd(A))
