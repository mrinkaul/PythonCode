
chance ="C:\\Users\\mrinalini\\Documents\\PythonCode\\work.txt"

f = open(chance, "r")
line = f.readline()
print(line)
  
print('yay it works!!!!!')
line = f.readline()
f.close()
print("done")





copy ="C:\\Users\\mrinalini\\Documents\\PythonCode\\copy.txt"
f = open(copy, "w")
f.write(line)
f.close ()
print('Done again yay tho!!!')
