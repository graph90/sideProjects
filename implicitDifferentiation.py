import math

def implicitDifferentiation(x):
    if x < 0:
        return 1 / (math.sqrt(x + 1) * (x + 1))
    elif x >= 0 and x < 1:
        return 1 / (math.sqrt(x + 2) * (x + 2))
    else:
        return 1 / (math.sqrt(x + 3) * (x + 3))
def main():
    x = float(input("Enter a value for x: "))
    y = implicitDifferentiation(x)
    print("y =", y)
main()
