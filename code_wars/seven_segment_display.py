def segment_display(num):
    l = number_to_list(num)
    s = [''] * 9

    if num == 0:
        for i in range(len(s)):
            for j in range(len(l) - 1):
                s[i] += "|       "
            s[i] += '|' + digits[i][l[len(l) - 1]]
    else:
        for i in range(len(s)):
            for j in range(len(l)):
                if l[j] is None:
                    s[i] += "|       "
                else:
                    s[i] += '|' + digits[i][l[j]]

    res = ''
    for i in range(len(s) - 1):
        res += s[i] + '|\n'
    res += s[len(s) - 1] + '|'
    return res


def number_to_list(num: int):
    n = [int(i) for i in str(num)]
    if len(n) < 6:
        while len(n) < 6:
            n.insert(0, None)
    return n


digits = []
digits.append(['  ###  ', '       ', '  ###  ', '  ###  ', '       ', '  ###  ', '  ###  ', '  ###  ', '  ###  ', '  ###  '])
digits.append([' #   # ', '     # ', '     # ', '     # ', ' #   # ', ' #     ', ' #     ', '     # ', ' #   # ', ' #   # '])
digits.append([' #   # ', '     # ', '     # ', '     # ', ' #   # ', ' #     ', ' #     ', '     # ', ' #   # ', ' #   # '])
digits.append([' #   # ', '     # ', '     # ', '     # ', ' #   # ', ' #     ', ' #     ', '     # ', ' #   # ', ' #   # '])
digits.append(['       ', '       ', '  ###  ', '  ###  ', '  ###  ', '  ###  ', '  ###  ', '       ', '  ###  ', '  ###  '])
digits.append([' #   # ', '     # ', ' #     ', '     # ', '     # ', '     # ', ' #   # ', '     # ', ' #   # ', '     # '])
digits.append([' #   # ', '     # ', ' #     ', '     # ', '     # ', '     # ', ' #   # ', '     # ', ' #   # ', '     # '])
digits.append([' #   # ', '     # ', ' #     ', '     # ', '     # ', '     # ', ' #   # ', '     # ', ' #   # ', '     # '])
digits.append(['  ###  ', '       ', '  ###  ', '  ###  ', '       ', '  ###  ', '  ###  ', '       ', '  ###  ', '  ###  '])
