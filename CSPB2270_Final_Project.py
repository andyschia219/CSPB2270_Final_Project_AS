import numpy as np
import math
import random


Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
 
# create matrix1
matrix1 = []
print("matrix1:", end ="\n")
for row in range(Row):    
    temp = []
    # A for loop for column entries
    for column in range(Column):   
        temp.append(random.randint(1, 3))
    matrix1.append(temp)
 
# print matrix1
for row in range(Row):
    for column in range(Column):
        print(matrix1[row][column], end=" ")
    print()

#create matrix2
matrix2 = []
for row in range(Row):    
    temp = []
    # A for loop for column entries
    for column in range(Column):   
        temp.append(random.randint(1, 3))
    matrix2.append(temp)
 
#print matrix2
print("matrix2:", end ="\n")
for row in range(Row):
    for column in range(Column):
        print(matrix2[row][column], end=" ")
    print()


#Algorithm1 Iterative Approach
result_matrix1 = []
total = 0
for i in range(len(matrix1)):
    temp = []
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            total += matrix1[i][k] * matrix2[k][j]
        temp.append(total)  
        total = 0  
    result_matrix1.append(temp)    

#print Algorithm1 result matrix
print("result matrix:", end ="\n")
for row in range(Row):
    for column in range(Column):
        print(result_matrix1[row][column], end=" ")
    print()


#Algorithm 2



