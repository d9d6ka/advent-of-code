clues = {}

with open("clues.txt", "r") as f:
    for line in f:
        if line.strip() != '':
            fact, _, val = line.strip().partition(':')
            clues[fact] = int(val.strip())

with open("input.txt", "r") as f:
    for line in f:
        if line.strip() != '':
            name, _, rest = line.strip().partition(":")
            _, number = name.split()
            facts = rest.strip().split(',')
            denominator = len(facts)
            numerator = 0
            for el in facts:
                fact, _, val = el.strip().partition(':')
                if clues[fact] == int(val.strip()):
                    numerator += 1
            if numerator == denominator:
                print("Part 1: {}".format(number))