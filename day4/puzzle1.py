def main():

    repeat_check = False
    decrease_check = False
    counter = 0

    for x in range(145852,616942):
        num_str = str(x)
        digit_list = [int(i) for i in num_str]

        for entry in digit_list[:4]:
            if digit_list[entry] == digit_list[entry + 1]:
                repeat_check = True
                break

        for entry in digit_list[:4]:
            if digit_list[entry] <= digit_list[entry + 1]:
                decrease_check = True

        if repeat_check and decrease_check:
            counter += 1
    print(counter)



if __name__ == '__main__':
    main()
