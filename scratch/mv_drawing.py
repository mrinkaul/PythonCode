
print('------------------------------------------')
print('--  Mountain View Science Fair Lottery  --')
print('--      Mrinalini Kaul (5th Grade)      --')
print('------------------------------------------')

FNAME ="C:\\Users\\mrinalini\\Documents\\PythonCode\\choices.txt"
import random


r1 = random.randint(0,99)
r2 = random.randint(0,99)
r3 = random.randint(0,99)

print('')
print('Winning numbers are', r1, r2, r3)
#print('Results:')
print('')

f = open(FNAME, "r")
line = f.readline()
while line:
  #print('Prossecing ' + line)
  mylist = line.split(" ")
  #print(mylist)
  #howmany = len(mylist)
  #print(howmany)
  #print(mylist[3])
  
  name = mylist[0]
  c1 = int(mylist[1])
  c2 = int(mylist[2])
  c3 = int(mylist[3])
  
  e1 = r1-c1
  e2 = r2-c2
  e3 = r3-c3
  
  g1 = abs(e1)
  g2 = abs(e2)
  g3 = abs(e3)
  
  h1 =  g1 + g2 + g3 
  
  print("{:<9}".format(name), ' : Selections: ', c1, c2, c3, ' => Total :',  h1) 
  line = f.readline()
  
f.close()
print('------------------------------------------')
print('Lowest Absolute Total wins the lottery')
print('------------------------------------------')

