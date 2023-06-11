# take user input and solve the intermediate value theorem using python
def solveIntermediateValueTheorem(x):
    if x < 0:
        return 2 * x ** 2 + 3 * x + 1
    elif x >= 0 and x < 1:
        return -x ** 2 + 1
    else:
        return x ** 2
def main():
    # get user input
    x = float(input("Enter a value for x: "))
    # solve the intermediate value theorem
    y = solveIntermediateValueTheorem(x)
    # print the result
    print("y =", y)
main()