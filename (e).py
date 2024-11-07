import random
import time
import matplotlib.pyplot as plt
from matrix_utils import add_matrices, subtract_matrices, generate_matrix

# Implementation of Strassen’s algorithm for two-dimensional matrices (without the recursion)
def strassen_2x2(A, B):
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]
    
    M1 = (a + d) * (e + h)
    M2 = (c + d) * e
    M3 = a * (f - h)
    M4 = d * (g - e)
    M5 = (a + b) * h
    M6 = (c - a) * (e + f)
    M7 = (b - d) * (g + h)
    
    return [
        [M1 + M4 - M5 + M7, M3 + M5],
        [M2 + M4, M1 - M2 + M3 + M6]
    ]

# Implementation of Strassen’s algorithm for two-dimensional matrices (with the recursion)
def strassen_recursive(A, B):
    n = len(A)
    if n == 2:
        return strassen_2x2(A, B)
    
    # Split matrices into quadrants
    mid = n // 2
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    # Recursive multiplications
    M1 = strassen_recursive(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen_recursive(add_matrices(A21, A22), B11)
    M3 = strassen_recursive(A11, subtract_matrices(B12, B22))
    M4 = strassen_recursive(A22, subtract_matrices(B21, B11))
    M5 = strassen_recursive(add_matrices(A11, A12), B22)
    M6 = strassen_recursive(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen_recursive(subtract_matrices(A12, A22), add_matrices(B21, B22))
    
    # Combine results
    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(subtract_matrices(add_matrices(M1, M3), M2), M6)
    
    # Combine quadrants into a single matrix
    C = [[0] * n for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    return C

# Benchmark Strassen's recursive algorithm against other methods
matrix_sizes = [2, 4, 8, 16, 32, 64]
strassen_times = []

for n in matrix_sizes:
    A = generate_matrix(n)
    B = generate_matrix(n)
    
    start_time = time.time()
    strassen_recursive(A, B)
    end_time = time.time()
    strassen_time = end_time - start_time
    strassen_times.append(strassen_time)
    print(f"Matrix size: {n}x{n}, Strassen Recursive Time: {strassen_time:.4f} seconds")

plt.plot(matrix_sizes, strassen_times, label="Strassen Recursive", marker='o')
plt.xlabel("Matrix Size (n x n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()