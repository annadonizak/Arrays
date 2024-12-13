arr = [15, 8, 31, 47, 2, 19]

print("existed array:", ' '.join([str(item) for item in arr]))

reversed_arr = []
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])

# there is an alternative, neat way to do that
# reversed_arr = arr[::-1]
print("reverse array:", ' '.join([str(item) for item in arr]))