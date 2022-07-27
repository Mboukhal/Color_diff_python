#!/usr/bin/env python3

"""

    change strings before index in infile
    in this case upper all strings tha 
    before '='

"""

index = '='
infile = 'colors_lower.py'
outfile = 'colors.py'

with open(infile, 'r') as f:
    x = f.read()

x = x.split(' ')

i = 0

res = []
r = ''
for s in x:
    if s == index:
        # instraction to do for str
        r = r.upper()
    if i > 0:
        res.append(r)
    i += 1
    r = s

res = ' '.join(res)
with open(outfile, 'w') as f:
    f.write(res)