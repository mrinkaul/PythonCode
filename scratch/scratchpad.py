#Hello World
print('Hello World')

#If/Else with varibles
x=1
if x==2:
    print('x is 1')
else:
    print('x is not 1')
#Floats-Decimal
myfloat = 7.0
print(myfloat)
#Int-number
myint = -5
print(myint)
#More Stuff
one = 1
two = 2
three = one + two
print(three)


#AnExercise
#Change first 3
mystring = "hello"
myfloat = 10.0
myint = 20


if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
     print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
	
#Exersice2
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)