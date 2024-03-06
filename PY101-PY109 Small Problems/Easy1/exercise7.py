'''

Short Long Short

Write a function that takes two strings as arguments,
 determines the length of the two strings, 
 and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again.
   You may assume that the strings are of different lengths.
'''
def combine(short, long):
    return short+long+short


def run(str1, str2):
    if len(str1) < len(str2):
        return combine(str1, str2)
    else:
        return combine(str2, str1)
    

print(run('abc', 'defgh') =='abcdefghabc')
print(run('abcde', 'fgh') == 'fghabcdefgh')
print(run('' , 'xyz') == 'xyz')