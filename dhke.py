"""
Module to help with DHKE homework.\n
Author: Esther Arimoro
"""
import math
import discrete_log

def dhke(priv_a, priv_b, alpha, p):
    pub_a = pow(alpha, priv_a, p)
    pub_b = pow(alpha, priv_b, p)
    
    # alice shares public key with bob, bob shares public key with alice
    shared_a = pow(pub_b, priv_a, p)
    shared_b = pow(pub_a, priv_b, p)
    
    # return all keys generated
    return pub_a, pub_b, shared_a, shared_b

def print_dhke(priv_a, priv_b, alpha, p):
    print(f"a={priv_a}, b={priv_b}, alpha={alpha}, p={p}")        
    pub_a, pub_b, shared_a, shared_b = dhke(priv_a, priv_b, alpha, p)
    print(f"public keys: A={pub_a}, B={pub_b}")
    print(f"shared keys: B^a % p = {shared_a} , A^b % p = {shared_b}\n")


# work for Q5
def get_masking_keys(alpha, beta, p):
    """
    Get the masking keys that are possible from the gien alpha and beta.
    """
    # beta = alpha^d mod p
    d = discrete_log.brute_force(alpha, beta, p)
    
    # i is in the set {2, ... p - 2}
    eph_keys = set()
    for i in range(2, p - 1):
        eph_key = pow(alpha, i, p)
        # print(f"{alpha}^{i} mod {p} = {eph_key}")
        eph_keys.add(eph_key)
    print(f"ephemeral keys: {eph_keys}")
    
    masking_keys_b = set()
    for eph_key in eph_keys:
        masking_key = pow(eph_key, d, p)
        masking_keys_b.add(masking_key)
    print(f"masking keys: {masking_keys_b}")
    
    # masking_keys_a = set()
    # for i in range(2, p - 1):
    #     masking_key = pow(alpha, i, p)
    #     masking_keys_a.add(masking_key)
    # print(f"a: {masking_keys_a}")
    
    return masking_keys_b, d

def find_inverse(a, n):
    """
    Find a_inv in integer ring n using bruteforce
    """
    for i in range(n):
        result = a * i % n
        if result == 1:
            return i
    return -1
    
def decrypt_attack(ciphertext, alpha, beta, p):
    """
    Decrypt ciphertext.
    
    Args:
        ciphertest (list<tuple>): A list of tuples containing ephemeral keys and ciphertest.
        masking_keys (set): A set of possible masking keys.
    """
    masking_keys, d = get_masking_keys(alpha, beta, p)
    # for key in masking_keys:
    #     print(find_inverse(key, p))
    encoding = {i:chr(i + 97) for i in range(26)}
    ptxt = ""
    for ctxt in ciphertext:
        eph_key = ctxt[0]
        print(ctxt)
        count = 0
        for masking_key in masking_keys:
            # determine if this is the correct masking key
            if eph_key is not None:
                testing_key = pow(eph_key, d, p)
                if testing_key != masking_key:
                    continue
                print(f"\t{eph_key}^{d} mod {p} = {testing_key}")
             
            key_inv = find_inverse(masking_key, p)
            y = ctxt[1]
            x = y * key_inv % p 
            try:
                print(f"\tx = {x}, {encoding[x]}")
                txt = encoding[x]
            except KeyError:
                print(f"\tx = {x}, not found")
                txt = None
            if eph_key is not None:
                # this is the only letter that needs to be added
                ptxt += txt
            else:
                # add each possible letter
                if count == 0:
                    ptxt += "{"
                ptxt += txt if txt is not None else ""
                count += 1
                if count == len(masking_keys):
                    ptxt += "}"
                    count = 0
                else:
                    ptxt += ", " if txt is not None else ""
    print(ptxt)
    return ptxt    
            
                


def main():
    # Q1
    # priv_a = 3
    # priv_b = 5
    # alpha = 2
    # p = 467
    # print_dhke(priv_a, priv_b, alpha, p)
    
    # priv_a = 400
    # priv_b = 134
    # print_dhke(priv_a, priv_b, alpha, p)
    
    # priv_a = 228
    # priv_b = 57
    # print_dhke(priv_a, priv_b, alpha, p)
    
    # # Q2
    # alpha = 4
    # print()
    # priv_a = 400
    # priv_b = 134
    # print_dhke(priv_a, priv_b, alpha, p)
    
    # priv_a = 167
    # print_dhke(priv_a, priv_b, alpha, p)
    
    # Q5
    alpha = 3
    beta = 25
    p = 31
    masking_keys, d = get_masking_keys(alpha, beta, p)

    print()
    ciphertext = [(14, 3), (26, 23), (9, 8), (None, 26), (None, 7), (29, 13), (29, 8), (None, 19), (None, 9), (26, 23)]
    decrypt_attack(ciphertext, alpha, beta, p)
    
if __name__ == "__main__":
    main()