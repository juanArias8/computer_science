basic_english = {
    'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15, 'f': 16, 'g': 17, 'h': 18,
    'i': 19, 'j': 20, 'k': 21, 'l': 22, 'm': 23, 'n': 24, 'o': 25, 'p': 26,
    'q': 27, 'r': 28, 's': 29, 't': 30, 'u': 31, 'v': 32, 'w': 33, 'x': 34,
    'y': 35, 'z': 36, ' ': 99
}


def reverse_alphabet(alphabet: dict) -> dict:
    new_keys, new_values = alphabet.values(), alphabet.keys()
    return dict(zip(new_keys, new_values))


def parser_text_to_big_number(text: str, alphabet: dict) -> str:
    big_number = [alphabet.get(key) for key in text]
    return ''.join(map(str, big_number))


def build_blocks_from_big_number(number: str, size: int) -> list:
    length = len(number)
    number_blocks = [number[i: i + size] for i in range(0, length, size)]
    return number_blocks


if __name__ == '__main__':
    text = 'hello world'
    big = parser_text_to_big_number(text, basic_english)
    print(build_blocks_from_big_number(big, 3))
