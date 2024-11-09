import math


def lab1(N: int, e: int, C: str):
    print("Рассчет параметров")
    n = int(math.sqrt(N) + 1)
    print(f"n = int(sqrt({N})) + 1 = {n}")

    t = n
    while True:
        # Перебор t >= n
        t += 1
        sub = t ** 2 - N

        sqrt_sub = int(math.sqrt(sub))
        if sqrt_sub ** 2 == sub:
            break

    p = t + sqrt_sub
    print(f"p = {t} + {sqrt_sub} = {p}")

    q = t - sqrt_sub
    print(f"q = {t} - {sqrt_sub} = {q}")

    phi = round((p - 1) * (q - 1))
    print(f"ф(N) = {p - 1} * {q - 1} = {phi}")

    d = pow(e, -1, phi)
    print(f"d = {e}^(-1) mod {phi} = {d}")

    print("Дешифровка")
    result = ""
    for i, c in enumerate(C.split()):
        num_block = pow(int(c), d, N)
        print(f"num_block_{i} = {c}^{d} mod {N} = {num_block}")

        text_block = num_block.to_bytes(4, byteorder="big").decode("cp1251")
        print(f"text_block = {text_block}")

        result += text_block

    print(f"Результат = {result}")


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
    71614018816334
    24651499733229
    """

    lab1(_N, _e, _C)
