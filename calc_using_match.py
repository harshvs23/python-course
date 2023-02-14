# using match

import os

while True:
    print('Select a number')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Remainder')
    print('6. Exiting' )
    match(input('Enter your choice:')):

        case '1':
            a=int(input('Enter first number: '))
            b=int(input('Enter second number: '))
            print(f'{a} + {b} is {a+b}')
        case '2':
            a=int(input('Enter first number: '))
            b=int(input('Enter second number: '))
            print(f'{a} - {b} is {a-b}')
        case '3':
            a=int(input('Enter first number: '))
            b=int(input('Enter second number: '))
            print(f'{a} * {b} is {a*b}')
        case '4':
            a=int(input('Enter first number: '))
            b=int(input('Enter second number: '))
            print(f'{a} / {b} is {a/b}')
        case '5':
            a=int(input('Enter first number: '))
            b=int(input('Enter second number: '))
            print(f'{a} % {b} is {a%b}')

        case '6' :
            print('Exiting...')
            break
        case _:
            print('empty')

    input('Press enter to continue...')
    os.system('cls')


