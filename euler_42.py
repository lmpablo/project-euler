def calculate_value(string):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = 0
    for i in range(len(string)):
        val = 1 + letters.index(string[i])
        value += val

    return value

def calculate_triangles(n):
    arr = []
    for i in range(n):
        tri_num = ((i ** 2) + i) / 2
        arr.append(tri_num)

    return arr


def main():
    file = open("words.txt")
    words = [x for x in file.read().split("\"") if (x != "" and x != ",")]

    triangle_words = []
    triangle_numbers = calculate_triangles(100)
    for word in words:
        value = calculate_value(word)
        if value in triangle_numbers:
            triangle_words.append(word)

    print len(triangle_words)

if __name__ == '__main__':
    main()