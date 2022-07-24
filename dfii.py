#!/usr/bin/env python3

"""
		Color diff 0.1
"""

GREEN = '\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

def my_split(s):
    x = []
    i = 0
    slen = len(s)
    # print (slen)
    while i < slen:
        x.append(s[i])
        i += 1
    return x

def rev_str(s):
    ns = ''
    slen = len(s) - 1
    while slen > 0:
        ns += s[slen]
        slen -= 1
    ns += s[slen]
    return ns

def check_str(s1, s2):
    i = 0
    x1 = my_split(s1)
    x2 = my_split(s2)
    len1 = len(x1)
    len2 = len(x2)
    str_res_start = ''
    str_res_end = ''
    while  len1 > i and len2 > i:
        if x1[i] == x2[i]:
            str_res_start += x1[i]
        i += 1
    len1 -= 1
    len2 -= 1
    while  x1[len1] == x2[len2]:
        str_res_end += x1[len1]
        # print (x1[len1], len1, len2)
        len1 -= 1
        len2 -= 1
    # print (s1, s2)
    str_res_end = rev_str(str_res_end)
    # print ()
    # print ("start", str_res_start, str_res_end)
    return str_res_start, str_res_end

def color_diff(s1, s2):
    i = 0
    i1 = 0
    i2 = 0
    x1 = s1.split(' ')
    x2 = s2.split(' ')
    str_res = ''
    start = ''
    end = ''
    len1 = len(x1)
    len2 = len(x2)
    while  len1 > i and len2 > i:
        if x1[i] == x2[i]:
            str_res += x1[i] + ' '
        else:
            # x1[i], x2[i] = 
            n_start, n_end = check_str(x1[i], x2[i])
            # while x1[i][i1] == x2[i][i1]:
            #     start += x1[i][i1]
            #     i1 += 1
            # i2 = len(x1[i]) - 1
            # while x1[i][i2] == x2[i][i2]:
            #     end += x1[i][i2]
            #     i2 -= 1
            str_res += f'[{RED}{x1[i]}{NC}/{GREEN}{x2[i]}{NC}]' + ' '
        
        i += 1
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