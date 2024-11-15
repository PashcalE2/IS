import random


_switch_table = [
    [9, 6, 3, 2, 8, 11, 1, 7, 10, 4, 14, 15, 12, 0, 13, 5],
    [3, 7, 14, 9, 8, 10, 15, 0, 5, 2, 6, 12, 11, 4, 13, 1],
    [14, 4, 6, 2, 11, 3, 13, 8, 12, 15, 5, 10, 0, 7, 1, 9],
    [14, 7, 10, 12, 13, 1, 3, 9, 0, 2, 11, 4, 15, 8, 5, 6],
    [11, 5, 1, 9, 8, 13, 15, 0, 14, 4, 2, 3, 12, 7, 10, 6],
    [3, 10, 13, 12, 1, 2, 0, 11, 7, 5, 9, 4, 8, 15, 14, 6],
    [1, 13, 2, 9, 7, 10, 6, 0, 8, 12, 4, 5, 15, 3, 11, 14],
    [11, 10, 15, 5, 0, 12, 14, 8, 6, 2, 3, 9, 1, 7, 13, 4]
]


def gost_main_block(N: int, K: int) -> int:
    A = N & 0xFFFFFFFF
    B = (N >> 32) & 0xFFFFFFFF

    new_B = A
    new_A = A ^ K
    S = [(new_A >> i * 4) & 15 for i in range(8)]
    for i, s in enumerate(S):
        S[i] = _switch_table[i][s]

    new_A = 0
    for i in range(1, 9):
        new_A = (new_A << 4) + S[-i]

    new_A = ((new_A << 11) & 0xFFFFFFFF_FFFFFFFF) + (new_A >> 21)
    new_A = B ^ new_A

    return (new_B << 32) + new_A


def gost_ofb(file_data: bytes, K: list[int], IV: int) -> bytes:
    if len(file_data) & 7 != 0:
        file_data = file_data + (b' ' * (8 - (len(file_data) & 7)))

    iters_count = len(file_data) // 8

    T = IV
    result = []
    for i in range(iters_count):
        T = gost_main_block(T, K[i % len(K)])
        text_block = int.from_bytes(file_data[i * 8:i * 8 + 8])
        result.append(int.to_bytes(T ^ text_block, 8))

    return b''.join(result)


def lab4(input_file: str, encrypted_file: str, decrypted_file: str, K: list[int], IV: int):
    with open(input_file, "r", encoding="UTF-8") as file:
        input_data = file.read()

    encrypted = gost_ofb(bytes(input_data, "UTF-8"), K, IV)
    with open(encrypted_file, "wb") as file:
        file.write(encrypted)

    decrypted = gost_ofb(encrypted, K, IV)
    with open(decrypted_file, "wb") as file:
        file.write(decrypted)


if __name__ == "__main__":
    """
    Реализовать систему симметричного блочного шифрования,
    позволяющую шифровать и дешифровать файл на диске с использованием
    заданного блочного шифра в заданном режиме шифрования. Перечень
    блочных шифров и режимов шифрования приведен в таблице. Номер
    шифра и режима для реализации получить у преподавателя.
    
    Вариант 10
    Алгоритм шифрования: ГОСТ 28147-89
    Режим шифрования: OFB
    """

    _K = [random.randint(0, (2 ** 32) - 1) for i in range(8)]
    _IV = random.randint(0, (2 ** 64) - 1)

    lab4("input.txt", "encrypted.txt", "decrypted.txt", _K, _IV)
