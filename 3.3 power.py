import numpy as np


arr = [8, 2, 5, 1, 9]
np_arr = np.array(arr)


def main():
    print(f'Array: {" ".join(map(str, arr))}')
    powers = np.power(np_arr, 2)
    print(f'2nd power: {" ".join(map(str, powers))}')
    

if __name__ == '__main__':
    main()