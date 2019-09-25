import math as m


def z_value(x: float, mx: float, sd: float):
    return (x - mx) / sd


# integral function of the Laplace
def laplace_local_function(x: float, mx: float, sd: float):
    """
    Локальная функция Лапласа
    :param x: целевое занчение
    :param mx: медиана
    :param sd: Дисперсия
    """
    return alfa() * m.e ** (z_value(x, mx, sd))


def laplace_integral_function(x: float, mx: float, sd: float):
    """
    Функция Лапласа
    :param x: целевое занчение
    :param mx: медиана
    :param sd: Дисперсия
    """
    z = z_value(x, mx, sd)
    return alfa() * trapezoidal(0, z, 32)


def trapezoidal(a, b, n):
    """
    Вычисляет приближенное значение интеграла с помощью формулы трапеций
    :param a: - пределы интегрирования
    :param b: - пределы интегрирования
    :param n: - количество частичных отрезков
    """
    h = float(b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result


def alfa():
    return 1 / ((2 * m.pi) ** 0.5)


def f(z: float) -> float:
    return m.e ** (-1 * ((z ** 2) / 2))


def se(sdx: float, D: float, n: int):
    if n > 30:
        return sdx / (n ** 0.5)
    return (D / n) ** 0.5


def confidence_interval(x_mean: float, sd: float, n: int, accuracy=0.95) -> []:
    res = []
    se_ = se(sdx=sd, n=n, D=sd**0.5)
    ci = 0
    if accuracy == 0.95:
        ci = 1.96 * se_
    if accuracy == 0.99:
        ci = 2.58 * se_
    res.append(x_mean - ci)
    res.append(x_mean + ci)
    return res
