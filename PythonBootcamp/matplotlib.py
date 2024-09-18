# Representing the graph by using Matplotlib


import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,4,6,8,10]

# #dimensions must be same means x=y
# plt.title("Student Data Graph")
# plt.plot(x,y)
# plt.show()  #display the graph



# Showing your life journey on the basis of your 10th 12th and graduation marks

import numpy as np

x = np.array([2018,2020,2022,2023,2024])
y = np.array([61,64,73.2,81.5,82])
plt.title("My Life Graph")
plt.xlabel("Semester")
plt.ylabel("Student Performance")
plt.plot(x,y)
plt.show()