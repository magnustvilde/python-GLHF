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
def write_a_number():
    print('I want to add this line!')
    num = int(input('Write a number: '))
    return num

def num_to_roman(number):
    roman = ''
    while number>0:
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
        elif number >= 50:
            roman += 'L'
            number -= 50
        elif number >= 40:
            roman += 'XL'
            number -= 40
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

num_to_roman(write_a_number())

# TASK
'''
Make a roman_to_num transformer, that takes in a string and
prints the transformed value. It should work for both
upper- and lowercase letters.
'''
