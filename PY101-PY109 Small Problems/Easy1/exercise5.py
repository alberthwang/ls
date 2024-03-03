'''

Tip Calculator

Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. 
The program must compute the tip, then print both the tip and the total amount of the bill. 
You can ignore input validation and assume that the user will enter valid numbers.

'''

def run():
    bill = float(input('What is the bill amount? '))
    tip = float(input('What is the tip percentage? '))

    tipamount = bill * (tip/100)
    total = bill + tipamount

    print(f'The tip is ${tipamount:.2f}')
    print(f'The total is ${total:.2f}')

run()