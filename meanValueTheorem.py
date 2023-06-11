def meanValueTheorem():
    # get user input
    a = float(input("Enter a value for a: "))
    b = float(input("Enter a value for b: "))
    c = float(input("Enter a value for c: "))
    # solve the mean value theorem
    y = (f(b) - f(a)) / (b - a)
    # print the result
    print("y =", y)
meanValueTheorem()