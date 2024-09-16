'''Roman numbers is a number-system used by the ancient Romans.
You can still see them today, maybe in tattoos and on watches.
An example is the number 26, which translates to the
Roman number of XXVI.'''


# TASK
'''
Make a num_to_roman transformer, that takes in an integer
and prints the transformed value.
Roman values:
1 = I, IV = 4, 5 = V, IX = 9, 10 = X,
L = 50, XC = 90, C = 100, D = 500, M = 1000
'''

convert_number: int = int(input('Write a number to convert to a Roman number: '))

def num_to_roman(number: int) -> str:
    """
    Convert integer to roman number.
    """
    roman: str = ''
    while number>0:
        if number >= 1000:
            roman += 'M'
            number -= 1000
        elif number >=900:
            roman += 'CM'
            number -= 900
        elif number >=500:
            roman += 'D'
            number -= 500
        elif number >=100:
            roman += 'C'
            number -= 100
        elif number >=90:
            roman += 'XC'
            number -= 90
        elif number >=50:
            roman += 'L'
            number -= 50
    return roman
    
print(num_to_roman(convert_number))