
x =(input("Enter a number: "))
num = float(x)
counter = 0



while num != 1:
    
    if (num % 2) == 0:
        num = num/2
        print(num)
        counter = counter + 1
            
    elif(num % 2) != 0:
        while (num % 2) != 0:
            num = num*3 +1
            
            print(num)
            
            counter = counter + 1
            
print(counter)