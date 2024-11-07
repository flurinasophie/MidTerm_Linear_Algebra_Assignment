# Explanation of Time Complexity for Both Methods

# Matrix Multiplication:
# - The function has three nested loops (one for each row, column, and the shared dimension)
# - For each element in the result matrix, the function performs n multiplications and additions
# - Given a matrix of size n x n, there are n^2 elements to compute (fore each element it performs n operations)
# - Time Complexity = O(n x n x n) = On^3

# NumPys dot function: 
# - The function is implemented in optimized low-level languages like C or Fortran (they are much faster than Python)
# Uses optimized librarys

# Differences
# The languages and implementations (Python - lower-level languages C or Fortran)
# Algorithmische Optimierung (three nested loops - optimized linear algebra libraries (BLAS/LAPACK))