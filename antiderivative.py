def f(x):
    return 2 * x ** 2 + 3 * x + 1
def antiDerivative(x):
    if x < 0:
        return x ** 3 + 3 * x ** 2 / 2 + x
    elif x >= 0 and x < 1:
        return -x ** 3 / 3 + x
    else:
        return x ** 3 / 3
def main():
    x = float(input("Enter a value for x: "))
    y = antiDerivative(x)
    print("y =", y)
main()
