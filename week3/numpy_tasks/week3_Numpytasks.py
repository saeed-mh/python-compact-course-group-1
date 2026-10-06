import numpy as np

# Set 1 of Numpy tasks
# Task 1 Create and Reverse a Vector
print("\nTask 1 of Set 1")

original = np.arange(10, 50)

print("Original vector:")
print(original)

reverse = original[ : : -1]

print("Reversed vector:")
print(reverse)


# Task 2 Find Minimum and Maximum in a Random 5×5 Array
print("\nTask 2 of Set 1")

randomarray = np.random.random((5, 5))

print("5x5 random array:")
print(randomarray)

print("Minimum value:", randomarray.min())
print("Maximum value:", randomarray.max())


# Task 3 Normalize a Random 5×5 Matrix
print("\nTask 3 of Set 1")

original_matrix = np.random.random((5, 5))

print("Original matrix:")
print(original_matrix)

# using min-max normalization in this task

normalized_matrix = (original_matrix - original_matrix.min()) / (original_matrix.max() - original_matrix.min())

print("Normalized matrix:")
print(normalized_matrix)


# Task 4 Multiply a 5×3 Matrix by a 3×2 Matrix
print("\nTask 4 of Set 1")

A = np.random.random((5, 3))
B = np.random.random((3, 2))

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

C = np.dot(A, B)

print("Matrix product:")
print(C)

# Task 5 Find Yesterday, Today, and Tomorrow
print("\nTask 5 of Set 1")

today = np.datetime64("today", "D")
yesterday = today - np.timedelta64(1, "D")
tomorrow = today + np.timedelta64(1, "D")

print("Yesterday was", yesterday)
print("Today is", today)
print("Tomorrow will be", tomorrow)


# Task 6 Extract the Integer Part Using Five Methods
print("\nTask 6 of Set 1")

a = np.random.uniform(0,20,5)

print("Original array:")
print(a)

print("Method 1 (type casting):", a.astype(int))
print("Method 2 (floor function):", np.floor(a))
print("Method 3 (truncation function):", np.trunc(a))
print("Method 4 (modulo method):", a - a % 1)
print("Method 5 (modf function):", np.modf(a)[1])


# Task 7 Create a Structured Array for Position and Color
print("\nTask 7 of Set 1")

data_type = [
    ("position", [("x", float), ("y", float)]),
    ("color", [("r", int), ("g", int), ("b", int)])
]

a = np.zeros(3, dtype=data_type)

a[0] = ((1.0, 2.0), (255, 0, 0))
a[1] = ((3.0, 4.0), (0, 255, 0))
a[2] = ((5.0, 6.0), (0, 0, 255))

# print(a)

for item in a:
    print("Position:", item["position"], "Color:", item["color"])

# Set 2 of Numpy tasks
# Task 1 Create an Array Using a Generator Function
print("\nTask 1 of Set 2")

def generator():
    for i in range(10):
        yield i

generated_array = np.array(list(generator()))

print("Generated array:")
print(generated_array)


# Task 2 Check if Two Random Arrays are Equal
print("\nTask 2 of Set 2")

A = np.random.randint(0, 10, 5)
B = np.random.randint(0, 10, 5)

print("Array A:")
print(A)

print("Array B:")
print(B)

print("Are the two arrays equal?", np.array_equal(A, B))


# Task 3 Find Point-by-Point Distances of Coordinates
print("\nTask 3 of Set 2")

coordinates = np.random.random((100, 2))

difference = coordinates[:, np.newaxis, :] - coordinates[np.newaxis, :, :]

distance = np.sqrt(np.sum(difference ** 2, axis=2))

print("Coordinates:")
print(coordinates)

print("Point-by-point distances:")
print(distance)


# Task 4 Subtract the Mean of Each Row of a Matrix
print("\nTask 4 of Set 2")

original_matrix = np.random.random((5, 5))

print("Original matrix:")
print(original_matrix)

row_mean = original_matrix.mean(axis=1)

result = original_matrix - row_mean[:, np.newaxis]

print("Matrix after subtracting row means:")
print(result)


# Task 5 Sort an Array by the nth Column
print("\nTask 5 of Set 2")

array = np.array([
    [5, 2, 8],
    [1, 7, 4],
    [3, 1, 6],
    [2, 9, 5]
])

print("Original array:")
print(array)

n = 1 # sorting by second column

sorted_array = array[array[:, n].argsort()]

print("Array sorted by column", n)
print(sorted_array)


# Task 6 Compute the Rank of a Matrix
print("\nTask 6 of Set 2")

matrix = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [1, 1, 1]
])

print("Matrix:")
print(matrix)

rank = np.linalg.matrix_rank(matrix)

print("Rank of the matrix:", rank)


# Task 7 Find 4x4 Block Sums of a 16x16 Array
print("\nTask 7 of Set 2")

array = np.arange(256).reshape(16, 16)

print("Original 16x16 array:")
print(array)

block_sum = array.reshape(4, 4, 4, 4).sum(axis=(1, 3))

print("4x4 block sums:")
print(block_sum)