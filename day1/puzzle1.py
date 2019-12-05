import fileinput
import math

def main():
    sum_fuel = 0
    for line in fileinput.input():




        sum_fuel += (int(line) // 3) - 2


    print(sum_fuel)

if __name__ == '__main__':
    main()
