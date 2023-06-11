def fundamentalTheoremOfCalculus(a,b):
    if a==0:
        return b
    else:
        return (b**2)/(2*a)
def main():
    a = 1
    b = 2
    x = fundamentalTheoremOfCalculus(a,b)
    print(x)
main()