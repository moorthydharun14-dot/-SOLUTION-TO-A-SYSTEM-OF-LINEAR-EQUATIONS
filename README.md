# -SOLUTION-TO-A-SYSTEM-OF-LINEAR-EQUATIONS
## Aim:
To write a python program to find a solution to a system of linear equations.
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
Step 1: Start the program and import the NumPy module.

Step 2: Define the coefficient matrix a and constant matrix b using np.array().

Step 3: Use np.linalg.solve(a, b) to compute the solution and store it in x.

Step 4: Print the solution and end the program.
## Program:
```
#Program to find the solution for the given linear equations.
#Developed by: DHARUN M 25018453
#RegisterNumber:212225230057
import numpy as np
a = np.array([[1,3],[2,5]])
b = np.array([5,-3])
x = np.linalg.solve(a,b)
print(x)
```
## Output:
<img width="1465" height="848" alt="Screenshot 2026-02-19 200441" src="https://github.com/user-attachments/assets/9a56e28a-e343-4cac-8238-85b9b9741ddc" />


## Result: 
Thus the solutions for the linear equations are successfully solved using python program

