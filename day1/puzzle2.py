import fileinput


def main():

    sum_fuel = 0
    for line in fileinput.input():
        entry_fuel = (int(line) // 3) - 2
        rec_fuel = entry_fuel // 3 - 2
        while rec_fuel >= 1:
            entry_fuel += rec_fuel
            rec_fuel = rec_fuel // 3 - 2

        sum_fuel += entry_fuel

    print(sum_fuel)

if __name__ == '__main__':
    main()
