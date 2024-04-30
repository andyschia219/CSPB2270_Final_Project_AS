import numpy as np
import math
import random


Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
 
# Initialize matrix
matrix1 = []

# A for loop for row entries
print("matrix1:", end ="\n")
for row in range(Row):    
    a = []
    # A for loop for column entries
    for column in range(Column):   
        a.append(random.randint(1, 9))
    matrix1.append(a)
 
# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix1[row][column], end=" ")
    print()

matrix2 = []

for row in range(Row):    
    a = []
    # A for loop for column entries
    for column in range(Column):   
        a.append(random.randint(1, 9))
    matrix2.append(a)
 
# For printing the matrix
print("matrix2:", end ="\n")
for row in range(Row):
    for column in range(Column):
        print(matrix2[row][column], end=" ")
    print()



#Alorithm 1 - Iterative Approach
#def iterative_algorithm(matrix1, matrix2):

result_matrix = []

for row in range(Row):
    a = []
    for column in range(Column):
        a.append(matrix1[row][column]*matrix2[row][column])
    result_matrix.append(a)    
     



print("result matrix:", end ="\n")
for row in range(Row):
    for column in range(Column):
        print(result_matrix[row][column], end=" ")
    print()



#Algorithm 2


#Algorithm 3

