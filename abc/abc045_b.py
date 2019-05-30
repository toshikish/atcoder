S = [list(input()) for i in range(3)]
member = ['a', 'b', 'c']

turn = 0
while S[turn] != []:
    turn = member.index(S[turn].pop(0))
print(member[turn].upper())
