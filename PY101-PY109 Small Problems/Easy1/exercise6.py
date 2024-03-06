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
        choice = input('Did you want the sum(s) or product(p)')
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

def getNums():

    while True:
        prompt = input('Enter a list of nums separated by space ')
        nums = prompt.split()
        valid = True
        numslist = []
        # print(numslist , ' + 1')
        # print(nums, '+2')
        for num in nums:
            if not num.isnumeric() or int(num) < 0:
                print('invalid input')
                valid = False
                break
            else:
                numslist.append(int(num))
        
        if valid:
            print(numslist)
            return numslist
            break
        else:
            print('new numbers')

        
def getSum(nums):
    print(f'The sum of {nums} is {sum(nums)}')
    return sum(nums)

def getProduct(nums):
    total = 1
    for num in nums:
        total *= num
    
    print(f'The product of {nums} is {total}')
    return total

    

def run2():
    nums = getNums()
    choice = getChoice()
    print(nums)

    if choice == 's':
        getSum(nums)
    elif choice == 'p':
        getProduct(nums)
    else:
        print("I'm going to give you the product anyways.")
        getProduct(nums)


run2()