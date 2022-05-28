

Name ="C:\\Users\\mrinalini\\Documents\\PythonCode\\worktxt.txt"
f = open(Name, "a")

yourname = input('Enter your name: ')
b  = str(yourname)



f.write(str(yourname) + "\n" )
f.close ()


print('         ')
print('         ')
print('---------------Saved name into program---------------')
print('--------------------Thank you------------------------')