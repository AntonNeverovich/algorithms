# exponentiation: given an integer a and a positive integer n,
# it is necessary to calculate a to the power of n

# option 1
print "option 1"
print 'input a'
a = input()
print 'input n'
n = input()
print 'input values: a = {0}, n = {1}'.format(a, n)


# exponentiation' algorithm
def exp1(a, n):
    b = 1  # such that b = a ** n
    for i in range(n):
        b *= a
    return b


def check(a, n , r):
    return r == a ** n


print 'a ** n = {0}: {1}'.format(exp1(a, n), check(a, n, exp1(a, n)))