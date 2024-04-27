import numpy as np
import math
import random


Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
 
# Initialize matrix
matrix = []

# A for loop for row entries
for row in range(Row):    
    a = []
    # A for loop for column entries
    for column in range(Column):   
        a.append(random.randint(1, 10))
    matrix.append(a)
 
# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()

