#I put the def matrix_multiply(A, B) in a different file so if I make changes 
#I only have to make changes in that file instead of on every single file
from matrix_utils import matrix_multiply

# Test 1 (small 2x2 matrices)
A = [
    [1, 2],
    [3, 4]
]

B = [
    [2, 0],
    [1, 3]
]

# Expected output: [[4, 6], [10, 12]]
print("Test Case 1 Result:", matrix_multiply(A, B))


# Test 2 (identity matrix multiplication)
A = [
    [5, 7],
    [1, 2]
]

I = [
    [1, 0],
    [0, 1]
]

# Expected output: [[5, 7], [1, 2]]
print("Test Case 2 Result:", matrix_multiply(A, I))


# Test 3 (incompatible matrices (should raise an error))
A = [
    [1, 2],
    [3, 4]
]

B = [
    [1, 2]
]

try:
    matrix_multiply(A, B)
except ValueError as e:
    print("Test Case 3 Error:", e)


# Test 4: (larger matrix multiplication)
import numpy as np

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Expected output from numpy for verification
expected_output = np.dot(A, B)
print("Expected Output (NumPy):\n", expected_output)

# Output from our function
print("Function Output:", matrix_multiply(A, B))
