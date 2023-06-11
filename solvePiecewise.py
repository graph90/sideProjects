# take the user input and solve the piecewise function
def solvePiecewise(x):
    if x < -2:
        return 4 * x + 5
    elif x >= -2 and x < 2:
        return -3 * x + 1
    else:
        return x / 2 - 1
def main():
    # get the user input
    x = float(input("Enter a value for x: "))
    # solve the piecewise function
    y = solvePiecewise(x)
    # print the result
    print("y =", y)
main()