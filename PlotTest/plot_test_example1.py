import matplotlib.pyplot as plt
  

x1 = [1,3]
y1 = [2,1]
    
plt.plot(x1, y1, label = "line 1")
  

x2 = [1,2]
y2 = [4,1]


plt.plot(x2, y2, label = "line 2")
  

plt.title('linear graph.')
plt.legend()
plt.show()
