A, B = map(int, input().split())
S = A + B
print(S // 2 if S % 2 == 0 else 'IMPOSSIBLE')
