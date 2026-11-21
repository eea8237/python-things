"""
Class for solving the discrete log problem.\n
Author: Esther Arimoro
"""
import math
def brute_force_discrete_log(a, b, p):
    """
    solve for x in the equation a^x = b mod p using brute force
    """
    solution = -1
    for x in range(p):
        answer = pow(a, x, p)
        if answer == b:
            solution = x
            break
    return solution
        
def main():
    # a.
    a = 2
    b = 162
    p = 173
    x = brute_force_discrete_log(a, b, p)
    print(f"{a}^x = {b} mod {p}")
    print(f"x={x}")
    
    # b.
    a = 7
    b = 6593
    p = 13649
    x = brute_force_discrete_log(a, b, p)
    print(f"{a}^x = {b} mod {p}")
    print(f"x={x}")
    
    # c.
    a = 1062
    b = 4134766
    p = 24691141
    x = brute_force_discrete_log(a, b, p)
    print(f"{a}^x = {b} mod {p}")
    print(f"x={x}")

if __name__ == "__main__":
    main()
