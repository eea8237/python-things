"""
Module for encrypting / decrypting ciphers using an affine cipher.
Author: Esther Arimoro
"""
import math

ASCII_SHIFT = 97 # using lowercase ASCII characters for conversions

def encrypt_letter(plaintext, a, b):
    """
    Encrypt a plaintext letter using the given key (a, b).
    """
    
    # assume that we're only using the 26 letters of the alphabet
    plaintext = plaintext.lower()
    
    plaintext_value = ord(plaintext) - ASCII_SHIFT # let's work with integer ring 26
    ciphertext_value = plaintext_value * a + b % 26
    ciphertext = chr(ciphertext_value + ASCII_SHIFT)
    return ciphertext
        
    
def encrypt(plaintext, a, b):
    """
    Encrypt a plaintext string using the given key (a, b).
    """
    
    ciphertext = ""
    for char in plaintext:
        ciphertext += encrypt_letter(char, a, b).lower()
    
    return ciphertext

def decrypt_letter(ciphertext, a, b):
    """
    Decrypt a ciphertext letter using the given key (a, b).
    """
    
    # assume that we're only using the 26 letters of the alphabet
    ciphertext = ciphertext.lower()
    ciphertext_value = ord(ciphertext) - ASCII_SHIFT # let's work with integer ring 26
    plaintext_value = pow(a, -1, 26) * (ciphertext_value - b) % 26
    plaintext = chr(plaintext_value + ASCII_SHIFT)
    return plaintext
        
    
def decrypt(ciphertext, a, b):
    """
    Decrypt a ciphertext string using the given key (a, b).
    """
    
    plaintext = ""
    for char in ciphertext:
        plaintext += decrypt_letter(char, a, b).lower()
    
    return plaintext

def brute_force(ciphertext):
    """
    Run through each potential key to try and decrypt a given ciphertext.
    """
    print(f"Decrypting ciphertext: {ciphertext}\n")
    # 1, 3, 5, 7, 9, 11, 5, 17, 19, 21, 23, 25
    possible_a_values = [i for i in range(26) if math.gcd(i, 26) == 1]
    for a in possible_a_values:
        for b in range(26):
            print(f"Key ({a}, {b}): {decrypt(ciphertext, a, b)}")
    

def main():
    # testing encrypt
    # plaintext_input = input("Enter plaintext to encrypt: ")
    # a = input("Enter a key value (a): ")
    # b = input("Enter a key value (b): ")
    # ciphertext = encrypt(plaintext_input, int(a), int(b))
    # print(f"Ciphertext: {ciphertext}")
    
    # testing decrypt
    # ciphertext_input = input("Enter ciphertext to decrypt: ")
    # a = input("Enter a key value (a): ")
    # b = input("Enter a key value (b): ")
    # plaintext = encrypt(ciphertext_input, int(a), int(b))
    # print(f"Plaintext: {plaintext}")
    
    # test string: zrckewsgnpaovhatbeqfuajcpzrclidyxamu
    # key is (5, 8)
    ciphertext_input = input("Enter ciphertext to decrypt: ")
    brute_force(ciphertext_input)
    
    
    

if __name__ == "__main__":
    main()
    
    
    
    