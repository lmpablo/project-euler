def calculate_value(string):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = 0
    for i in range(len(string)):
        val = 1 + letters.index(string[i])
        value += val

    return value


def main():
    file = open("names.txt")
    names = [x for x in file.read().split("\"") if (x != "" and x != ",")] 

    names = sorted(names)

    final_scores = []
    for name in names:
        value = calculate_value(name)
        pos = names.index(name) + 1
        final_scores.append(value * pos)

    print sum(final_scores)

if __name__ == '__main__':
    main()