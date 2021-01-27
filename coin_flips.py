# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

n = 4
toss = list('-' * n)
def coin_flips(n):
  if type(n) != int:
    raise TypeError('Value must be an integer.')  
  if n < 1:
    raise ValueError('Value must be greater than 0.')
  global toss
  if n == 1:
    toss[-n] = 'T'
    print(''.join(toss))
    toss[-n] = 'H'
    print(''.join(toss))
  else:
    toss[-n] = 'T'
    coin_flips(n-1)
    toss[-n] = 'H'
    coin_flips(n-1)

print(coin_flips(n)) 
# => ["HH", "HT", "TH", "TT"]