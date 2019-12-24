#Copyright Chris Bowles, I had no idea how to do this, but wanted to see if i could do day 2, i could not 




import fileinput
import math
from typing import List, Dict, Tuple

reactions: Dict[str, Tuple[int, List[Tuple[int, str]]]] = {}


def make(tgt: str, needs: Dict[str, int]):
    qty = reactions[tgt][0]
    mult = math.ceil(needs.get(tgt, 0) / qty)
    ings = reactions[tgt][1]

    for ing in ings:
        needs[ing[1]] = needs.get(ing[1], 0) + (ing[0] * mult)

    needs[tgt] = needs.get(tgt, 0) - (qty * mult)


def main():
    needs: Dict[str, int] = {'FUEL': 1}

    for line in fileinput.input():
        line = line.rstrip().split(' => ')
        result = line[1].split(' ')

        inputs: List[Tuple[int, str]] = []

        ings = line[0].split(', ')
        for ing in ings:
            ing = ing.split(' ')
            inputs.append((int(ing[0]), ing[1]))

        reactions[result[1]] = (int(result[0]), inputs)

    while True:
        need = [need for need in needs if needs[need] > 0 and need != 'ORE']
        if len(need) > 0:
            make(need[0], needs)
        else:
            print(needs['ORE'])
            break


if __name__ == '__main__':
    main()
