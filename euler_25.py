from BigNumber import *

def main():
    curr_term = BigNumber("1")
    last = BigNumber("1")

    term = 3
    while True:
        temp = BigNumber(curr_term.ToString())
        curr_term.Add(last.ToString())
        digit_length = len(curr_term.digits)

        if digit_length == 1000:
            print term
            break

        last = temp
        term += 1

if __name__ == '__main__':
    main()