arr = [1.5, 3.2, 0.7, 4.1, 2.8, 5.6, 1.9]


def main():
    threshold = float(input("Enter threshold value: "))

    greater_count = sum(1 for num in arr if num > threshold)

    # Print results
    print(f"Array: {arr}")
    print(f"Threshold: {threshold}")
    print(f"Number of elements greater than {threshold}: {greater_count}")
    

if __name__ == '__main__':
    main()