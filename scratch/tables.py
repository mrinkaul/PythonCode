num = 0

while(num <= 12):
  print('Table of ',num)
  for i in range(0, 13):
    print(num,'x',i,'=',num*i)
  print('\n')
  num = num + 1