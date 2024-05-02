import numpy as np
import random
from timeit import default_timer as timer


#create a matrix with random integers between 1 and 3
def create_matrix(row, column):
    matrix = []
    for r in range(row):
        temp_row = []
        for c in range(column):
            temp_row.append(random.randint(1,3))
        matrix.append(temp_row)  
    return matrix


#print matrix
def print_matrix(matrix, row, column):
    x = np.array(matrix)
    row = row
    column = column
    for r in range(row):
        for c in range(column):
            print(x[r][c], end=" ")
        print()   
    print()
    return     


#Algorithm1 - Iterative Approach
def iterative(matrix1, matrix2):
    result_matrix = []
    total = 0
    for i in range(len(matrix1)):
        temp = []
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            temp.append(total)  
            total = 0  
        result_matrix.append(temp)  
    return result_matrix   

#Algoritm2 - Strassen's Algorithm
def strassen(matrix1, matrix2):

    x = np.array(matrix1) 
    y = np.array(matrix2)

    if x.size == 1 or y.size == 1:
        return x * y

    #get partition index
    n = x.shape[0]
    m = int(np.ceil(n / 2))

    # partition matrix 1
    a = x[: m, : m]
    b = x[: m, m:]
    c = x[m:, : m]
    d = x[m:, m:]

    # partition matrix 2
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


#create 4x4 matrix
row = 4
column = 4

matrix1 = create_matrix(row, column)
matrix2 = create_matrix(row, column)  

print("Matrix1:")
print_matrix(matrix1, row, column)
print("Matrix2:")
print_matrix(matrix2, row, column)   

#iterative algoritm
start = timer()
iterative_matrix = iterative(matrix1, matrix2)
end = timer()

print("4x4 Matrix Iterative Algorithm Resulst:")
print_matrix(iterative_matrix, row, column)

print("4x4 Matrix Iterative Algorithm Runtime:")
print(end - start, "\n")

#strassen algorithm
start = timer()
strassen_matrix = strassen(matrix1, matrix2)
end = timer()

print("4x4 Matrix Strassen Algorithm Result:")
print_matrix(strassen_matrix, row, column)

print("4x4 Matrix Iterative Algorithm Runtime:")
print(end - start, "\n")

input("Press Enter to continue...")





#create 8x8 matrix
row = 8
column = 8

matrix1 = create_matrix(row, column)
matrix2 = create_matrix(row, column)  

print("Matrix1:")
print_matrix(matrix1, row, column)
print("Matrix2:")
print_matrix(matrix2, row, column)   

#iterative algoritm
start = timer()
iterative_matrix = iterative(matrix1, matrix2)
end = timer()

print("8x8 Matrix Iterative Algorithm Resulst:")
print_matrix(iterative_matrix, row, column)

print("8x8 Matrix Iterative Algorithm Runtime:")
print(end - start, "\n")

#strassen algorithm
start = timer()
strassen_matrix = strassen(matrix1, matrix2)
end = timer()

print("8x8 Matrix Strassen Algorithm Result:")
print_matrix(strassen_matrix, row, column)

print("8x8 Matrix Iterative Algorithm Runtime:")
print(end - start, "\n")

input("Press Enter to continue...")



#create 32x32 matrix
row = 32
column = 32

matrix1 = create_matrix(row, column)
matrix2 = create_matrix(row, column)  

print("Matrix1:")
print_matrix(matrix1, row, column)
print("Matrix2:")
print_matrix(matrix2, row, column)   

#iterative algoritm
start = timer()
iterative_matrix = iterative(matrix1, matrix2)
end = timer()

print("32x32 Matrix Iterative Algorithm Resulst:")
print_matrix(iterative_matrix, row, column)

print("32x32 Matrix Iterative Algorithm Runtime:")
print(end - start, "\n")

#strassen algorithm
start = timer()
strassen_matrix = strassen(matrix1, matrix2)
end = timer()

print("32x32 Matrix Strassen Algorithm Result:")
print_matrix(strassen_matrix, row, column)

print("32x32 Matrix Iterative Algorithm Runtime:")
print(end - start, "\n")

input("Press Enter to continue...")

#create 64x64 matrix
row = 64
column = 64

matrix1 = create_matrix(row, column)
matrix2 = create_matrix(row, column)  

print("Matrix1:")
print_matrix(matrix1, row, column)
print("Matrix2:")
print_matrix(matrix2, row, column)   

#iterative algoritm
start = timer()
iterative_matrix = iterative(matrix1, matrix2)
end = timer()

print("64x64 Matrix Iterative Algorithm Resulst:")
print_matrix(iterative_matrix, row, column)

print("64x64 Matrix Iterative Algorithm Runtime:")
print(end - start, "\n")

#strassen algorithm
start = timer()
strassen_matrix = strassen(matrix1, matrix2)
end = timer()

print("64x64 Matrix Strassen Algorithm Result:")
print_matrix(strassen_matrix, row, column)

print("64x64 Matrix Iterative Algorithm Runtime:")
print(end - start, "\n")

input("Press Enter to continue...")

#create 128x128 matrix
row = 128
column = 128

matrix1 = create_matrix(row, column)
matrix2 = create_matrix(row, column)  

print("Matrix1:")
print_matrix(matrix1, row, column)
print("Matrix2:")
print_matrix(matrix2, row, column)   

#iterative algoritm
start = timer()
iterative_matrix = iterative(matrix1, matrix2)
end = timer()

print("128x128 Matrix Iterative Algorithm Resulst:")
print_matrix(iterative_matrix, row, column)

print("128x128 Matrix Iterative Algorithm Runtime:")
print(end - start, "\n")

#strassen algorithm
start = timer()
strassen_matrix = strassen(matrix1, matrix2)
end = timer()

print("128x128 Matrix Strassen Algorithm Result:")
print_matrix(strassen_matrix, row, column)

print("128x128 Matrix Iterative Algorithm Runtime:")
print(end - start, "\n")


print("fin")



####To DO#####
# containerize functions: print, create matrix

# show time of two functions

# Challenges:
# creating the iterative algorithm and strassen algorithm by hand. keeping track of what was happening in each for loop was brain melty
# talk about the other algorithms added
# also just keeping the flow of the project organized with functions was challenging. I just jumped in using the print method and generate matrix methods, without putting them in a functions 
# and then I lost track when I was copy and pasting for testing. It became difficult to manage

# https://github.com/hardianlawi/algorithm-implementation/blob/master/src/multiplication/strassenAlgorithm.py
# https://www.geeksforgeeks.org/strassens-matrix-multiplication/
