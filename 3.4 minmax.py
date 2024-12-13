arr = [-15, 8, -31, 47, -2, 19]

min_value = arr[0]
max_value = arr[0]

for num in arr:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

print("Minimum number:", min_value)
print("Maximum number:", max_value)