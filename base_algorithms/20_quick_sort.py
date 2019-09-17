# quick sort Hoar
import random as rnd


def split1(a, x):
    """Splitting an array by element"""
    j = 0
    n = len(a)
    for i in range(n):
        if a[i] < x:
            a[j], a[i] = a[i], a[j]
            j += 1


def split2(a, m, n, x):
    """Splitting an array area by element
        n, m - array bounds
    """
    j = 1
    for i in range(m, n):
        if a[i] < x:
            a[j], a[i] = a[i], a[j]
            j += 1
    return j


def quick_sort(a, m, n):
    if n == 1:
        x = rnd.randint(m, n)
        r = split2(a, m, n, x)
        quick_sort(a, m, r-1)
        quick_sort(a, r, n)
