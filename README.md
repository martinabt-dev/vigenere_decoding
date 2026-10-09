# Vigenère Cipher Decryption

## Overview

This project explores how to decrypt text encrypted with the Vigenère cipher when the original key is unknown.

The implementation uses a dictionary-based approach to identify potential plaintext words, calculate candidate keys, and evaluate the resulting decryptions based on how closely they match common English vocabulary.

Instead of relying on a single manually selected word, the program automatically identifies the longest words in the ciphertext and tests them as potential plaintext candidates.

## How It Works

The program follows several steps to identify possible decryption keys.

### 1. Text Preprocessing

The ciphertext is split into individual words. The program identifies the maximum word length and collects all words matching that length.

A separate helper function removes non-ASCII letters and converts the remaining characters to lowercase. This allows the key calculation to work with a consistent representation of the English alphabet.

### 2. Plaintext Candidate Selection

The longest words in the ciphertext are used as potential plaintext candidates. The program uses a collection of common English words to help identify plausible matches.

Longer words can provide more information for key reconstruction, although word length alone does not guarantee that a candidate is correct.

### 3. Key Calculation

For each candidate, the program compares the ciphertext word with the proposed plaintext word, character by character.

The numerical positions of the letters are used to calculate the required shifts:

`K = (C - P) mod 26`

Where:

* `K` represents the key character.
* `C` represents the ciphertext character.
* `P` represents the plaintext character.

Python's `ord()` and `chr()` functions convert between characters and their numerical representations.

### 4. Key Length Verification

The calculated key segment is checked against possible key lengths.

For a repeating Vigenère key, characters at positions separated by the key length should match. The program uses this property to identify compatible key lengths.

### 5. Key Reconstruction and Decryption

After identifying compatible key lengths, the program reconstructs candidate keys while accounting for the position of the candidate word in the ciphertext.

The `decrypt()` function then applies the candidate key to the full ciphertext. It preserves non-letter characters and spaces while decrypting ASCII letters.

### 6. English Language Scoring

The resulting plaintext candidates are evaluated using a dictionary of common English words.

The scoring function searches for English words in each candidate text and adds their corresponding scores. Candidates with higher scores are considered more likely to contain meaningful English text.

This provides a way to rank possible decryptions, although the highest score does not necessarily guarantee the correct result.

## Python Concepts Used

* **String manipulation** — splitting, cleaning, and joining text.
* **List processing** — collecting candidate words and decrypted results.
* **Loops and comprehensions** — iterating over text and generating results.
* **`zip()`** — comparing ciphertext and plaintext characters in pairs.
* **`ord()` and `chr()`** — converting between characters and numerical values.
* **Modular arithmetic** — calculating shifts within the 26-letter alphabet.
* **Regular expressions** — extracting English words for scoring.
* **Dictionary lookups** — evaluating candidates using common English vocabulary.
* **Functions and modular design** — separating preprocessing, key calculation, decryption, and scoring into individual functions.

## Limitations

The method relies on suitable plaintext candidates and assumptions about the language of the original text.

* The longest ciphertext words are not necessarily the most useful candidates.
* A word may have multiple plausible interpretations, and a common-word dictionary cannot recognize every valid English word.
* Different candidate keys may produce similar language scores.
* The key length verification checks compatibility but does not independently prove that a candidate key is correct.
* The scoring method is vocabulary-based rather than a complete statistical language model.

The project is intended as an educational exploration of classical cryptanalysis. It is not designed to break modern encryption algorithms.

## Project Structure

```text
vigenere_decoding/
├── main.py
├── requirements.txt
├── README.md
└── src/
    ├── functions.py
    ├── config.py
    └── text.py
```

The `src` package contains the helper functions for text processing, key calculation, decryption, and language scoring. The `text.py` module provides the common-word data used to evaluate candidate plaintexts.

## Technologies

* Python
* Regular expressions (`re`)
* String processing
* Modular arithmetic
* Dictionary-based language scoring

## Project Goals

The main goal of this project is to understand the mathematical principles behind the Vigenère cipher and implement a practical approach to candidate key recovery.

The project also provides hands-on experience with Python functions, text processing, algorithmic problem-solving, and evaluating candidate solutions using a simple scoring system.

## Status

Educational project — implementing and evaluating a dictionary-based approach to Vigenère cipher decryption.
