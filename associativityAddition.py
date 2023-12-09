def associativityAddition(x, y, z):
    return (x + y) + z == x + (y + z)
def main():
    x = float(input("Enter a value for x: "))
    y = float(input("Enter a value for y: "))
    z = float(input("Enter a value for z: "))
    result = associativityAddition(x, y, z)
    print("Result =", result)
main()
