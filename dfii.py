#!/usr/bin/env python3

"""
		Color diff 0.1
"""

GREEN = '\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

def color_diff(s1, s2):
    i = 0
    len1 = len(s1)
    len2 = len(s2)
    li = {
        'shurt' : '',
        'long' : '',
        's' : 0,
        'l' : 0,
        'cs' : 0,
        'cl' : 0
        }
    if len1 < len2:
        li['shurt'] = s1
        li['long'] = s2
        li['cs'] = len1
        li['cl'] = len2
        len_t = len2
    else:
        li['shurt'] = s2
        li['long'] = s1
        li['cs'] = len2
        li['cl'] = len1
        len_t = len1
    # print (len_t)

    while len_t > i + 1:
        if li['long'][li['l']] != li['shurt'][li['s']] \
            and li['s'] < li['cs'] and li['l'] < li['cl']:
            str1 = f'[{RED}'
            str2 = f'{NC}/{GREEN}'
            while li['s'] < li['cs'] and li['l'] < li['cl'] \
                and li['long'][li['l']] != li['shurt'][li['s']]: 
                str1 += li['long'][li['l']]
                str2 += li['shurt'][li['s']]
                li['s'] += 1
                li['l'] += 1
                i += 1
            if li['s'] < li['cs'] and li['l'] < li['cl']:
                str1 += li['long'][li['l']]
                str2 += li['shurt'][li['s']]
                li['s'] += 1
                li['l'] += 1
            str2 += f'{NC}]'
            str1 += str2
            print(str1, end='')
            # print(li['long'][li['l']], end='')
        else:
           if li['s'] < li['cs'] and li['l'] < li['cl']:
                print(li['long'][i], end='')
        li['s'] += 1
        li['l'] += 1
        i += 1
    if li['s'] < li['cs'] and li['l'] < li['cl']:
        print(li['long'][i], end='')
    print()
'''        str += x[i]
        if s1[i] != s2[i]:
            str += RED
            #while  lenx >= i and (s1[i] != s2[i]):
             #   i += 1
            str += END
'''
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

color_diff(r1, r2)
# print()
# print()
# color_diff(s1, s2)