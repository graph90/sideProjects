import math
def solveProductRule(x):
    if x < 0:
        return math.sqrt(1 - x)
    elif x >= 0 and x < 1:
        return math.sqrt(1 + x)
    else:
        return math.sqrt(x)
def main():
    x = float(input("Enter a value for x: "))
    y = solveProductRule(x)
    print("y =", y)
main()
