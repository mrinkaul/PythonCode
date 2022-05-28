#
# Example on how to open a new file and write something to it
#
FNAME="C:\\Users\\mrinalini\\Documents\\PythonCode\\this_is ma_file_test.txt"
myname='Vikram'
a = 99
# w below says write (create new, or of already there, wipe it and create new)
f = open(FNAME, "w")
f.write("This is the first line\n")
f.write("Second line\n")
f.write("The value of a = " + str(a) + "\n")
f.write(str(a) + "\n")
f.write("The name = " + myname + "\n")
f.close()
print("Finished writing in w mode to ", FNAME)



a = 324
myname ='MR'
# a below says append to a file (create new, or if already there, open it at the end to start writing)
f = open(FNAME, "a")
f.write("This is appended\n")
f.write("The value of a = " + str(a) + "\n")
f.write("The name = " + myname + "\n")
f.close()
print("Finished writing in a mode to ", FNAME)
f = open(FNAME, "w")
f.write("I am bored")
f.close()