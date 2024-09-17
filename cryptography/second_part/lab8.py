"""
P = (78, 480)

147P = 1P + 2P + 16P + 128P = (463, 15)

1P = (78, 480)

2P = (440, 212)

16P = (406, 354)

128P = (16, 416)
"""

from utils import Point


def lab8(Px: int, Py: int, n: int) -> Point:
    P = Point(Px, Py)
    print(f"P = {P}")

    Ps = []
    nP = None
    nPs = []

    N = 0
    base = 1
    i = 0
    while n > 0:
        if n % 2 == 1:
            if nP is None:
                nP = P
            else:
                nP = nP + P

            N += base
            nPs.append({"n": N, "nP": nP})
            Ps.append({"pow": i, "P": P})

        P = P.double()

        n >>= 1
        base <<= 1
        i += 1

    print(f"{nPs[-1]["n"]}P = {" + ".join([f"{2 ** v["pow"]}P" for v in Ps])} = {nP}")
    for v in Ps:
        print(f"{2 ** v["pow"]}P = {v["P"]}")

    return nP


if __name__ == "__main__":
    """
    E_751 (-1, 1) <=> y^2 = x^3 - x + 1 (mod 751)
    
    Вариант 10:
    
    P = (78, 480)
    n = 147
    """

    result = lab8(78, 480, 147)
