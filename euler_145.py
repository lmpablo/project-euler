def is_all_odd(n):
    if n == 0:
        return False
    elif n % 2 == 0:
        if n <= 10:
            return False
        else:
            return False and is_all_odd((n - (n % 10)) / 10)
    else:
        if n < 10:
            return True
        else:
            return True and is_all_odd((n - (n % 10)) / 10)


def reverse(n):
    temp = str(n)[::-1]
    return temp


def main():
    count = 0
    i = 0

    while i < 1000000000:
        i += 1
        
        if i % 10 == 0:
            continue
        else:
            first = int(str(i)[:1])
            last = i % 10

            if (first + last) % 2 == 0:
                continue
        reversed = int(reverse(i))
        sum_val = reversed + i


        if sum_val % 2 == 0:
            continue
        elif is_all_odd(sum_val):
            count += 1

    print count

if __name__ == '__main__':
    main()