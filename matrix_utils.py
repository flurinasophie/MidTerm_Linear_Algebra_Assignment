import random

# Definition of thr matrix multiplication function 
def matrix_multiply(A, B):
    # Check the dimensions
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    # Ensure the inner dimensions match
    if cols_A != rows_B:
        raise ValueError("Incompatible dimensions for matrix multiplication")
    
    # Initialize the result matrix with zeros
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform the multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or range(rows_B), as cols_A == rows_B
                C[i][j] += A[i][k] * B[k][j]
    
    return C

# Function to create a random n x n matrix
def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# Matrix addition helper
def add_matrices(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

# Matrix subtraction helper
def subtract_matrices(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

# Function to create a random n x n matrix
def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

