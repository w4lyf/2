import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Element at index 2 in arr1:", arr1[2])
print("Element at row 1, column 2 in arr2:", arr2[1, 2])

print("Slice of arr1 from index 1 to 3:", arr1[1:4])
print("Slice of arr2 from row 0 to 2, and column 1:", arr2[:3, 1])

arr3 = np.array([1, 2, 3, 4, 5])
arr4 = np.array([6, 7, 8, 9, 10])
print("Addition of arr3 and arr4:", arr3 + arr4)
print("Multiplication of arr3 and arr4:", arr3 * arr4)

print("Sum of elements in arr1:", np.sum(arr1))
print("Minimum element in arr1:", np.min(arr1))
print("Maximum element in arr1:", np.max(arr1))
print("Mean of elements in arr1:", np.mean(arr1))
print("Standard deviation of elements in arr1:", np.std(arr1))

print("Square root of arr3:", np.sqrt(arr3))
print("Exponential of arr3:", np.exp(arr3))

arr5 = np.array([1, 2, 3, 4, 5])
bool_arr = arr5 > 2
print("Elements greater than 2:", arr5[bool_arr])
