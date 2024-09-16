
import math
def lagrangeRange(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                return "infinite solutions"
            else:
                return "no solutions"
        else:
            return -c/b
    else:
        d = (b**2)-(4*a*c)
        if d<0:
            return "no solutions"
        elif d==0:
            return -b/(2*a)
        else:
            x1 = (-b+math.sqrt(d))/(2*a)
            x2 = (-b-math.sqrt(d))/(2*a)
            return x1,x2
def main():
    a = 1
    b = 2
    c = 8
    x = lagrangeRange(a,b,c)
    print(x)
main()
