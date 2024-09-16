import math

def solveLinear(a,b):
    if a==0:
        if b==0:
            return "infinite solutions"
        else:
            return "no solutions"
    else:
        return -b/a
def main():
    a = 1
    b = 2
    x = solveLinear(a,b)
    print(x)
main()
