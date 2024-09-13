#This Python script uses the cryptography library to encrypt a message using symmetric encryption. Symmetric encryption is a type of encryption where the same key is used for encryption and decryptio
import cryptography

# use symetric encryption method
from cryptography.fernet import Fernet

# genrate key
key = Fernet.generate_key()

# create a fernet object
cipher = Fernet(key)

#The message we want to encrypt
message = "this is a secret message ".encode()
print(" Original message: ", message.decode())

#Encrypt the message 
encrypted_message = cipher.encrypt(message)
print("Secret message:", encrypted_message.decode())
