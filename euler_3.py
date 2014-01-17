def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False

    return True

def get_divisor(n):
    x = 2
    while (x <= n):
        if n % x == 0:
            return x

        x += 1

def main():
    num = 600851475143
    # num = 13195

    div = get_divisor(num)
    print div

    i = 2
    factors = []
    prime_factors = []
    while(i <= (num / div)):
        if num % i == 0:
            factors.append(i)

        i += 1

    for f in factors:
        if is_prime(f):
            prime_factors.append(f)

    print prime_factors


if __name__ == '__main__':
    main()