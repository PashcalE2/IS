"""
https://habr.com/ru/articles/335906/
"""


def extended_euclidean_algorithm(a, b):
    """
    Возвращает кортеж из трёх элементов (gcd, x, y), такой, что
    a * x + b * y == gcd, где gcd - наибольший
    общий делитель a и b.

    В этой функции реализуется расширенный алгоритм
    Евклида и в худшем случае она выполняется O(log b).
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def inverse(n, p):
    """
    Возвращает обратную величину
    n по модулю p.

    Эта функция возвращает такое целое число m, при котором
    (n * m) % p == 1.
    """
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Или n равно 0, или p не является простым.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p


_p = 751


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        if self == other:
            return self.double()

        m = ((other.y - self.y) * inverse(other.x - self.x, _p)) % _p
        x = (m * m - self.x - other.x) % _p
        y = (-self.y - m * (x - self.x)) % _p

        return Point(x, y)

    def double(self):
        m = ((3 * (self.x ** 2) - 1) * inverse(2 * self.y, _p)) % _p
        x = (m * m - 2 * self.x) % _p
        y = (-self.y - m * (x - self.x)) % _p

        return Point(x, y)

    def mul(self, n: int):
        P = self
        nP = None

        while n > 0:
            if n % 2 == 1:
                if nP is None:
                    nP = P
                else:
                    nP = nP + P

            P = P.double()

            n >>= 1

        return nP

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()
