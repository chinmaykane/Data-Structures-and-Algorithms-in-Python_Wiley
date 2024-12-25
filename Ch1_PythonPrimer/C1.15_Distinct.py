'''Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)'''


def distinct(input):
    unique = True
    lizt = input.split(',')
    for n in lizt:
        lizt = input.split(',')
        lizt.remove(n)
        if n in lizt:
            unique = False
    return unique
print(distinct('4,6,6,8,9,0'))