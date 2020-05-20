"""
with the help from book solution
"""
def sed(pattern, replacement, readfile, writefile):
    try:
        r = open(readfile)
        w = open(writefile, 'w')
        a = 'a'
        text = ''
        while a != '':
            a = r.readline()
            text += a
        while pattern in text:
            p = text.find(pattern)
            text = text[:p] + replacement + text[p + len(pattern):]
        w.write(text)
        r.close()
        w.close()
    except:
        return 'error message'
