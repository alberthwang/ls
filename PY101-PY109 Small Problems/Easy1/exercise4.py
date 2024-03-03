'''

How big is the room?

Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet

'''
def getChoice():
    while True:
        choice = input('What unit did you want you room area to be displayed in meters(m) or feet(f)')
        if choice.lower() == 'm' or choice.lower() == 'f':
            return choice.lower()
        else:
            print('invalid choice')


        
def run2():
    choice = getChoice()
    if choice == 'm':
        run()
    else:
        getareaft()

def getareaft():
    length = float(input('Give me a length in feet above 0: '))
    width = float(input('Give me a width in feet above 0: '))
    area = length * width
    area_m= area/10.7639

    print(f'The area of the room is {area:.2f} square feet square meters ({area_m:.2f} square meter)')

def run():
    length = float(input('Give me a length in meters above 0: '))
    width = float(input('Give me a width in meters above 0: '))
    area = length * width
    area_ft= 10.7639 * area

    print(f'The area of the room is {area} square meters ({area_ft:.2f} square feet)')

run2()