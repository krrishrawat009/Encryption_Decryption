import random
import string
from getpass import getpass

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)


def text():
    with open('Blackbox.csv', 'w') as f:
        f.write("**ENTERED INPUTS**\n")  # Write the title row

    while True:
        wish_text = input("Enter your wish e/d: ")
        
        if wish_text == "e":
            # ENCRYPT
            plain_text = getpass("Enter a message to encrypt: ")
            cipher_text = ""

            # Append data to the CSV file
            with open('Blackbox.csv', 'a') as f:
                f.write(plain_text + '\n')    # Add the input data

            for letter in plain_text:
                index = chars.index(letter)
                cipher_text += key[index]

            print(f"Encrypted message: {cipher_text}")
        
        elif wish_text == "d":
            # DECRYPT
            cipher_text = getpass("Enter a message to decrypt: ")
            plain_text = ""

            for letter in cipher_text:
                index = key.index(letter)
                plain_text += chars[index]

            print(f"Original message: {plain_text}")
        
        k = input("Do you wish to continue (y/n): ")
        if k.lower() == "n":
            break

text()
