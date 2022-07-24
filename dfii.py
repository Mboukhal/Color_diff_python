#!/usr/bin/env python3

"""
		Color diff 0.1
"""

GREEN = '\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

def color_diff(s1, s2):
    i = 0
    x1 = s1.split(' ')
    x2 = s2.split(' ')
    str_res = ''
    while len(x1) > i and len(x2) > i:
        if x1[i] == x2[i]:
            str_res += x1[i] + ' '
        else:
            str_res += f'[{RED}{x1[i]}{NC}/{GREEN}{x2[i]}{NC}]' + ' '
        
        i += 1
    # print (x1[1])
    # print (x2[1])
    print(str_res)

s1 = '''
token (|echo|, 0)
token (|-nsdkfghj|, 9)
token (| |, 9)
token (|hi|, 1)
token (| |, 1)
token (|;|, 3)
token (|echo|, 1)
token (|\-\n|, 6)
token (| |, 6)
token (|;|, 3)
token (|echo|, 1)
token (|\\\\\$USER|, 4)
token (|/Users/piola/Desktop/parsing 2|, 8)
cmd(3, [echo -nnnsdkfghsdkfjghnnnnn -77nnnkljptrtfnnn88 hello world;             echo '\-\n' '\h\e\l\l\o'; echo \\\\\\\\\\\$USER  $PWD])
'''
# print (s1)
s2 =  '''
token (|echo|, 0)
token (|-nsdkfghj|, 9)
token (| |, 9)
token (|hello|, 1)
token (| |, 1)
token (|;|, 3)
token (|echo|, 1)
token (|\-\n|, 6)
token (| |, 6)
token (|;|, 3)
token (|echo|, 1)
token (|\\\\\$USER|, 4)
token (|/Users/piola/lilo/parsing 2|, 8)
cmd(3, [echo -nnnsdkfghsdkfjghnnnnn -77nnnkljptrtfnnn88 hello world;             echo '\-\n' '\h\e\l\l\o'; echo \\\\\\\\\\\$USER  $PWD])
'''
r1 = 'hi lilo ok/Users/piola/lilo/parsing'
r2 = 'hi kaio ok/Users/piola/lilo/parsing'

# color_diff(r1, r2)
# print()
# print()
color_diff(s1, s2)