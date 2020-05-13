# Task 2

import string
from string import punctuation, whitespace
from collections import Counter

file = 'pnp.txt'

with open(file, 'r') as header:
    chops = header.read().split()

counts = Counter(chops)
print(counts)


