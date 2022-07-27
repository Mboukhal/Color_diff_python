#!/usr/bin/env python3

"""
    pyDiff 0.1
    made by kai/Mboukhal
"""

# from diffLine import diffLine
from colors import colors


def my_split(s):
    x = []
    i = 0
    slen = len(s)
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

def get_last(s, end):
    elen = len(end)

    print ('|'+s[:-elen]+'|', end)

def check_str(s1, s2):
    i = 0
    x1 = my_split(s1)
    x2 = my_split(s2)
    len1 = len(x1)
    len2 = len(x2)
    str_res_start = ''
    str_res_end = ''
    while x1[i] == x2[i]:
        str_res_start += x1[i]
        i += 1
    len1 -= 1
    len2 -= 1
    while  x1[len1] == x2[len2]:
        str_res_end += x1[len1]
        len1 -= 1
        len2 -= 1
    str_res_end = rev_str(str_res_end)
    slen = len(str_res_start) 
    elen = len(str_res_end)
    return str_res_start, str_res_end, s1[slen:-elen], s2[slen:-elen]

def diff(s1, s2):
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
            n_start, n_end, ss1, ss2 = check_str(x1[i], x2[i])
            # str_res += f'{n_start}{colors['YELLOW']}'
            # str_res += f'[{colors['NC']}{colors['RED']}{ss1}{colors['NC']}{colors['YELLOW']}'
            # str_res += f'/{colors['NC']}{colors['GREEN']}{ss2}{colors['NC']}{colors['YELLOW']}]'
            # str_res += f'{colors['NC']}{n_end}' + ' '
        i += 1
    # print(str_res)
    return str_res
# print (colors)
print (f'{colors.bg.YELLOW}OK{colors.NC}')
