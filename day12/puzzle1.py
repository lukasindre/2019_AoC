from math import gcd

def find_velocity(list1: list, list2: list, list3: list, list4: list):
    for x in range(3):
        if list1[x] > list2[x]:
            list1[x + 3] -= 1
            list2[x + 3] += 1
        elif list1[x] < list2[x]:
            list1[x + 3] += 1
            list2[x + 3] -= 1
        else:
            pass

        if list1[x] > list3[x]:
            list1[x + 3] -= 1
            list3[x + 3] += 1
        elif list1[x] < list3[x]:
            list1[x + 3] += 1
            list3[x + 3] -= 1
        else:
            pass

        if list1[x] > list4[x]:
            list1[x + 3] -= 1
            list4[x + 3] += 1
        elif list1[x] < list4[x]:
            list1[x + 3] += 1
            list4[x + 3] -= 1
        else:
            pass

        if list2[x] > list3[x]:
            list2[x + 3] -= 1
            list3[x + 3] += 1
        elif list2[x] < list3[x]:
            list2[x + 3] += 1
            list3[x + 3] -= 1
        else:
            pass

        if list2[x] > list4[x]:
            list2[x + 3] -= 1
            list4[x + 3] += 1
        elif list2[x] < list4[x]:
            list2[x + 3] += 1
            list4[x + 3] -= 1
        else:
            pass

        if list3[x] > list4[x]:
            list3[x + 3] -= 1
            list4[x + 3] += 1
        elif list3[x] < list4[x]:
            list3[x + 3] += 1
            list4[x + 3] -= 1
        else:
            pass

    return [list1, list2, list3, list4]


def find_energy(moon):
    potential = abs(moon[0]) + abs(moon[1]) + abs(moon[2])
    kinetic = abs(moon[3]) + abs(moon[4]) + abs(moon[5])
    return potential * kinetic

def main():
    moon_Io = [1, 2, -9, 0, 0, 0]
    moon_Europa = [-1, -9, -4, 0, 0, 0]
    moon_Ganymede = [17, 6, 8, 0, 0, 0]
    moon_Callisto = [12, 4, 2, 0, 0, 0]
    # moon_Io = [-1, 0, 2, 0, 0, 0]
    # moon_Europa = [2, -10, -7, 0, 0, 0]
    # moon_Ganymede = [4, -8, 8, 0, 0, 0]
    # moon_Callisto = [3, 5, -1, 0, 0, 0]


    states = set()

    for x in range(500_000):
        new_velocities = find_velocity(moon_Io, moon_Europa, moon_Ganymede, moon_Callisto)
        moon_Io = new_velocities[0]
        moon_Europa = new_velocities[1]
        moon_Ganymede = new_velocities[2]
        moon_Callisto = new_velocities[3]

        for i in range(3):
            moon_Io[i] += moon_Io[i+3]
            moon_Europa[i] += moon_Europa[i+3]
            moon_Ganymede[i] += moon_Ganymede[i+3]
            moon_Callisto[i] += moon_Callisto[i+3]
    # print(find_energy(moon_Io) + find_energy(moon_Europa) + find_energy(moon_Ganymede) + find_energy(moon_Callisto))

        axis = 2
        state = f"{moon_Io[axis]}, {moon_Europa[axis]}, {moon_Ganymede[axis]}, {moon_Callisto[axis]}, {moon_Io[axis+3]}, {moon_Europa[axis+3]}, {moon_Ganymede[axis+3]}, {moon_Callisto[axis+3]}"
        if x==0:
            print(f"{x}: {state}")
        if state in states:
            print(f"{x}: {state}")
            break
        else:
            states.add(state)
        # print(moon_Io[:3])
        # print(moon_Europa[:3])
        # print(moon_Ganymede[:3])
        # print(moon_Callisto[:3])
        # print()

# x repeats on 186028
# y repeats on 167624
# z repeats on 193052
# LCM = ###/GCD

    LCM1 = 186028*193052 // gcd(186028, 193052)
    LCM2 = 186028*167624 // gcd(186028,167624)

    LCM3 = LCM1*LCM2 // gcd(LCM1,LCM2)
    print(LCM3)


if __name__ == '__main__':
    main()
