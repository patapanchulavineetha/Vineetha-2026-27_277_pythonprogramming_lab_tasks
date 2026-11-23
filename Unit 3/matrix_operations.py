# Create two matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Matrix addition
addition = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]

# Matrix subtraction
subtraction = [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]

# Matrix multiplication
multiplication = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

print("Matrix A:", A)
print("Matrix B:", B)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
