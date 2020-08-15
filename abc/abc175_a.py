S = input()
print(3 if S == 'RRR' else 2 if S[0:2] == 'RR' or S[1:3]
      == 'RR' else 1 if 'R' in S else 0)
