'''Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd'''


def odd_product(input):
    isodd = False
    seq = input.split(',')
    for i,r in seq:
        if (i*r)%2 !=0:
            isodd = True
    return isodd
print(odd_product('3,4,5,6,7,8'))