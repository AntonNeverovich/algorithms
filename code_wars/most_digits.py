def find_longest(arr):
    nd = [number_digits(n) for n in arr]
    s = dict(zip(arr, nd))
    m = [k for k, v in s.items() if v == max(s.values())]
    return m[0]


def number_digits(a: int):
    l = [int(i) for i in list(str(a))]
    return len(l)