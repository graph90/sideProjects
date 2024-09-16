
def eulersEquation(V,E,F):
    if V==0:
        if E==0:
            if F==0:
                return "infinite solutions"
            else:
                return "no solutions"
        else:
            return 2*F/E
    elif E==0:
        if V==0:
            if F==0:
                return "infinite solutions"
            else:
                return "no solutions"
        else:
            return 2*F/V
    elif F==0:
        if V==0:
            if E==0:
                return "infinite solutions"
            else:
                return "no solutions"
        else:
            return V-E
    else:
        return 2*F/(V-E)
def main():
    V = 0
    E = 0
    F = 0
    x = eulersEquation(V,E,F)
    print(x)
main()
