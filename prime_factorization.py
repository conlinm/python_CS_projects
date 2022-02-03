def prime_factors(n):
    """Returns the list of prime factors for a 
      positive integer n. The list will be
      returned in sorted order.

    Args:
        n (int): integer of interest
    
    Returns:
        list: list of prime factors 

    Examples:
        >>> prime_factors(6)
        [2, 3]

        >>> prime_factors(36)
        [2, 2, 3, 3]

    """
    # initialze factor
    factor = 2
    factor_list = []

    while factor <= n:
        if n%factor == 0:
            factor_list = factor_list + [factor]
            n = n//factor
        else:
            factor += 1
    return sorted(factor_list) 
