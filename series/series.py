
def fibonacci(n):
    '''
    Calculates the nth number in the Fibonacci sequence.

    Args:
        n (int): The index of the number to calculate. Must be a non-negative integer.

    Returns:
        int: The nth number in the Fibonacci sequence.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55    
        '''
    if n < 0 :
        return 'Please write non-negative number'
    if n >= 2:
        return fibonacci(n - 2) + fibonacci(n - 1)
    return n


def lucas(n):
    '''
    Calculates the nth number in the Lucas sequence.

    Args:
        n (int): The index of the number to calculate. Must be a non-negative integer.

    Returns:
        int: The nth number in the Lucas sequence.

    Examples:
        >>> Lucas(0)
        2
        >>> Lucas(1)
        1
        >>> Lucas(2)
        3
        >>> Lucas(3)
        4    
    '''
    if n < 0 :
        return 'Please write non-negative number'
    if n == 0:
        return n+2
    elif n == 1:
        return n
    elif n >= 2:
        return lucas(n - 2) + lucas(n - 1)
    return n


def sum_series(n, optional1=0, optional2=1):
    '''
    Calculates the nth number in the Fibonacci sequence or a modified sequence based on the first two optional arguments.

    Args:
        n (int): The index of the number to calculate. Must be a non-negative integer.
        optional1 (int): The first number in the sequence. Defaults to 0 for the standard Fibonacci sequence.
        optional2 (int): The second number in the sequence. Defaults to 1 for the standard Fibonacci sequence.

    Returns:
        int: The nth number in the Fibonacci sequence or the modified sequence based on the optional arguments.

    Examples:
        >>> sum_series(0)
        0
        >>> sum_series(1)
        1
        >>> sum_series(2)
        1
        >>> sum_series(3)
        2
        >>> sum_series(4, 2, 1)  # modified sequence starting with 2 and 1
        3
        >>> sum_series(5, 2, 1)  # modified sequence starting with 2 and 1
        5 
    '''
    series_name = ''

    if n == 0 and optional1 == 0 and optional2 == 0:
        return 0
    if n < 0 :
        return 'Please write non-negative number'
    
    if optional1 == 0 and optional2 == 1:
        series_name = 'Fibonacci series'
    elif optional1 == 2 and optional2 == 1:
        series_name = 'Lucas series'
    elif optional1 != 0 and optional2 != 1:
        series_name = 'Series'

    if n == 0:
        return optional1, f'It is {series_name}'
    elif n == 1:
        return optional2, f'It is {series_name}'
    elif n >= 2:
        num = sum_series(
            n - 2, optional1, optional2)[0] + sum_series(n - 1, optional1, optional2)[0]
        return num, f'It is {series_name}'


print(sum_series(3, 2, 1))
