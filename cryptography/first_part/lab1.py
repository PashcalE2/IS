import pandas as pd


# TODO: частотный анализ


class Alphabet:
    def __init__(
            self,
            first_lower_ord: int,
            first_upper_ord: int,
            size: int,
            words_freq: dict[str, float]
    ):
        self.first_lower_ord = first_lower_ord
        self.first_upper_ord = first_upper_ord
        self.size = size
        self.words_freq = words_freq

        self.lowers = [chr(first_lower_ord + i) for i in range(size)]
        self.uppers = [chr(first_upper_ord + i) for i in range(size)]

    def is_lower(self, char: str) -> bool:
        return char[0] in self.lowers
    
    def to_lower(self, s: str) -> str:
        result = ""
        for char in s:
            if self.is_upper(char):
                result += self.lowers[ord(char) - self.first_upper_ord]
            else:
                result += char
        return result

    def is_upper(self, char: str) -> bool:
        return char[0] in self.uppers

    def in_alphabet(self, char: str) -> bool:
        return self.is_lower(char) or self.is_upper(char)


class Caesar:
    def __init__(self, alphabets: list[Alphabet]):
        self.alphabets = alphabets

    def rotate(self, s: str, n: int) -> str:
        result = ""
        for char in s:
            not_rotated = True
            for alphabet in self.alphabets:
                if alphabet.is_lower(char):
                    result += alphabet.lowers[(ord(char) - alphabet.first_lower_ord + n) % alphabet.size]
                    not_rotated = False
                    break
                elif alphabet.is_upper(char):
                    result += alphabet.uppers[(ord(char) - alphabet.first_upper_ord + n) % alphabet.size]
                    not_rotated = False
                    break

            if not_rotated:
                result += char

        return result

    def in_alphabet(self, char: str) -> bool:
        for alphabet in self.alphabets:
            if alphabet.in_alphabet(char):
                return True
        return False


# TODO: прочитать частоты из .csv
_RU = Alphabet(
    first_lower_ord=ord("а"),
    first_upper_ord=ord("А"),
    size=ord("я") - ord("а") + 1,
    words_freq={})

_EN = Alphabet(
    first_lower_ord=ord("a"),
    first_upper_ord=ord("A"),
    size=ord("z") - ord("a") + 1,
    words_freq={})

_caesar = Caesar([_RU, _EN])


def lab1(filepath: str, rotates_count: int):
    with open(filepath, "r", encoding="UTF-8") as file:
        filedata = file.read()

    encrypted = _caesar.rotate(filedata, rotates_count)
    with open("./output.txt", "w", encoding="UTF-8") as file:
        file.write(encrypted)

    words_freq = {}
    left_border = None
    for i in range(len(encrypted)):
        if _caesar.in_alphabet(encrypted[i]):
            if left_border is None:
                left_border = i
        elif left_border is not None:
            word = encrypted[left_border:i]
            left_border = None

            if word in words_freq:
                words_freq[word] += 1
            else:
                words_freq[word] = 1

    print(words_freq)


if __name__ == "__main__":
    """
    Вариант 10:
    
    Реализовать в программе шифрование и дешифрацию
    содержимого файла по методу Цезаря. Провести частотный анализ
    зашифрованного файла, осуществляя проверку по файлу с набором
    ключевых слов.
    """

    lab1("./input.txt", 5)
