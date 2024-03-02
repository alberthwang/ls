'''

Isn't it Odd?

Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.
'''
def run(num):
    return bool(abs(num)%2)


print(run(0)) #false
print(run(2)) #true
print(run(3)) #false
print(run(100)) #false
print(run(-1010487)) #true

