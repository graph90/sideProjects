import math
def chainRule(x):
    if x < 0:
        return math.log(x + 1)
    elif x >= 0 and x < 1:
        return math.log(x + 2)
    else:
        return math.log(x + 3)
def main():
    x = float(input("Enter a value for x: "))
    y = chainRule(x)
    print("y =", y)
main()
