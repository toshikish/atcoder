A, B, C = map(int, input().split())

a = A if C % 2 == 1 else A * A
b = B if C % 2 == 1 else B * B
print('<' if a < b else '>' if a > b else '=')
