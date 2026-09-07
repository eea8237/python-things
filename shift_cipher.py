"""
Module for encrypting / decrypting ciphers using a shift cipher.
Author: Esther Arimoro
"""

ASCII_SHIFT = 97 # using lowercase ASCII characters for conversions

def encrypt_letter(plaintext, shift):
    """
    Encrypt a plaintext letter using the given shift value.
    """
    
    # assume that we're only using the 26 letters of the alphabet
    plaintext = plaintext.lower()
    
    plaintext_value = ord(plaintext) - ASCII_SHIFT # let's work with integer ring 26
    ciphertext_value = (plaintext_value + shift) % 26
    ciphertext = chr(ciphertext_value + ASCII_SHIFT)
    return ciphertext
        
    
def encrypt(plaintext, shift):
    """
    Encrypt a plaintext string using the given shift value.
    """
    
    ciphertext = ""
    for char in plaintext:
        ciphertext += encrypt_letter(char, shift).lower()
    
    return ciphertext

def decrypt_letter(ciphertext, shift):
    """
    Decrypt a ciphertext letter using the given shift value.
    """
    
    # assume that we're only using the 26 letters of the alphabet
    ciphertext = ciphertext.lower()
    
    ciphertext_value = ord(ciphertext) - ASCII_SHIFT # let's work with integer ring 26
    plaintext_value = (ciphertext_value - shift) % 26
    plaintext = chr(plaintext_value + ASCII_SHIFT)
    return plaintext
        
    
def decrypt(ciphertext, shift):
    """
    Decrypt a ciphertext string using the given shift value.
    """
    
    plaintext = ""
    for char in ciphertext:
        plaintext += decrypt_letter(char, shift).lower()
    
    return plaintext

def brute_force(ciphertext):
    """
    Run through each potential key to try and decrypt a given ciphertext.
    """
    print(f"Decrypting ciphertext: {ciphertext}\n")
    for i in range(26):
        print(f"Shift {i}: {decrypt(ciphertext, i)}")
    

def main():
    # testing encrypt
    # plaintext_input = input("Enter plaintext to encrypt: ")
    # encrypt_shift = input("Enter a shift value: ")
    # ciphertext = encrypt(plaintext_input, int(encrypt_shift))
    # print(f"Ciphertext: {ciphertext}")
    
    # testing decrypt
    # ciphertext_input = input("Enter ciphertext to decrypt: ")
    # decrypt_shift = input("Enter a shift value: ")
    # plaintext = encrypt(ciphertext_input, int(decrypt_shift))
    # print(f"Plaintext: {plaintext}")
    
    ciphertext_input = input("Enter ciphertext to decrypt: ")
    brute_force(ciphertext_input)
    
    
    

if __name__ == "__main__":
    main()
    
    
    
    