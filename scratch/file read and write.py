
print('------------------------------------------')
print('--  Mountain View Science Fair Lottery  --')
print('--      Mrinalini Kaul (5th Grade)      --')
print('------------------------------------------')

FNAME ="C:\\Users\\mrinalini\\Documents\\PythonCode\\choices.txt"
import random

x = random.randint(0,99)
y = random.randint(0,99)
z = random.randint(0,99)

f = open(FNAME, "r")
line = f.readline()
while line:
  #print('Prossecing ' + line)
  mylist = line.split(" ")
  #print(mylist)
  #howmany = len(mylist)
  #print(howmany)
  #print(mylist[3])
  a = mylist[0]
  b = int(mylist[1])
  c = int(mylist[2])
  d = int(mylist[3])
  e1 = x-b
  e2 = y-c
  e3 = z-d
  g1 = abs(e1)
  g2 = abs(e2)
  g3 = abs(e3)
  h1 =  g1 + g2 + g3 
  print(a, h1) 
  line = f.readline()

