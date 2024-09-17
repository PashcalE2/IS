import math


def lab1(N: int, e: int, C: str):
    n = int(math.sqrt(N) + 1)
    print(f"n = int(sqrt({N})) + 1 = {n}")

    i = 0
    while True:
        i += 1
        t = n + i
        w = t ** 2 - N

        sqrt_w = int(math.sqrt(w))
        if sqrt_w ** 2 == w:
            sqrt_w = int(sqrt_w)
            break

    p = t + sqrt_w
    print(f"p = {t} + {sqrt_w} = {p}")

    q = t - sqrt_w
    print(f"q = {t} - {sqrt_w} = {q}")

    phi = round((p - 1) * (q - 1))
    print(f"Phi(N) = ({p - 1}) * ({q - 1}) = {phi}")

    d = pow(e, -1, phi)
    print(f"d = {e}^(-1) mod {phi} = {d}", "\n")

    message = ""
    for i, c in enumerate(C.split()):
        m = pow(int(c), d, N)
        part = m.to_bytes(4, byteorder='big').decode('cp1251')
        print(f'm{i} = C[{i}]^d mod N = {c}^{d} mod {N} = {m} => text({m}) = {part}')
        message += part

    print(f"message = {message}")


if __name__ == "__main__":
    """
    Вариант 10
    """

    _N = 77027476849549
    _e = 2936957
    _C = """
    18937689886043
    6667195679130
    53238895771820
    6189192838687
    48623327840257
    47264919314001
    42510070950746
    16878504505970
    22744978157662
    23644842894223
    """

    lab1(_N, _e, _C)
