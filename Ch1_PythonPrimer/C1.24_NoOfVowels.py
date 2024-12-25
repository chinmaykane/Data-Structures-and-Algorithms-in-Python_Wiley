"""Write a short Python function that counts the number of vowels in a given
character string"""
vows = ['a','e','i','o','u']
numbvows=0
stringg = input('Enter a string')
for i in stringg:
    if i in vows:
        numbvows +=1
print(numbvows)