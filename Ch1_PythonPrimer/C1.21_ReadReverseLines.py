"""Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D)."""
import sys
list=[]
while True:
    try:
        list.append(input('Type a line:'))
    except EOFError:
        list.reverse()
        for ele in list:
            print(ele, end=' ')
        break