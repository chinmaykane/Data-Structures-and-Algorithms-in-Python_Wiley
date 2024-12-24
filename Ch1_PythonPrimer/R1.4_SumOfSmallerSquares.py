'''Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.'''
def sum_of_smaller_squares(n):
    s=0
    while n>0:
        s = s + ((n-1)*(n-1))
        n = n-1
    return s
print(sum_of_smaller_squares(10))
