#
# Write a program where you pre-choose one number between 0 and 99
# Then ask the user for a number
# Find out how far is their number from your number and print nicely 
# Hint: you willl be using abs, int, input, print

x = 74
z = input ('Enter a whole number between 0 and 99:')
a = int (z)
f = x - a
b = abs (f)
print ('Your number was ', a, '. My number was ', b, ' away from your number.')
