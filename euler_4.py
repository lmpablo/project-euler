def is_palindrome(n):
    num = str(n)
    if len(num) == 1:
        return True
    elif len(num) == 0:
        return True
    else:
        first = num[:1]
        last = num[-1:]

        if first == last:
            return True and is_palindrome(num[1:-1])
        else:
            return False

def main():
    max_val = float("-inf")
    for i in range(100,1000):
        for j in range(100, 1000):
            prod = i * j
            if is_palindrome(prod):
                if prod > max_val:
                    max_val = prod
    print max_val

if __name__ == '__main__':
    main()