from typing import List


def caesar_cipher_encode(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted_char
        else:
            result += char
    return result


def caesar_cipher_decode(text: str, shift: int) -> str:
    return caesar_cipher_encode(text, -shift)


def vigenere_cipher_encode(text: str, key: str) -> str:
    result = ""
    key_len = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') + ord(key[i % key_len]) - ord('a')) % 26 + ord('a'))
            result += shifted_char
        else:
            result += char
    return result


def vigenere_cipher_decode(text: str, key: str) -> str:
    result = ""
    key_len = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') - (ord(key[i % key_len]) - ord('a'))) % 26 + ord('a'))
            result += shifted_char
        else:
            result += char
    return result


def rail_fence_cipher_encode(text: str, rails: int) -> str:
    fence = [[None] * len(text) for _ in range(rails)]
    rail = 0
    for i in range(len(text)):
        fence[rail][i] = text[i]
        rail += 1
        if rail == rails:
            rail = 0
    result = ""
    for row in fence:
        result += "".join([char for char in row if char is not None])
    return result


def rail_fence_cipher_decode(text: str, rails: int) -> str:
    fence = [[None] * len(text) for _ in range(rails)]
    rail = 0
    for i in range(len(text)):
        fence[rail][i] = True
        rail += 1
        if rail == rails:
            rail = 0
    index = 0
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] is True:
                fence[i][j] = text[index]
                index += 1
    rail = 0
    result = ""
    for i in range(len(text)):
        result += fence[rail][i]
        rail += 1
        if rail == rails:
            rail = 0
    return result


def rot13_cipher_encode(text: str) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result += shifted_char
        else:
            result += char
    return result


def rot13_cipher_decode(text: str) -> str:
    return rot13_cipher_encode(text)

def example():
    print("congrats if you got this code working!")
