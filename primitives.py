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

def find_generators(p, factors, min=None, max=None, limit=None):
    """
    Find the number of generators in a multiplicative group Z*p
    
    Args:
        p (int): The prime number
        factors (list<int>): a list of the prime factors
        min (int): minimum value to search for primitives.
        max (int): max value to search for primitives
        limit (int): number of primitive values to return
    Returns:
        list<int>: A list of primitive values in the integer ring.
    """
    # determine cardinality
    card = p - 1
    
    if min is None:
        min = 1 # 0 is never primitive
    if max == None:
        max = card
    
    exponents = [card // i for i in factors]
    primitives = []
    if limit is not None:
        # keep track of the number of primitives that have been found
        count = 0
        alpha = min
        while count < limit:
            primitive = True
            test = 0
            for exp in exponents:
                test = pow(alpha, exp, p)
                print(f"{alpha}^{exp} = {test} mod {p}")
                if test == 1:
                    primitive = False
                    break
                
                
            if primitive:
                primitives.append(alpha)
                count += 1
            if count > card:
                break
            alpha += 1
            print()
     
    return primitives
    
    
def main():
    # print_powers(11)
    
    p = 4973
    factors = [2, 11, 113]
    min = 1001
    limit = 15
    primitives = find_generators(p, factors, min, limit=limit)
    print(primitives)
    
if __name__ == "__main__":
    main()