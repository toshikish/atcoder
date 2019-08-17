S = int(input())
G = 10 ** 9

Q = S // G
R = S % G
if R > 0:
    Q += 1
    R -= G

print(0, 0, G, 1, -R, Q)
