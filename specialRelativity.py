# python special relativity equation
def specialRelativity(v,c):
    if v==0:
        return 0
    elif v==c:
        return 1
    else:
        return (1-v**2/c**2)**(-1/2)
def main():
    v = 0
    c = 3*10**8
    x = specialRelativity(v,c)
    print(x)
main()