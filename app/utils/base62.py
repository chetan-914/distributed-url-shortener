ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(ALPHABET)

CHAR_TO_INDEX = {c: i for i, c in enumerate(ALPHABET)}


def encode(num: int) -> str:
    if num < 0:
        raise ValueError("Number must be non-negative")

    if num == 0:
        return ALPHABET[0]

    result = []

    while num > 0:
        num, rem = divmod(num, BASE)
        result.append(ALPHABET[rem])

    return "".join(reversed(result))


def decode(s: str) -> int:
    num = 0

    for char in s:
        if char not in CHAR_TO_INDEX:
            raise ValueError(f"Invalid Base62 character: {char}")
        num = num * BASE + CHAR_TO_INDEX[char]

    return num
