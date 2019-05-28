N = int(input())
T, A = map(int, input().split())
for i in range(N - 1):
    Ti, Ai = map(int, input().split())
    mt = T // Ti + (1 if T % Ti > 0 else 0)
    ma = A // Ai + (1 if A % Ai > 0 else 0)
    m = max(mt, ma)
    Ti *= m
    Ai *= m
    T, A = Ti, Ai
print(T + A)
