Overview


This Python script provides a simple encryption and decryption tool using a substitution cipher. The script generates a random key based on a character set and uses it to encrypt or decrypt user-provided messages.


Features

Encryption: Converts plain text into ciphertext using the generated key.
Decryption: Decrypts ciphertext back into plain text using the same key.
Key Generation: Creates a random key for each session.
CSV Logging: Records encrypted messages in a CSV file for auditing.
Usage


Clone the repository:
Bash
git clone https://github.com/your-username/encryption-decryption-tool.git
Use code with caution.


Install dependencies:
Bash
pip install -r requirements.txt
Use code with caution.


Run the script:
Bash
python encryption_decryption.py
Use code with caution.

How it works


The script generates a random key by shuffling a list of characters.
The user is prompted to enter either "e" for encryption or "d" for decryption.
If "e" is chosen, the user enters a plain text message. The script iterates through each character, finds its corresponding index in the character list, and replaces it with the character at the same index in the key.
If "d" is chosen, the user enters a ciphertext message. The script performs the reverse process, finding the index of each character in the key and replacing it with the corresponding character in the character list.
The encrypted or decrypted message is displayed to the user.
The script continues to prompt for input until the user enters "n" to quit.
Contributing

Contributions are welcome! Please feel free to fork the repository, make changes, and submit a pull request.
