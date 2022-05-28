# i=0
# while(1>0):
 # print('abc', i)
 # i=i+1
 # if(i == 50):
   # break;
 
# print('outside')

  
# Ask user a number, and find absolute difference between it and x
# If difference is more than 50, print Too Cold
# If between 25 and 50, print Warm
# If between 10 and 25, print Hot
# If between 1 and 10, print Very Hot

print('------------------------------------------')
print('--  Mount OLive Distric Science Fair  --')
print('--      Mrinalini Kaul (5th Grade)      --')
print('------------------------------------------')

print("Welcome to Guess The Number! The rules are simple. You guess a number, and I say if it is hot, cold or other description")
print("")
# If exact, print You got it
import random
x = random.randint(1,99)
i=0
while(1==1):
	a = input ('Enter a whole number between 0 and 99: ')
	z = int(a)
	b = x - z
	c = abs(b)
	i=i+1

	if (c >= 50):
	  print(" Too Cold!")
	elif( (c >= 40) & (c < 50)):
	  print("Cold")
	elif( (c >= 30) & (c < 40)):
	  print("Warm")
	elif( (c >= 20) & (c < 30)):
	  print("Warmer")
	elif( (c >=10) & (c < 20)):
	  print("Hot")
	elif( (c >=5) & (c < 10)):
	  print("Hot Hot Hot")
	elif( (c >=1) & (c < 5)):
	  print("Super Hot!!!")
	elif (c == 0):
	  print("YOU'RE ON FIRE!!! Good job!!!")
	  break
	  
print('Thanks for playing. You took ', i, 'tries to guess the number')
  
