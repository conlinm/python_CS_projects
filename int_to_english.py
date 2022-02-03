def int_to_english_ones(n):
    """
    A function that takes a positive integer 
    parameter n and returns a string with the equivalent English text 
    for the 'ones' digit.

    Parameters:
        n (int): positive integer 
   
    Returns:
        string: the english word for the ones digit of 'n'

    Examples:

        >>> int_to_english(243)
        'three'

    """
    
    # create list of english words integers
    ones = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']

    final_string = ""

    # index will be the ones place for any number
    index = n%10

    # pull correspnding word from 'words' to 'final_string', and return
    final_string = ones[index]

    return final_string

def int_to_english_teens(n):
    """
    A function that takes a positive integer 10 < n < 20, as
    parameter n and returns a string with the equivalent English text 
    for that value.

    Parameters:
        n (int): positive integer from 11 to 19
   
    Returns:
        string: the english word for the digit 'n'

    Examples:

        >>> int_to_english(18)
        'eighteen'

    """
    
    # create list of english words for the teens:
    teens =  ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
              'sixteen', 'seventeen', 'eighteen', 'nineteen']

    final_string = ""

    # index comes from the ones place, subtracting 1 to line up with
    # the correct value in our list 'teens'
    index = n%10 - 1

    # pull correspnding word from 'teens' to 'final_string', and return
    final_string = teens[index]

    return final_string

def int_to_english_tens(n):
    """
    A function that takes a positive integer 20 < n < 100, as
    parameter n and returns a string with the equivalent English text 
    for that value.

    Parameters:
        n (int): positive integer from 21 to 99
   
    Returns:
        string: the english word for the digit 'n'

    Examples:

        >>> int_to_english(98)
        'ninety-eight'

    """
    
    # create list of english 'tens'
    tens = ['twenty', 'thirty', 'forty', 'fifty', 
            'sixty', 'seventy', 'eighty', 'ninety']

    final_string = ""

    # index comes from the tens place, subtracting 2 to line up with
    # the correct value in our list 'tens'
    index = n//10 - 2

    # pull correspnding word from 'tens' to 'final_string', and return
    final_string = tens[index]

    return final_string


def int_to_english(n):
    """
    A function that taks a positive integer 
    parameter n that returns a string with the equivalent English text 
    representing the integer parameter.

    Parameters:
        n (int): positive integer from 0 to 1,000,000
   
    Returns:
        string: the english words for the number 'n'

    Examples:

        >>> int_to_english(181) 
         'one hundred eighty-one'

    """
    # the final string is stored in 'english'
    english = ''

    if n < 10:
        english = int_to_english_ones(n)
    elif n < 20:
        english = int_to_english_teens(n)
    elif n < 100:
        if n%10 == 0:
            english = int_to_english_tens(n)
        else:
            english = f'{int_to_english_tens(n)}-{int_to_english_ones(n)}'

    # recursivly use in_to_english() to build the remaining english 
    # after the thousands and hundreds places
    elif n < 1000:
        if n%100 == 0:
            english = f'{int_to_english_ones(n//100)} hundred'
        else:
            english = f'{int_to_english_ones(n//100)} hundred {int_to_english(n%100)}'
    elif n < 1_000_000:
        if n%1000 == 0:
            english = f'{int_to_english_ones(n//1000)} thousand'
        elif n%10_000 == 0:
            # need to add in code to account for ten thousand, 21 thousand, etc
            english = f'{int_to_english_tens(n//10_000)} thousand'
        elif n%100_000 == 0:
            english = f'{int_to_english_ones(n//100_000)} hundred'
        else:
            english = f'{int_to_english(n//1000)} thousand {int_to_english(n%1000)}'
    elif n == 1_000_000:
        english = "one million"

    return english



