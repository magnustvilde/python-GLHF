'''Roman numbers is a number-system used by the ancient Romans.
You can still see them today, maybe in tattoos and on watches.
An example is the number 26, which translates to the
Roman number of XXVI.'''
 
# TASK
'''
Make a num_to_roman transformer, that takes in an integer
and prints the transformed value.

Roman values:
1 = I, IV = 4, 5 = V, IX = 9, 10 = X, XL = 40,
L = 50, XC = 90, C = 100, CD = 400, D = 500, CM = 900, M = 1000
'''

def num_to_roman(number: int) -> str:
    '''
    Function that takes in an integer and returns its roman numbers value.
    '''
    roman: str = ''
    while number > 0:
        if number >= 1000:
            roman += 'M'
            number -= 1000
        elif number >= 900:
            roman += 'CM'
            number -= 900
        elif number >= 500:
            roman += 'D'
            number -= 500
        elif number >= 400:
            roman += 'CD'
            number -= 400
        elif number >= 100:
            roman += 'C'
            number -= 100
    print(roman)

num_to_roman(2200)