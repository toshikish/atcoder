A, B = map(int, input().split())

easy = True
while A > 0 and B > 0:
    if A % 10 + B % 10 >= 10:
        easy = False
        break
    A //= 10
    B //= 10
print('Easy' if easy else 'Hard')
