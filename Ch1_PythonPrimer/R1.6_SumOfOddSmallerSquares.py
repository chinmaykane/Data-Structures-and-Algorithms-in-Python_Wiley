'''Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n'''
def sum_of_odd_smaller_squares(n):
    s=0
    if n%2==0:
        while n>0:
            s = s + ((n-1)*(n-1))
            n = n-2
    else:
        while n-2>0:
            s = s + ((n-2)*(n-2))
            n = n-2
    return s
print(sum_of_odd_smaller_squares(10))