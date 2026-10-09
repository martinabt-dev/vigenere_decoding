from src.text import cipher_text
from src.config import language, key_lengths, top_results
from src.functions import (
    find_longest_word_length,
    find_longest_words,
    letters_only,
    decrypt,
    find_key,
    english_score
)
from wordfreq import iter_wordlist
import re

def main():
    words = []
    length = find_longest_word_length(cipher_text)
    longest_words = find_longest_words(cipher_text, length)
    print(f"longest words: {longest_words}")

    for word in iter_wordlist(language):
        if len(word) == length and word.isalpha():
            words.append(word.lower())

    print(f"Number of words with {length} letters: {len(words)}")

    for cipher_word in longest_words:
        cipher_word_clean = letters_only(cipher_word)
        cipher_letters = letters_only(cipher_text)

        positions = [
            match.start()
            for match in re.finditer(
                re.escape(cipher_word_clean),
                cipher_letters
            )
        ]

        print(f"Gefundenes Geheimtext-Wort: {cipher_word_clean}")
        print(f"Position(en), ab 0 gezählt: {positions}")

        # Das erste Vorkommen verwenden
        word_position = positions[0]
        print(f"Verwendete Position: {word_position}")

        results = []

        for plain_word in words:

            full_key = find_key(cipher_word_clean, plain_word)

            for key_length in key_lengths:
                compatible = all(
                    full_key[i] == full_key[i + key_length]
                    for i in range(len(full_key) - key_length)
                )

                if not compatible:
                    continue

                key = "".join(
                    full_key[(i - word_position) % key_length]
                    for i in range(key_length)
                )

                decrypted = decrypt(cipher_text, key)

                score = english_score(decrypted)

                results.append(
                    (score, plain_word, key_length, key, decrypted)
                )

                results.sort(key=lambda result: result[0], reverse=True)

                print(f"\n{len(results)} passende Kandidaten gefunden.")

                for score, plain_word, key_length, key, decrypted in results[:top_results]:
                    print("\n" + "=" * 60)
                    print(f"Score:             {score}")
                    print(f"Vermutetes Wort:   {plain_word}")
                    print(f"Schlüssellänge:    {key_length}")
                    print(f"Schlüssel:         {key}")
                    print(f"Entschlüsselung:\n{decrypted[:500]}")

if __name__ == "__main__":
    main()