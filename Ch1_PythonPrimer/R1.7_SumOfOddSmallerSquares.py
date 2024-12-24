'''Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.'''
print(sum(i*i for i in range(10) if i % 2 == 0))