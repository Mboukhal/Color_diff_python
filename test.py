#!/usr/bin/env python3

from pyDiff import diff, diffLine
"""
    py_diff 0.1
    made by kai/Mboukhal
"""

s1 = '''
token (|echo|, 0)
token (|-nsdkfghj|, 9)
token (| |, 9)
token (|hi|, 1)
token (| |, 1)
token (|;|, 3)
token (|\-\|, 6)
token (|echo|, 1)
token (|;|, 3)
token (| |, 6)
token (|echo|, 1)
token (|\\\\\$USER|, 4)
token (|/Users/piola/Desktop/parsing 2|, 8)
cmd(3, [echo -nnnsdkfghsdkfjghnnnnn
'''
s2 =  '''
token (|echo|, 0)
token (|-nsdkfghj|, 9)
token (| |, 9)
token (|hello|, 1)
token (| |, 1)
token (|;|, 3)
token (|echo|, 1)
token (|\-\|, 6)
token (| |, 6)
token (|;|, 3)
token (|echo|, 1)
token (|\\\\\$USER|, 4)
token (|/Users/piola/lilo/parsing 2|, 8)
cmd(3, [echo -nnnsdkfghsdkfjghnnnnn
'''
r1 = 'hi slilo ok/Users/piola/lilo/parsing'
r2 = 'hi skaio ok/Users/piola/lilo/parsing'

l1 =  '''token 1111111111111
token 2222222222222
token 333333333333
token 333333333333
token 333333333333
token 2222222222222'''

l2 =  '''token 1111111111111
token 333333333333
token 2222222222222
token 333333333333
token 333333333333
token 2222222222222'''

# diff1 = diff(r1, r2)
# diff2 = diff(s1, s2)
line = lineDiff(s1, s2) 
# line1 = diffLine(l1, l2) 

# print (diff1,'\n\n',diff2)
print ('\n\n' + line)