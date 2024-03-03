'''

Sum or Product of Consecutive Integers

Write a program that asks the user to enter an integer greater than 0, 
then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

'''
def getNum():
    while True:
        try:
            num = int(input('Enter a interger above 0: '))
            if num < 0 : 
                print('that is not a valid number')
            else:
                return num
            
        except ValueError:
            print('that is not a valid number')

def getChoice():
    while True:
        choice = input('Did you want the sum(s) or product(p) of all the numbers between 1 and the entered integer?')
        if choice.lower() == 's' or choice.lower() == 'p':
            return choice.lower()
        else:
            print('invalid choice')

def sums(num):
    total = 0
    total = sum(range(1,num+1))
    print(f'The sum from 1 to {num} is {total}')

def product(num):
    total = 1
    for i in range(1, num+1):
        total *= i
    print(f'The product from 1 to {num} is {total}')


def run():
    num = getNum()
    choice = getChoice()

    if choice == 's':
        sums(num)
    else:
        product(num)

run()