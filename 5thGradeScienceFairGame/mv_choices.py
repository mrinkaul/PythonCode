print('------------------------------------------')
print('--  Mountain View Science Fair Lottery  --')
print('--      Mrinalini Kaul (5th Grade)      --')
print('------------------------------------------')

FNAME ="C:\\Users\\mrinalini\\Documents\\Code\\PythonCode\\choices.txt"

name = input('Enter your name: ')
a1 = input ('Enter a whole number between 0 and 99: ')
a2 = input ('Enter a whole number between 0 and 99: ')
a3 = input ('Enter a whole number between 0 and 99: ')

b  = str(name).strip()
b1 = int (a1)
b2 = int (a2)
b3 = int (a3)

f = open(FNAME, "a")
f.write(b + " " + str(a1) + " " + str(a2) + " " + str(a3) + "\n" )
f.close ()

print('------------------------------------------')
print('Thank you ' + b + ', for your choices')
print('Results will be generated randomly')

print('------------------------------------------') 