a1 = 34
a2 = 67
a3 = 98
name  = input('What is your name:')
b1 = input ('Enter a whole number between 0 and 99:')
b2 = input ('Enter a whole number between 0 and 99:')
b3 = input ('Enter a whole number between 0 and 99:')
c1 = int (b1)
c2 = int (b2)
c3 = int (b3)
d1 = a1 - c1
d2 = a2 - c2
d3 = a3 - c3
e1 = abs (d1)
e2 = abs (d2)
e3 = abs (d3)
s = e1 + e2 + e3
print (name,c1,c2,c3)  
print (name, "," ,c1, "," ,c2, "," ,c3,)
print (name, "," ,s,)
