"""Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible."""

bills = [2000, 500, 100, 50]
coins = [20, 10, 5, 2, 1]

def makechange(amount):
    for bill in bills:
        if int(bill)<int(amount):
            times = (int(amount)//int(bill))
            amount = amount - (int(bill)*int(times))
            print(f"{bill} denomination notes * {times}")

    for coin in coins:
        if int(coin)<int(amount):
            times = int(coin) * (int(amount)//int(coin))
            amount = amount - (int(coin)*int(times))
            print(f"{coin} denomination coins * {times}")

makechange(6873)