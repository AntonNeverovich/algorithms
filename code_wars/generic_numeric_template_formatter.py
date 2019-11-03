def numeric_formatter(*template):
    s = template[0]
    n = template[1] if len(template) == 2 else '1234567890'
    res = []
    res.append(replace_letter_to_digit(s, n))

    return ' '.join(res)


def is_digit(s: str) -> bool:
    symb = ['+', '/', '-', '*']
    b = False
    for i in range(10):
        if s == str(i):
            b = True
    for i in range(len(symb)):
        if s == symb[i]:
            b = True
    return b


def replace_letter_to_digit(letters: str, digits: str):
    l = list(letters)
    d = list(digits)
    m = 0
    for k in range(len(l)):
        if l[k] == ' ' or is_digit(l[k]):
            continue
        if m % len(d) == 0:
            m = 0
        l[k] = d[m]
        m += 1
    return ''.join(l)
