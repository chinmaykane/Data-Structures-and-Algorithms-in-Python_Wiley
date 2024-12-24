'''Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.'''


def list_reversal(list):
    list = list.split(',')
    revd = []
    for i in list[:: -1]:
        revd.append(i)
    print(revd)


list_reversal('4,5,6,7,8,9')
for b in reversed([4, 5, 6, 7, 8, 9]):
    print(b, end=',')
