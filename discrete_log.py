"""
Class for solving for bruteforcing the discrete log problem.\n
Author: Esther Arimoro
"""
import math
def solve_discrete_log(a, b, p):
    """
    solve for x in the equation a^x = b
    """
    # loga(b) = x
    return math.log(b, a) % p
    
def print_solution(a, b, p):
    x = solve_discrete_log(a, b, p)
    print(f"{a}^x % {p} = {b}")
    print(f"x={x}")
    print(f"verifying: {a}^{x} % {p} = {a**x % p}\n")

def main():
    # a.
    a = 2
    b = 162
    p = 173
    print_solution(a, b, p)
    
    # b.
    a = 7
    b = 6593
    p = 13649
    print_solution(a, b, p)
    
    # c.
    a = 1062
    b = 4134766
    p = 24691141
    print_solution(a, b, p)
    
    
    


if __name__ == "__main__":
    main()
