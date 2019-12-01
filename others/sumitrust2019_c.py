X = int(input())
print(1 if X % 105 == 0 or X % 100 == 0 or X // 105 + 1 <= X // 100 else 0)
