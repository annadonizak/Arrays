import numpy as np

# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]


def calculate_stock_value(prices, quantities):
    return round(sum(np.array(prices) * np.array(quantities)), 2)


def main():
    print(calculate_stock_value(product_prices, product_quantities))
    

if __name__ == '__main__':
    main()