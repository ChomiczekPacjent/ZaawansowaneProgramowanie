import re


def is_palindrome(text: str) -> bool:
    cleaned = text.replace(' ', '').lower()
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError('n nie może być ujemne')
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def count_vowels(text: str) -> int:
    vowels = 'aeiouyąęó'
    return sum(1 for char in text.lower() if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError('Zniżka musi być w zakresie 0-1')
    return float(price * (1 - discount))


def flatten_list(nested_list: list) -> list:
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def word_frequencies(text: str) -> dict:
    frequencies = {}
    for word in re.findall(r'\w+', text.lower()):
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True
