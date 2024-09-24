
import math
def angleBetweenTwoLines(x1, y1, x2, y2):
    return math.degrees(math.atan2(y2 - y1, x2 - x1))
def main():
    x1 = float(input("Enter a value for x1: "))
    y1 = float(input("Enter a value for y1: "))
    x2 = float(input("Enter a value for x2: "))
    y2 = float(input("Enter a value for y2: "))
    angle = angleBetweenTwoLines(x1, y1, x2, y2)
    print("The angle between the two lines is: ", angle)
if __name__ == "__main__":
    main()