A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

print('YES' if V > W and abs(A - B) <= (V - W) * T else 'NO')
