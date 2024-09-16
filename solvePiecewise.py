
def solvePiecewise(x):
    if x < -2:
        return 4 * x + 5
    elif x >= -2 and x < 2:
        return -3 * x + 1
    else:
        return x / 2 - 1
def main():
    x = float(input("Enter a value for x: "))
    y = solvePiecewise(x)
    print("y =", y)
main()
