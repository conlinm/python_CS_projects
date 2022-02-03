def sum_digits(int_num):
    """
    Returns the sum of the digits of a positive integer.

    Paramters:
        int_num (int): a positive integer

    Returns:
        int: the sum of the digits of int_num
       
    Examples:
        >>> sum_digits(1234)
        10

        >>> sum_digits(9850)
        22
    """ 
    # convert int to string to allow use of index
    str_num = str(int_num)

    # iterate through each digit, and add them to sum
    sum = 0
    for char in str_num:
        sum = sum + int(char)
    return sum
 

def is_valid_luhn_num(id):
    """
    Returns whether the string id is valid under Luhn's algorithm. 

    Paramters:
        id (str): a string representing an identification number. 

    Returns:
        bool: returns True if id is valid; returns False otherwise. 
    
    Examples:
        >>> is_valid_luhn_num('79927398713')
        True

        >>> is_valid_luhn_num('12345675')
        False
    """
    new_id = ''
    
    # take every second digit starting at the end of the id, and double it
    for char in id[-2::-2]:
        double = int(char) * 2

        # if the value has two digits, add them together
        if double > 9:
            double = sum_digits(double)
        # add 'double' to the new_id string
        new_id += str(double)

    # if not an 'every second digit', just add it to new_id
    for char in id[-1::-2]:
        new_id += char
    total = sum_digits(int(new_id))
    if total % 10 == 0:
        return True
    return False
