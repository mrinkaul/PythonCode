person1name = input('Please enter your full name:')
person1age = input('Please enter your age:')

person2name = input('Please enter the name of someone you know:')
person2age = input('Please enter the age of the same person:')

p1age = int(person1age)
p2age = int(person2age)

ogdif = p2age - p1age
a = 0

if ogdif > a:
    x = 'older'
else:
   x = 'younger'
    

newdif = abs (ogdif)

print ('Your friend,' , person2name, 'is' , x , 'to you,' ,person1name, 'by' , newdif , 'years.')
