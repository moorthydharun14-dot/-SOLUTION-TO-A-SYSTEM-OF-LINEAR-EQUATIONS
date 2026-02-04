#Program to find the solution for the given linear equations.
#Developed by: DHARUN M 25018453
#RegisterNumber:212225230057
import numpy as np
a = np.array([[1,3],[2,5]])
b = np.array([5,-3])
x = np.linalg.solve(a,b)
print(x)
