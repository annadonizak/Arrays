"""
Prints some array elements
"""

arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print("First value:", arr[0])
print("Second value:", arr[1])
print("Last value:", arr[-1])
print("Last but one value:", arr[len(arr) - 2])
print("Sum of first and last value:", arr[0] + arr[-1])
middle_index = len(arr) // 2
print("Middle value:", arr[middle_index])
print("All values separated by space:", end=" ")
for value in arr:
    print(value, end=" ")