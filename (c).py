import random
import time
import numpy as np
import matplotlib.pyplot as plt

# matrix_multiply function from Task 1.a
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

# List of matrix sizes to test, reduced sizes for quicker testing
matrix_sizes = [10, 20, 50, 100, 200]
custom_times = []
numpy_times = []

# Toggle to skip the custom multiplication if needed
test_only_numpy = False  # Set to True if you only want to test NumPy timings

# Loop through each matrix size and measure times for both methods
for n in matrix_sizes:
    print(f"Starting matrix size: {n}x{n}")  # Track progress

    # Generate random matrices A and B of size n x n
    A = generate_matrix(n)
    B = generate_matrix(n)

    if not test_only_numpy:
        print("Timing custom matrix multiply...")  # Print before custom timing
        start_time = time.time()
        matrix_multiply(A, B)
        end_time = time.time()
        custom_time = end_time - start_time
        custom_times.append(custom_time)
        print(f"Custom Time for {n}x{n}: {custom_time:.4f} seconds")
    else:
        custom_times.append(None)  # Placeholder if only testing NumPy

    # Convert A and B to NumPy arrays for comparison
    A_np = np.array(A)
    B_np = np.array(B)

    print("Timing NumPy dot...")  # Print before NumPy timing
    start_time = time.time()
    np.dot(A_np, B_np)
    end_time = time.time()
    numpy_time = end_time - start_time
    numpy_times.append(numpy_time)
    print(f"NumPy Time for {n}x{n}: {numpy_time:.4f} seconds")

print("Finished timing. Now generating plot...")

# Plot the results (only plot custom times if available)
plt.figure(figsize=(10, 6))
if not test_only_numpy:
    plt.plot(matrix_sizes, custom_times, label="Custom Matrix Multiply", marker='o')
plt.plot(matrix_sizes, numpy_times, label="NumPy dot", marker='o')
plt.xlabel("Matrix Size (n x n)")
plt.ylabel("Time (seconds)")
plt.title("Performance Comparison of Matrix Multiplication Methods")
plt.legend()
plt.grid(True)
plt.show()
