arr = [15, 8, 31, 47, 2, 19]

print("Array:", ' '.join(map(str, arr)))

total_sum = 0
for num in arr:
    total_sum += num

mean = total_sum / len(arr)

print("Arithmetic mean:", mean)