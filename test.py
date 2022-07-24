#!/usr/bin/env python3

from diff import py_diff
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
token (|echo|, 1)
token (|\-\n|, 6)
token (| |, 6)
token (|;|, 3)
token (|echo|, 1)
token (|\\\\\$USER|, 4)
token (|/Users/piola/Desktop/parsing 2|, 8)
cmd(3, [echo -nnnsdkfghsdkfjghnnnnn -77nnnkljptrtfnnn88 hello world;             echo '\-\n' '\h\e\l\l\o'; echo \\\\\\\\\\\$USER  $PWD])
'''
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
r1 = 'hi slilo ok/Users/piola/lilo/parsing'
r2 = 'hi skaio ok/Users/piola/lilo/parsing'

diff1 = py_diff(r1, r2)
diff2 = py_diff(s1, s2)

print (diff1,'\n\n',diff2)