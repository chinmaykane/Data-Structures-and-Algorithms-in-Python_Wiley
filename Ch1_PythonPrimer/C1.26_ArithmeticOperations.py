"""Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”"""
from itertools import permutations
integs = input('Enter 3 integers, seperated by commas').split(',')
integs = [int(ints) for ints in integs]
combs = list(permutations(integs, 3))
operators = ['+','-','*','/']
equal = '=='
canbe = False
for op in operators:
    for comb in combs:
        if eval(f'{comb[0]} {equal} {comb[1]} {op} {comb[2]}'):
            canbe = True
print(canbe)