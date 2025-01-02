"""Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once."""
from itertools import permutations

def all_possible_strings(*args):
    perms = []
    for group in range(len(args)+1):
        thisperm = list(permutations(args, group))
        perms.append(thisperm)
    return perms

print(all_possible_strings('a','b','c','d'))