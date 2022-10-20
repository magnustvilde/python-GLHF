# INFORMATION
'''
Roman numbers is a number-system used by the ancient Romans.
You can still see them today, maybe in tattoos and on watches.
An example is the number 26, which translates to the
Roman number of XXVI.
'''

# TASK
'''
Make a num_to_roman transformer, that takes in an integer
and prints the transformed value.
Roman values:
1 = I, 5 = V, 10 = X,
L = 50, C = 100, D = 500, M = 1000
'''
def num_to_roman(number):
    roman = ''
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
        elif number >= 100:
            roman += 'C'
            number -= 100
        elif number >= 50:
            roman += 'L'
            number -= 50
        elif number >= 10:
            roman += 'X'
            number -= 10
        elif number >= 9:
            roman += 'IX'
            number -= 9
        elif number >= 5:
            roman += 'V'
            number -= 5
        elif number >= 4:
            roman += 'IV'
            number -= 4
        elif number >= 1:
            roman += 'I'
            number -= 1
        print(roman)
        print('Remaining:', number)
    print(f'Result: {roman}')

def write_number():
    num = int(input('Convert number:'))
    return num

num_to_roman(write_number())

'''
Roman numbers also have this attribute, e.g.
making the number 9 is I less than X:
IV = 4, IX = 9, XL = 40,
XC = 90, CD = 400, CM = 900
'''

# TASK
'''
Make a roman_to_num transformer, that takes in a string and
prints the transformed value. It should work for both
upper- and lowercase letters.
'''
