
def main():
    p1 = float(input("Enter the probability of the first event: "))
    p2 = float(input("Enter the probability of the second event: "))
    p1g2 = float(input("Enter the probability of the first event given the second event: "))
    p2g1 = (p1g2 * p2) / p1
    print("The probability of the second event given the first event is", p2g1)
main()
