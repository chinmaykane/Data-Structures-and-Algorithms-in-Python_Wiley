'''Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].'''
list1=[1]
for i in range(8): list1.append(int(list1[-1])*2)
print(list1)