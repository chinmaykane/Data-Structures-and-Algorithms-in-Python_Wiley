"""Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1."""

elems = input('Enter no. of elements in arrays')
arr1 = (input('Enter array 1 of integers seperated with commas')).split(',')
arr2 = (input('Enter array 2 of integers seperated with commas')).split(',')
c=[]
if len(arr1) == len(arr2) == int(elems):
    for nth in range(int(elems)):
        c.append(int(arr1[nth])*int(arr2[nth]))
    print(c)
else:
    print('Error in input')


