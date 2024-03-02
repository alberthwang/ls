'''

Odd Numbers

Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

Bonus Question: Can you solve the problem by iterating over just the odd numbers?

'''
def run():
    num = 1

    while num <= 99:
        print(num)
        num+=2

def run2():
    for i in range(1, 100, 2):
        print(i)

run()
#run2()