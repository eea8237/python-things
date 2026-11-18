"""
Module to help with finding primitive elements.\n
Author: Esther Arimoro
"""

def primes(n):
    ring = [i for i in range(n)]
    powers = [[pow(i, j, n) for j in range(n)] for i in range(n)]
    return ring, powers

def print_powers(n):
    print(f"INTEGER RING {n}")
    ring, powers = primes(n)
    
    print(f"   {ring}")
    for i in range(len(powers)):
        print(f"{i}: {powers[i]}")
        
# add function for determine cycle length of each value
# probably use sers or something?

def main():
    print_powers(11)
    
if __name__ == "__main__":
    main()