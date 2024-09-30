"""
kG = (384, 276)

r = 384 % 13 = 7

z = (11^-1) % 13 = 6

s = (6 * (3 + 3 * 7)) % 13 = 1

r, s = (7, 1)
"""


from utils import inverse, Point


_G = Point(416, 55)
_n = 13


def lab9(e: int, d: int, k: int):
    kG = _G.mul(k)
    print(f"kG = {kG}")

    r = kG.x % _n
    print(f"r = {kG.x} % {_n} = {r}")

    z = inverse(k, _n)
    print(f"z = ({k}^-1) % {_n} = {z}")

    s = (z * (e + d * r)) % _n
    print(f"s = ({z} * ({e} + {d} * {r})) % {_n} = {s}")

    print(f"r, s = ({r}, {s})")

    return r, s


if __name__ == "__main__":
    """
    E_751 (-1, 1) <=> y^2 = x^3 - x + 1 (mod 751)
    G = (416, 55)
    n = 13
    
    Вариант 10:

    e = 3
    d = 3
    k = 11
    """

    result = lab9(3, 3, 11)
