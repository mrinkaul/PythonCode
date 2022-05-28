def square(var):
    var2 = var*var
    return var2

def cube(var):
    var3 = var*var*var
    return var3

nu = input('What is your number?')
sorc = input ('Would you like to square a number or cube it?')
number = int(nu)

if sorc == 'square':
    number2 = square(number)
    print(number2)
    
    
else:
    number3 = cube(number)
    print(number3)
    




