from src.text import common_words
import re

def wordlist(text):
    text = text.replace(",", " ")
    text = text.replace("\n", " ")
    words = text.split(" ")
    return words

def find_longest_word_length(text):
    words = wordlist(text)
    longest_word_length = 0
    for word in words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    return longest_word_length

def find_longest_words(text, length):
    longest_words = []
    words = wordlist(text)
    for word in words:
        if len(word) == length:
            longest_words.append(word)

    return longest_words

def letters_only(text):
    return "".join(
        char.lower()
        for char in text
        if char.isalpha() and char.isascii()
    )

def find_key(cipher, plain):
    key = ""

    for c, p in zip(cipher, plain):
        # with ord() every letter has a number. a = 97, b = 98, ...
        # chr() makes a number to a letter. 97 -> a, 98 -> b, ...
        shift = (ord(c) - ord("a") - (ord(p) - ord("a"))) % 26
        key += chr(ord("a") + shift)

    return key

def decrypt(cipher, key):
    result = []
    key_index = 0

    for char in cipher:
        if char.isascii() and char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord("a")

            value = (
                ord(char.lower()) - ord("a") - shift
            ) % 26

            result.append(chr(ord("a") + value))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)

def english_score(text):
    words_in_text = re.findall(r"[a-z]+", text.lower())

    score = 0

    for word in words_in_text:
        score += common_words.get(word, 0)

    return score