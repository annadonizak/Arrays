"""
Modifies the array values. Prints the array after each change.
"""


arr = [1, 2, 3, 4, 5]
print('Array:', arr)

arr[0] -= 1
print('Array:', arr)

arr[-1] += 4
print('Array:', arr)

middle_index = len(arr) // 2
arr[middle_index] *= 2
print('Array:', arr)