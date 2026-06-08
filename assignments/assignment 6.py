#PART 1
import numpy as np
# Python list
numbers = list(range(100000))
start = time.time()
numbers = [x * 5 for x in numbers]
end = time.time()
print("List time:", end - start)

# NumPy array
arr = np.arange(100000)
start = time.time()
arr = arr * 5
end = time.time()
print("NumPy time:", end - start)
#PART 2
import numpy as np

# 1D array
arr1 = np.arange(1, 11)
print(arr1)

# 2D array
arr2 = np.arange(1, 10).reshape(3, 3)
print(arr2)

# Array information
for arr in [arr1, arr2]:
    print("Dimensions:", arr.ndim)
    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print("Data type:", arr.dtype)
    print("Element size:", arr.itemsize, "bytes\n")

# Convert float array to integer
float_arr = np.array([[1.1, 2.2, 3.3],
                      [4.4, 5.5, 6.6],
                      [7.7, 8.8, 9.9]])
int_arr = float_arr.astype(int)
print(int_arr)
#PART 3
import numpy as np

zeros = np.zeros((4,4))
ones = np.ones((3,2))
identity = np.eye(5)
sevens = np.full((2,3), 7)
randoms = np.random.randint(10, 99, (3,4))

print(zeros, "\n", ones, "\n", identity, "\n", sevens, "\n", randoms)

# np.arange + reshape
arr = np.arange(5, 55, 5).reshape(3,3)
print(arr)
#PART 4
arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

print("Second row:", arr[1])
print("First two rows & two columns:\n", arr[:2, 1:3])
print("Last column:", arr[:, -1])
arr[1] = [1, 2, 3, 4]
print("After replacement:\n", arr)
#PART 5
A = np.random.randint(1, 10, 5)
B = np.random.randint(1, 10, 5)

print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)
print("Division:", A / B)

# Functions
print("Square root:", np.sqrt(A))
print("Exponential:", np.exp(A))
print("Sine:", np.sin(A))

# Celsius to Fahrenheit
C = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
F = (C * 9/5) + 32
print("Fahrenheit:", F)
#PART 6
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print("Add 10:\n", A + 10)
print("Add row [1,2,3]:\n", A + np.array([1,2,3]))
print("Add column [[1],[2],[3]]:\n", A + np.array([[1],[2],[3]]))
#PART 7
arr = np.arange(1, 13)
print(arr.reshape(3,4))
print(arr.reshape(2,6))

# flatten vs ravel
a = np.arange(1, 10).reshape(3,3)
flat = a.flatten()
ravel = a.ravel()

flat[0] = 100
ravel[0] = 200

print("Original after flatten:", a)  # no change
print("Original after ravel:", a)    # changes
