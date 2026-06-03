''' euclid_gcd
'''

def euclid_gcd(nat_a: int, nat_b: int) -> int:
    ''' Returns the greatest common divisor of nat_a and nat_b.
        example:
        >>>euclid_gcd(88755, 23973)
        183
    '''
    # garbage filter to catch bad input
    assert (isinstance(nat_a, int) and nat_a > 0) \
      and  (isinstance(nat_b, int) and nat_b > 0),\
           "nat_a and nat_b must be natural numbers."
    # implementation of the algorithm
    while nat_b:
        nat_a, nat_b = nat_b, nat_a % nat_b
    return nat_a
