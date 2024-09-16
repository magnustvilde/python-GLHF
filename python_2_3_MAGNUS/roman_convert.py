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

def num_to_roman(number):
    roman_number = ''
    while number:
        if number >= 1000:
            roman_number += 'M'
            number -= 1000
        elif number >= 900:
            roman_number += 'CM'
            number -= 900
        elif number >= 500:
            roman_number += 'D'
            number -= 500
        elif number >= 400:
            roman_number += 'CD'
            number -= 400
        elif number >= 100:
            roman_number += 'C'
            number -= 100
        elif number >= 50:
            roman_number += 'L'
            number -= 50
        elif number >= 40:
            roman_number += 'XL'
            number -= 40
        elif number >= 10:
            roman_number += 'X'
            number -= 10
        elif number >= 9:
            roman_number += 'IX'
            number -= 9
        elif number >= 5:
            roman_number += 'V'
            number -= 5
        elif number >= 4:
            roman_number += 'IV'
            number -= 4
        elif number >= 1:
            roman_number += 'I'
            number -= 1
        print(roman_number)

num_to_roman(2999)