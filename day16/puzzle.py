import fileinput


def pattern(step: int, length: int):
    changer = []
    y = 0
    while y <= length:
        for x in range(step):
            changer.append(0)
            y += 1
        for x in range(step):
            changer.append(1)
            y += 1
        for x in range(step):
            changer.append(0)
            y += 1
        for x in range(step):
            changer.append(-1)
            y += 1

    first_dig = changer[0]
    changer.pop(0)
    changer.append(first_dig)

    return changer


def phase(pattern, num_list, length):
    sum = []
    for x in range(length):
        sum.append(pattern[x]*num_list[x])
    return sum


def main():
    num_str = '12345678'
    num_list = [int(i) for i in num_str]

    for x in range(101):
        y = 0
        while y < len(num_list):
            transformer = pattern(y + 1, len(num_list))
            num_list = phase(transformer, num_list, len(num_list))
            y += 1
    print(num_list)


if __name__ == '__main__':
    main()
