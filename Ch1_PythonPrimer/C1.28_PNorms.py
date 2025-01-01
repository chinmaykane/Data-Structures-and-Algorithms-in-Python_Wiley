"""The p-norm of a vector v = (v1, v2, . . . , vn) in n-dimensional space is de-
fined as
‖v‖ = p
√
v p
1 + v p
2 + · · · + v p
n .
For the special case of p = 2, this results in the traditional Euclidean
norm, which represents the length of the vector. For example, the Eu-
clidean norm of a two-dimensional vector with coordinates (4, 3) has a
Euclidean norm of √42 + 32 = √16 + 9 = √25 = 5. Give an implemen-
tation of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers"""


def norm(*args):
    if len(args)==1:
        summ = 0
        for num in args[0]:
            summ = summ + int(num)**2
        result = summ**0.5
    else:
        summ = 0
        for num in args[0]:
            summ = summ + int(num)**int(args[1])
        result = summ**(1/(int(args[1])))
    return result

listofnums = [2,3,4,5]


print(norm(listofnums,4))


