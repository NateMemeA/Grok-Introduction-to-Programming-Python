steps = int(input('How many steps? '))
steps = steps -1 
print('__')
for s in range(0, steps):
  print(' '*(2+s*2) + '|_')
print('_'*(2+steps*2) + '|')
