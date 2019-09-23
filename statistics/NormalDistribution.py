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
