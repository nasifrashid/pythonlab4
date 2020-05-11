# print("hello")
from string import punctuation, whitespace

fin = open('pnp.txt')
for line in fin:
    word = line.strip()
    print(word)


def strip(words):
    stripped = ''
    for char in words:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            stripped += char.lower()
    return stripped


print(word)
