"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]."""
lits=[]
for i in range(10):
    lits.append(i*i+i)
print(lits)