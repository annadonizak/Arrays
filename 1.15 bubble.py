car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    print('Car fuel consumption ', car_fuel_consumption)
    print('Car fuel consumption (sorted) ', bubble_sort(car_fuel_consumption))

    print('Bank transactions ', bank_transactions)
    print('Bank transactions (sorted) ', bubble_sort(bank_transactions))


if __name__ == '__main__':
    main()