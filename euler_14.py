def collatz(n):
    step = 1
    curr = n
    while(curr > 1):
        if curr % 2 == 0:
            curr = curr / 2
        else:
            curr = (3 * curr) + 1
        step += 1

    return step

def main():
    max_chain_size = float("-inf")
    max_num = -1

    for i in range(1000000):
        chain_size = collatz(i)
        if chain_size > max_chain_size:
            max_chain_size = chain_size
            max_num = i

    print max_num, max_chain_size

if __name__ == '__main__':
    main()