'''Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd'''


def odd_product(input):
    isodd = False
    seq = input.split(',')
    for i in seq:
        for r in range(len(seq)):
            if (int(i)*int(seq[r]))%2 !=0 and int(i)!=int(r):
                isodd = True
    return isodd

print(odd_product('3,4,5,6,7,8'))