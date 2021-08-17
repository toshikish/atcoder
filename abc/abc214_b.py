S, T = map(int, input().split())
print([a + b + c <= S and a * b * c <= T for a in range(S + 1)
       for b in range(S + 1) for c in range(S + 1)].count(True))
