# recursive algorithm
def merge(a, b):
    i, j, = 0, 0
    n, m = len(a), len(b)
    c = []
    while i < n or j < m:
        if j == m or (i < n and a[i] <= b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c


def merge_down(a, b):
    i, j, = 0, 0
    n, m = len(a), len(b)
    c = []
    while i < n or j < m:
        if j == m or (i < n and a[i] >= b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c


def merge_sort(a):
    n = len(a)
    if n == 1:
        return a
    x = a[:(n/2) - 1]
    y = a[n/2:]
    x = merge_sort(x)
    y = merge_sort(y)
    return merge(x, y)
