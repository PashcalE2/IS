import pandas as pd


class Alphabet:
    def __init__(
            self,
            first_lower_ord: int,
            first_upper_ord: int,
            size: int
    ):
        self.first_lower_ord = first_lower_ord
        self.first_upper_ord = first_upper_ord
        self.size = size

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


class CaesarMethod:
    def __init__(self, alphabets: list[Alphabet]):
        self.alphabets = alphabets

    def rotate(self, s: str, n: int) -> str:
        result = ""
        for char in s:
            not_rotated = True
            for alphabet in self.alphabets:
                if alphabet.is_lower(char):
                    new_ord = (ord(char) - alphabet.first_lower_ord + n) % alphabet.size
                    result += alphabet.lowers[new_ord]
                    not_rotated = False
                    break
                elif alphabet.is_upper(char):
                    new_ord = (ord(char) - alphabet.first_upper_ord + n) % alphabet.size
                    result += alphabet.uppers[new_ord]
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


def freq_analysis(encrypted: str) -> dict:
    chars_freq = {}
    for i in range(len(encrypted)):
        char = encrypted[i].lower()
        if _caesar_method.in_alphabet(char):
            if char in chars_freq:
                chars_freq[char] += 1
            else:
                chars_freq[char] = 1

    return chars_freq


def find_key_words(text: str, key_words: list[str]):
    result = []
    for word in key_words:
        if word.lower() in text.lower():
            result.append(word)
    return result


def hack_caesar(
        caesar_method: CaesarMethod,
        encrypted: str,
        key_words: list[str],
        max_rotations: int) -> str:
    acceptable_key_words_count = len(key_words) // 2

    for n in range(1, max_rotations):
        rotation = -n
        print(f"Сдвиг на: {rotation}")

        decrypted = caesar_method.rotate(encrypted, rotation)

        chars_freq = freq_analysis(decrypted)
        df = pd.DataFrame(
            data=[[
                key,
                chars_freq[key],
                chars_freq[key] / sum(chars_freq.values())
            ] for key in chars_freq],
            columns=["Буква", "Количество", "Вероятность"])
        df = df.sort_values("Буква")
        print(df)

        found_key_words = find_key_words(decrypted, key_words)
        found_key_words_count = len(found_key_words)
        print(f"Найденные ключевые слова ({found_key_words_count}): {found_key_words}\n")

        if found_key_words_count >= acceptable_key_words_count:
            return decrypted


_RU = Alphabet(
    first_lower_ord=ord("а"),
    first_upper_ord=ord("А"),
    size=ord("я") - ord("а") + 1)

_EN = Alphabet(
    first_lower_ord=ord("a"),
    first_upper_ord=ord("A"),
    size=ord("z") - ord("a") + 1)

_caesar_method = CaesarMethod([_RU, _EN])

_RU_key_words = ["и", "в", "то", "том", "на", "из", "под", "нам", "вам"]
_EN_key_words = ["and", "in", "that", "on", "from", "of", "the", "a", "you", "we"]

_key_words = _RU_key_words + _EN_key_words
_max_rotations = max(_EN.size, _RU.size)


def lab1(filepath: str, rotates_count: int):
    with open(filepath, "r", encoding="UTF-8") as file:
        filedata = file.read()

    def get_part_from_text(text: str):
        count = min(200, max(len(encrypted) // 2, 1000))
        return text[:count // 2] + "\n...\n" + text[-count // 2:]

    encrypted = _caesar_method.rotate(filedata, rotates_count)
    print(f"Зашифрованный текст:\n{get_part_from_text(encrypted)}")
    with open("./encrypted.txt", "w", encoding="UTF-8") as file:
        file.write(encrypted)

    decrypted = hack_caesar(_caesar_method, encrypted, _key_words, _max_rotations)
    print(f"Расшифрованный текст:\n{get_part_from_text(decrypted)}")
    with open("./decrypted.txt", "w", encoding="UTF-8") as file:
        file.write(decrypted)


if __name__ == "__main__":
    """
    Вариант 10:
    
    Реализовать в программе шифрование и дешифрацию
    содержимого файла по методу Цезаря. Провести частотный анализ
    зашифрованного файла, осуществляя проверку по файлу с набором
    ключевых слов.
    """

    lab1("./input.txt", 5)
