"""
Program to help with RSA homework.\n
Author: Esther Arimoro
"""
import math

def find_inverse(number, modulus):
    """
    Find the (smallest) multiplicative inverse of a number with a given modulus.
    """
    # update this to use EEA probably
    for i in range(modulus):
        if (number * i) % modulus == 1:
            return i
    return -1 # inverse wasn't found

def euclidean_algorithm(number, modulus):
    """
    Find the (smallest) multiplicative inverse of a number with a given modulus.
    """
    # initialize
    a = number
    b = modulus
    quotients = []
    while b > 0:
        q = a // b
        r = a % b
        print(f"a={a}, b={b}, q={q}, r={r}")
        a = b
        b = r
        quotients.append(q)
    print(f"a={a}, b={b}, q={q}, r={r}")
    return a, b, quotients

def euclidean_algorithm(number, modulus, debug=False):
    """
    Find the (smallest) multiplicative inverse of a number with a given modulus.
    """
    # initialize
    a = number
    b = modulus
    quotients = []
    while b > 0:
        q = a // b
        r = a % b
        if debug: print(f"a={a}, b={b}, q={q}, r={r}")
        a = b
        b = r
        quotients.append(q)
    if debug: print(f"a={a}, b={b}, q={q}, r={r}")
    return a, b, quotients

def eea(number, modulus, debug=False):
    """
    Find the (smallest) multiplicative inverse of a number with a given modulus.
    """
    # initialize
    x_prime, y_prime, quotients = euclidean_algorithm(number, modulus, debug)
    
    if debug: print(quotients)
    line = len(quotients) - 1
    x = y_prime
    y = x_prime - y_prime * quotients[line]
    
    while line >= 0:
        
        if debug: print(f"x={x}, y={y}, x'={x_prime}, y'={y_prime}")
        old_x = x
        old_y = y
        
        x = y_prime
        if debug: print(f"{line}: {quotients[line]}")
        y = x_prime - y_prime * quotients[line]
        x_prime = old_x
        y_prime = old_y
        line -= 1
        
    if debug: print(f"x={x}, y={y}, x'={x_prime}, y'={y_prime}")
    return x % modulus, y % number


def encrypt(x, n, e):
    return pow(x, e, n)

def generate_codebook(n, e):
    """
    Generate a codebook using a given public key.
    """
    codebook = {}
    for i in range(ord("A"), ord("Z")+1):
        codebook[encrypt(i, n, e)] = chr(i)
    return codebook

def decrypt_codebook(ciphertext, codebook):
    """
    Use a codebook to decrypt ciphertext.
    
    Args:
        ciphertext (list<int>): A ciphertext message in the form of a list of integers.
    """
    plaintext = ""
    for ctxt in ciphertext:
        if ctxt in codebook:
            plaintext += codebook[ctxt] 
    return plaintext
    
def codebook_attack(n, e, ciphertext):
    codebook = generate_codebook(n, e)
    for ctxt in codebook:
        print(f"{ctxt} = {codebook[ctxt]}")
    
    plaintext = decrypt_codebook(ciphertext, codebook)
    print(plaintext)


def rsa_129(y):
    """
    decrypt some ciphertext using the rsa-129 challenge public key and e
    
    Args:
        y (int): The ciphertext to decrypt.
    """
    # multiply p and q to get n
    p = 3490529510847650949147849619903898133417764638493387843990820577
    q = 32769132993266709549961988190834461413177642967992942539798288533
    n = p * q
    totient_n = (p -1) * (q - 1)
    print(f"n = {n}\n")
    print(f"totient(n) = {totient_n}\n")
    
    e = 9007
    d = eea(e, totient_n)[0]
    print(f"d = {d}\n")
    
    # decrypt the text using the above values
    x = pow(y, d, n)
    # x = y ** d % n
    print(f"x = {x}\n")
    
    # decode the message using the encoding scheme
    str_x = str(x)
    if len(str_x) % 2 == 1:
        str_x = "0" + str_x
    
    scheme = get_rsa_encoding_scheme()
    msg = ""
    letter = ""
    for i in range(len(str_x)):
        letter += str_x[i]
        try:
            if len(letter) == 2:
                msg += scheme[letter]
                letter = ""
        except KeyError:
            letter = ""
            msg += "-"
    print(msg)
    return msg

def get_rsa_encoding_scheme():
    scheme = {"00":" "}
    for i in range(1, 27):
        if i < 10:
            scheme[f"0{i}"] = chr(i + 96)
        else:
            scheme[f"{i}"] = chr(i + 96)
    return scheme
 
def main():
    # n = 3763
    # e = 11
    # ciphertext = [2912, 2929, 3368, 153, 3222, 3335, 153, 1222]
    # codebook_attack(n, e, ciphertext)
    
    y = 24102230047908492921334561683677822772379364497905426326274048627460349574761254064237656827652272780749547791945400229075831407
    rsa_129(y)
    
    # print(euclidean_algorithm(31, 5))
    # print(eea(31, 5))
    # print(find_inverse(5, 31))
    
if __name__ == "__main__":
    main()