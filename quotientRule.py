def quotientRule(x):
    if x < 0:
        return 1 / (x - 2)
    elif x >= 0 and x < 1:
        return 1 / (x + 2)
    else:
        return 1 / (x - 1)
def main():
    # get user input
    x = float(input("Enter a value for x: "))
    # solve using the quotient rule
    y = quotientRule(x)
    # print the result
    print("y =", y)
main()