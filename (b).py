import random
import time

# Re-use the matrix_multiply function from Task 1.a
def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        raise ValueError("Incompatible dimensions for matrix multiplication")
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Function to create a random n x n matrix
def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# List of matrix sizes to test
matrix_sizes = [10, 20, 50, 100, 200, 500, 1000]  # Adjust as needed
results = []

# Loop through each matrix size, measure time taken for multiplication
for n in matrix_sizes:
    A = generate_matrix(n)
    B = generate_matrix(n)

    start_time = time.time()
    matrix_multiply(A, B)
    end_time = time.time()

    time_taken = end_time - start_time
    results.append((n, time_taken))
    print(f"Matrix size: {n}x{n}, Time taken: {time_taken:.4f} seconds")

# Display results
for size, timing in results:
    print(f"Size: {size}x{size} took {timing:.4f} seconds")
