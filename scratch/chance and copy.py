
copy ="C:\\Users\\mrinalini\\Documents\\PythonCode\\copy.txt"
chance ="C:\\Users\\mrinalini\\Documents\\PythonCode\\chance.txt"

f = open(chance, "r")
f2 = open(copy, "w")
line = f.readline()
while line:
  print(line)
  f2.write(line)
  line = f.readline()
f .close()
f2.close()



