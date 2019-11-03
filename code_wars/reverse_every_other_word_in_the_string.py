def reverse_alternate1(string):
    if len(string) == 0:
        return ''
    l = string.split()
    for i in range(1, len(l), 2):
        if l[i].isalpha():
            l[i] = reverse(l[i])
        else:
            pm = get_punctuation_mark(l[i])
            print(pm)
            l[i] = l[i].replace(pm, '')
            l[i] = reverse(l[i]) + pm
    return ' '.join(l)


def reverse_alternate(string):
    if len(string) == 0:
        return ''
    l = string.split()
    for i in range(1, len(l), 2):
        l[i] = reverse(l[i])
    return ' '.join(l)


def reverse(string: str):
    l = [s for s in string]
    l.reverse()
    return ''.join(l)


def get_punctuation_mark(string: str):
    mark = ''
    for s in string:
        if not s.isalpha():
            mark += s
    return mark


print(reverse_alternate('Did it work?'))
print(reverse_alternate("I really... hope it% works this time..."))
print(reverse_alternate("Reverse this string, please!"))
