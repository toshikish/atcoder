X = int(input())

for A in range(-118, 120):
    Ap = A * A * A * A * A
    for B in range(-119, 119):
        Bp = B * B * B * B * B
        if Ap - Bp == X:
            break
        elif Ap - Bp == -X:
            A, B = B, A
            break
    else:
        continue
    break
print(A, B)
