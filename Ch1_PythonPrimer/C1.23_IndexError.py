"""Give an example of a Python code fragment that attempts to write an ele-
ment to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”"""
lsitt = [2,3,4,56,'yuiyu','yu']
print(lsitt)
newel = input('New Element')
posit = int(input('Its position'))
try:
    lsitt[posit] = newel
    print(lsitt)
except IndexError:
    print('Don’t try buffer overflow attacks in Python!')