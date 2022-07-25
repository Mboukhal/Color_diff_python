"""
    diffLine 0.1
    made by kai/Mboukhal
"""

# from pyDiff import diff, diffLine

def diffLine(s1, s2):
    i = 0
    i1 = 0
    i2 = 0
    x1 = s1.split('\n')
    x2 = s2.split('\n')
    str_res = ''
    start = ''
    end = ''
    len1 = len(x1)
    len2 = len(x2)
    while  len1 > i and len2 > i:
        if x1[i] == x2[i]:
            str_res += '\t' + x1[i] + '|'
        else:
            str_res += '\n' + '>>\t' + x1[i] + '|'
            str_res += '\n' + '>>\t' + x2[i] + '|'
            # i += 1

            # n_start, n_end, ss1, ss2 = check_str(x1[i], x2[i])
            # str_res += f'{n_start}{YELLOW}[{NC}{RED}{ss1}{NC}{YELLOW}/{NC}{GREEN}{ss2}{NC}{YELLOW}]{NC}{n_end}' + '\n'
            # str_res += '_______________________' + '\n'
            # str_res += '\n' + f'{x1[i]}'
            # str_res += f'_______________________'+ '\n'
            # str_res += f'{x2[i]}' + '\n'
            # str_res += '_______________________' + '\n'
        i += 1
    print(f'{s1}\n\n\n{s2}')
    # print(str_res)
    return str_res