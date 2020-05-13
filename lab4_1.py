#Task 1

import string
from string import punctuation, whitespace


file = 'pnp.txt'

with open(file, 'r') as header:
    chops = header.read().split()

#print(chops)


def formatted(chop):
    initial = ""
    for charecter in chop:
        if ((charecter in punctuation) or (charecter in whitespace) or (charecter in '\n')):
            pass
        else:
            initial += charecter.lower()
    print(initial)


print([formatted(chop) for chop in chops])
