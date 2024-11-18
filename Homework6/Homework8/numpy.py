#1
import numpy as np

array = np.zeros(10)
array[4] = 1
print(array) 
#2
array = np.arange(10, 50)
print(array) 
#3
reversed_array = array[::-1]
print(reversed_array)  
#4
matrix = np.arange(9).reshape(3, 3)
print(matrix) 
#5
array = np.array([1, 2, 0, 0, 4, 0])
non_zero_indices = np.nonzero(array)
print(non_zero_indices)  
#6
identity_matrix = np.eye(3)
print(identity_matrix)
#7
random_matrix = np.random.random((3, 3))
min_value = random_matrix.min()
max_value = random_matrix.max()
print(random_matrix)
print(f"Minimum: {min_value}, Maximum: {max_value}")
#8
random_matrix = np.random.random((5, 5))
normalized_matrix = (random_matrix - random_matrix.min()) / (random_matrix.max() - random_matrix.min())
print(normalized_matrix)
#9
array = np.array([1, 3, 5, 11, 15, 20, 25])
target = 14
closest_value = array[np.abs(array - target).argmin()]
print(closest_value)  
#10
array = np.array([[5, 9, 3], [10, 2, 15], [6, 7, 8]])
array[np.arange(array.shape[0]), array.argmax(axis=1)] = 0
print(array)  
#11
array = np.array([2, 3, 2, 5, 8, 3, 3, 7, 2, 3, 5, 5, 5, 5])
counts = np.bincount(array)
most_common_value = np.argmax(counts)
print(most_common_value) 
#12
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
product = np.dot(array, array.T)
print(product)  
#13
matrix = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
determinant = np.linalg.det(matrix)
print(determinant) 
#14
matrix = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
try:
    inverse_matrix = np.linalg.inv(matrix)
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("Matrix is singular and non-invertible.")
