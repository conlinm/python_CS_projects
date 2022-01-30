def fizz_buzz(start, end):
    """
    Prints the non-zero positive integers from start to end.
        * For multiples of three prints "Fizz".
        * For multiples of five prints "Buzz".
        * For multiples of three and five prints "FizzBuzz".
        * Otherwise, the function prints the integer.

    Parameters:
        start (int): a non-zero positive integer value representing
            the start of the sequence of interest
        end (int): a non-zero positive integer value representing
            the end of the sequence of interest

    Example:
        >>> fizz_buzz(1, 5)
        1 -> 1
        2 -> 2
        3 -> Fizz
        4 -> 4
        5 -> Buzz
        15 -> FizzBuzz
    """
    # loop over the list of ints from start to end
    for num in range(start, end + 1):
        # the first bit of the print statement that is the same for all numbers
        print(f"{num} ->", end = "")
        if num % 3 == 0 and num % 5 ==0:  
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)