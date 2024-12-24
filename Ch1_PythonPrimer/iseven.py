'''Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators'''
def is_even(n):
    return True if int(str(n)[-1]) in [0,2,4,6,8] else False

print(is_even(29))


