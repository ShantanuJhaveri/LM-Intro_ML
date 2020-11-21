# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW3
# Question 1

# Use numpy to create 200 random integers between 1 and 200. Store them in X. Similarly, create
# 200 more random integers between 1 and 200. Then display a scatter plot of X vs Y.

from numpy import random
from numpy.random import seed
import matplotlib.pyplot as plt

seed(3)

x = random.randint(200, size=200)
y = random.randint(200, size=200)
plt.title("Scatter of random integers", color='g')
plt.suptitle('Jhaveri_Shantanu_HW3_Q1')
plt.xlabel('Random integer(x)', color='b')
plt.ylabel('Random integer(y)', color='b')
plt.scatter(x, y, s=5, color='r')
plt.show()
