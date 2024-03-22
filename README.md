Simple Substitution Cipher Encryption/Decryption
Overview
This Python script implements a basic encryption and decryption system using a simple substitution cipher. The program allows users to encrypt and decrypt messages using a randomly generated key.

Features
Encryption: Users can input a message and receive its encrypted form.
Decryption: Encrypted messages can be decrypted back to their original form.
Logging: All entered inputs are logged into a CSV file named Blackbox.csv for record-keeping.
Security Considerations
It's important to note that the provided encryption mechanism is based on a basic substitution cipher, which is not secure for sensitive data. This implementation is intended for educational purposes and is not suitable for real-world applications requiring strong security.

Usage
Run the script substitution_cipher.py.
Choose whether to encrypt or decrypt a message by entering 'e' or 'd' respectively.
Enter the message as prompted.
Follow on-screen instructions to continue or exit the program.
Dependencies
Python 3.x
Files
substitution_cipher.py: The main Python script containing the encryption and decryption logic.
Blackbox.csv: A CSV file for logging entered inputs.
Future Improvements
Enhanced error handling for invalid inputs.
Improved key generation algorithm for better randomness.
Utilization of established encryption libraries for stronger security
