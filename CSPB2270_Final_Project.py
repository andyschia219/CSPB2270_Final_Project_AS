import numpy as np
import math
import random


row = int(input("Enter the number of rows:"))
column = int(input("Enter the number of columns:"))
 
# create matrix1
matrix1 = []
print("matrix1:", end ="\n")
for r in range(row):    
    temp = []
    # A for loop for column entries
    for c in range(column):   
        temp.append(random.randint(1, 3))
    matrix1.append(temp)
 
# print matrix1
for r in range(row):
    for c in range(column):
        print(matrix1[r][c], end=" ")
    print()

#create matrix2
matrix2 = []
for r in range(row):    
    temp = []
    # A for loop for column entries
    for c in range(column):   
        temp.append(random.randint(1, 3))
    matrix2.append(temp)
 
#print matrix2
print("matrix2:", end ="\n")
for r in range(row):
    for c in range(column):
        print(matrix2[r][c], end=" ")
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
for r in range(row):
    for c in range(column):
        print(result_matrix1[r][c], end=" ")
    print()


#Algorithm 2
# def split(matrix):
#     x = np.array(matrix1)
#     row1, col1 = x.shape
#     row2, col2 = row1//2, col1//2
#     return x[:row2, :col2], x[:row2, col2:], x[row2:, :col2], x[row2:, col2:]




def strassen(matrix1, matrix2):

    x = np.array(matrix1) 
    y = np.array(matrix2)

    if x.size == 1 or y.size == 1:
        return x * y

    n = x.shape[0]

    if n % 2 == 1:
        x = np.pad(x, (0, 1), mode='constant')
        y = np.pad(y, (0, 1), mode='constant')

    m = int(np.ceil(n / 2))

    # Split matrix 1
    a = x[: m, : m]
    b = x[: m, m:]
    c = x[m:, : m]
    d = x[m:, m:]

    # Split matrix 2
    e = y[: m, : m]
    f = y[: m, m:]
    g = y[m:, : m]
    h = y[m:, m:]    

    

    p1 = strassen(a, f - h)  
    p2 = strassen(a + b, h)        
    p3 = strassen(c + d, e)        
    p4 = strassen(d, g - e)        
    p5 = strassen(a + d, e + h)        
    p6 = strassen(b - d, g + h)  
    p7 = strassen(a - c, e + f)  

    c11 = p5 + p4 - p2 + p6  
    c12 = p1 + p2           
    c21 = p3 + p4            
    c22 = p1 + p5 - p3 - p7

    result = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return result


result_matrix2 = strassen(matrix1, matrix2)
print(result_matrix2)


