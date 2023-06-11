# solve cubic equation in python
import math
def solveCubic(a,b,c,d):
    if a==0:
        if b==0:
            if c==0:
                if d==0:
                    return "infinite solutions"
                else:
                    return "no solutions"
            else:
                return -d/c
        else:
            return solveQuadratic(b,c,d)
    else:
        f = ((3*c/a)-(b**2/a**2))/3
        g = ((2*(b**3/a**3))-(9*b*c/a**2)+(27*d/a))/27
        h = (g**2/4)+(f**3/27)
        if f==0 and g==0 and h==0:
            return -b/(3*a)
        elif h<=0:
            i = math.sqrt((g**2/4)-h)
            j = i**(1/3)
            k = math.acos(-g/(2*i))
            L = -j
            M = math.cos(k/3)
            N = math.sqrt(3)*math.sin(k/3)
            P = -b/(3*a)
            x1 = 2*j*math.cos(k/3)-b/(3*a)
            x2 = L*(M+N)+P
            x3 = L*(M-N)+P
            return x1,x2,x3
        else:
            R = -(g/2)+math.sqrt(h)
            if R>=0:
                S = R**(1/3)
            else:
                S = -(abs(R)**(1/3))
            T = -(g/2)-math.sqrt(h)
            if T>=0:
                U = T**(1/3)
            else:
                U = -(abs(T)**(1/3))
            x1 = (S+U)-b/(3*a)
            return x1
def main():
    a = 1
    b = 2
    c = 3
    d = 4
    x = solveCubic(a,b,c,d)
    print(x)
main()