class Fraction:
    fr: str
    p: int
    q: int

    def __init__(self, fr: str):
        self.fr = fr
        self.p = int(self.read()[0])
        self.q = int(self.read()[1])

    def __str__(self):
        return f'{self.p}/{self.q}'

    def __repr__(self):
        return f'{self.p}/{self.q}'

    def read(self):
        if self.fr == '':
            return [0, 1]
        elif '/' in self.fr:
            res = self.fr.split('/')
            if len(res) == 1:
                return self.read(self.simplify())
            if len(res) == 2:
                return [int(x) for x in self.fr.split('/')]
        elif '.' in self.fr:
            y = 10 ** len(self.fr.split('.')[1])
            x = self.fr.split('.')[1]
            r = Fraction(f'{x}/{y}').simplify()
            return [r.p, r.q]
        else:
            return [self.fr, 1]

    def simplify(self):
        if len(self.same(self.factorization(self.p), self.factorization(self.q))) == 0:
            cd = 1  # common divisor
        else:
            cd = self.mult(self.same(self.factorization(self.p), self.factorization(self.q)))  # common divisor
        return Fraction(f'{self.p // cd}/{self.q // cd}')

    def factorization(self, n: int):
        dividers = []
        while n > 1:
            for i in self.primes(n + 1):
                if n % i == 0:
                    dividers.append(i)
            n //= self.mult(dividers)
        return sorted(dividers)

    def primes(self, n):
        sieve = [True] * n
        for i in range(3, int(n ** 0.5) + 1, 2):
            if sieve[i]:
                sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
        return [2] + [i for i in range(3, n, 2) if sieve[i]]

    def mult(self, l: []):
        m = 1
        for i in l:
            m *= i
        return m

    def same(self, list1: [], list2: []):
        if len(list1) == len(list2) == 1:
            min_l = list1 if list1[0] < list2[0] else list2
            max_l = list1 if list1[0] > list2[0] else list2
        elif len(list1) == len(list2):
            min_l = list1
            max_l = list2
        else:
            min_l = list1 if len(list1) < len(list2) else list2
            max_l = list1 if len(list1) > len(list2) else list2
        res = []
        for i in min_l:
            if i in max_l:
                res.append(i)
        return res

    def __add__(self, other):
        if self.q == other.q:
            x = self.p + other.p
            y = self.q
        else:
            x = self.p * other.q + other.p * self.q
            y = self.q * other.q
        return Fraction(f'{x}/{y}').simplify()

    def __sub__(self, other):
        if self.q == other.q:
            x = self.p - other.p
            y = self.q
        else:
            x = self.p * other.q - other.p * self.q
            y = self.q * other.q
        return Fraction(f'{x}/{y}').simplify()

    def __mul__(self, other):
        x = self.p * other.p
        y = self.q * other.q
        return Fraction(f'{x}/{y}').simplify()

    def __div__(self, other):
        x = self.p * other.q
        y = self.q * other.p
        return Fraction(f'{x}/{y}').simplify()

    def __float__(self):
        return float(self.p) / float(self.q)


def decompose(n):
    fr = Fraction(n).simplify()
    if fr.q == 1:
        if fr.p == 0:
            return []
        else:
            return [str(fr.p)]
    else:
        res = []
        while fr.p != 1:
            res.append(egyptian_fractions(fr))
            fr = fr.dif_(egyptian_fractions(fr)).simplify()
        res.append(fr)
        return [str(e) for e in res]


def egyptian_fractions(fr):
    x = fr.p
    y = fr.q
    return Fraction(f'1/{int(y / x) + 1}')