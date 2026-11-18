"""
Module to help with DHKE homework.\n
Author: Esther Arimoro
"""
import math

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

def main():
    # Q1
    priv_a = 3
    priv_b = 5
    alpha = 2
    p = 467
    print_dhke(priv_a, priv_b, alpha, p)
    
    priv_a = 400
    priv_b = 134
    print_dhke(priv_a, priv_b, alpha, p)
    
    priv_a = 228
    priv_b = 57
    print_dhke(priv_a, priv_b, alpha, p)
    
    # Q2
    alpha = 4
    print()
    priv_a = 400
    priv_b = 134
    print_dhke(priv_a, priv_b, alpha, p)
    
    priv_a = 167
    print_dhke(priv_a, priv_b, alpha, p)

if __name__ == "__main__":
    main()