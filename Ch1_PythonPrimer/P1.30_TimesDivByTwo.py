"""Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2"""

def divby2(numb):
    return int(numb)//2

def divby2hard(numbr):
    countr = 0
    while int(numbr)>=2:
        numbr = int(numbr) - 2
        countr +=1
    return countr

print(divby2hard(8))
