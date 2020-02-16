N = int(input())
A = list(map(int, input().split()))

approved = True
for Ai in A:
    if Ai % 2 == 0 and Ai % 3 != 0 and Ai % 5 != 0:
        approved = False
        break
print('APPROVED' if approved else 'DENIED')
