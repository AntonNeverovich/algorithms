def persistence(n):
    if n < 10:
        return 0
    else:
        count = 1
        mult_of_digits = multiply(get_digits(n))
        while mult_of_digits >= 10:
            count += 1
            mult_of_digits = multiply(get_digits(mult_of_digits))
        return count


def get_digits(n: int):
    return [int(i) for i in str(n)]


def multiply(l: list):
    mul = 1
    for i in l:
        mul *= i
    return mul
