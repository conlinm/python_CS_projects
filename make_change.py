def make_change(amount):
    # add docstring to document function
    """
    A function that returns the minimum number of bills and coins
    to make change.

    This function, given an value ('amount') will determine the 
    number of one dollar bills, quarters, dimes, nickels, and pennies
    to be given.

    Parameters:
        amount (float): the amount of change to be given
    
    Returns:
        string: The chage to be given in dollar bills, quarters,
        dimes, nickels, and pennies, listed separately

    Examples:

        >>> make_change(5.68)
        5 ones
        2 quarters
        1 dime
        1 nickels
        3 pennies

        >>> make_change(33.32)
        33 ones
        1 quarters
        1 nickels
        2 pennies

    """
    # Convert change amount to cents.
    cents = round(amount * 100)
    # 100 cents per $1
    ones = cents // 100
    ones_remainder = cents % 100
    # 25 cents per quarter
    quarters = ones_remainder // 25
    quarters_remainder = ones_remainder % 25
    # 10 cents per dime
    dimes = quarters_remainder // 10
    dimes_remainder = quarters_remainder % 10
    # 5 cents per nickel
    nickels = dimes_remainder // 5
    # pennies
    pennies = dimes_remainder % 5

    if ones > 0:
        print(f'{ones} ones')
    if quarters > 0:
        print(f'{quarters} quarters')
    if dimes > 0:
        print(f'{dimes} dime')
    if nickels > 0:
        print(f'{nickels} nickels')
    if pennies > 0:
        print(f'{pennies} pennies')