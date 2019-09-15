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
def exp1(basis, exp):
    b = 1  # such that b = basis ** exp
    for i in range(exp):
        b *= basis
    return b


def check(b, k, r):
    return r == b ** k


print 'a ** n = {0}: {1}'.format(exp1(a, n), check(a, n, exp1(a, n)))
