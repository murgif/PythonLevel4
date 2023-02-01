#!/usr/bin/env python3

import string
from sys import argv
import collections
def decrypt(text, shift):
    decrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half
    for i, letter in enumerate(text.lower()):
        if letter in alphabet:
            index = shifted_alphabet.index(letter)
            original_letter = alphabet[index]
            decrypted_text[i] = original_letter
        else:
            decrypted_text[i] = letter

    return "".join(decrypted_text)
def brute_force(text):
    attempt = []
    for n in range(26):
        attempt.append(decrypt(text, n))

    e_count = []
    for i in range (0, len(attempt)):
        e_count.append(0)
        for n in range (0, len(attempt[i])):
            if attempt[i][n] == 'e':
                e_count[i] += 1
    location = e_count.index(max(e_count))
    print(f"Using a shift value of {location}")
    print(attempt[location])


filename = argv[1]

if __name__ == "__main__":

    decryption = ""
    with open(filename, 'r') as f:
        for line in f.readlines():
            decryption += str(line)
        brute_force(decryption)