import math

def decompose(n_str):
    arr = []
    for i in range(len(n_str)):
        arr.append(int(n_str[i]))

    return arr


def sum_array(arr):
    total_sum = 0
    for i in range(len(arr)):
        total_sum += arr[i]

    return total_sum

def main():
    curious = []
    for i in range(3, 1000000):
        decomposed = decompose(str(i))
        if i == sum_array([math.factorial(x) for x in decomposed]):
            curious.append(i)

    print curious

if __name__ == '__main__':
    main()