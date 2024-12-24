'''Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution'''
def minmax(data):
    minel = data[0]
    maxel = data[0]
    for i in data:
        if i<minel:
            minel=i
        if i>maxel:
            maxel = i
    return tuple([minel,maxel])

print(minmax([3,5,1,6,8,3,5,78,33]))