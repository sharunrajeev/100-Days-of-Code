# Python implementation of Caesar Cipher
# Caeser Cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet.
# The original message is written using the original alphabet and the ciphertext is written using the shifted alphabet.
# The original alphabet is a-z and the shifted alphabet is a-z.

from typing import Text
from caesar_cipher_asset import *

def caesar_cipher(input, shift, direction):
    # input is a string
    # shift is an integer
    # direction is a string -> encode or decode
    # returns a string (output)
    output = ''
    if direction == 'decode':
        shift *= -1
    for char in input:
        if char.isalpha():
            output += alphabet[alphabet.index(char) + shift]
        else:
            output += char
    print(f"Here is the {direction}d result : {output}")

restart = True
while restart:
    print("logo\n")
    print("Welcome to the Caesar Cipher Encoder/Decoder\n")
    direction = input("Would you like to encode or decode?\n")
    text = input("What is the text you would like to encode/decode?\n")
    shift = int(input("What is the shift value?\n"))
    if shift > 26 :
        shift %= 26
    caesar_cipher(text, shift, direction)
    if input("Would you like to encode/decode another text?\n") != 'yes':
        restart = False