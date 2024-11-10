import random


def lab2(filepath: str, K: list[int], IV: int):
    with open(filepath, "r", encoding="UTF-8") as file:
        filedata = file.read()

    input_bytes = bytes(filedata, "UTF-8")
    input_bytes = input_bytes + (b' ' * (len(input_bytes) % 8))

    # блоки по 8 байт
    N = []
    for i in range(len(input_bytes) // 8):
        N.append(int.from_bytes(input_bytes[i * 8:i * 8 + 8]))

    




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

    lab2("input.txt", _K, _IV)
