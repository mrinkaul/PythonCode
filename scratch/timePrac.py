import time
print("Time since the epoch:" , time.time())
print("Actual Time:" , time.asctime(time.localtime(time.time())))

keep_going = True

#while keep_going:
 #   if time.asctime(time.localtime(time.time())) == "Thu Jul 22 9:13:30 2021":
  #    print ("timer done!")
   #   keep_going = False
    #print("timer not done.")
   
   
startTime = time.time()
keep_going = True
    currentTime = time.time