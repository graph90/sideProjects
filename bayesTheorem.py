# bayes theorem

def main():
    # get the probability of the first event
    p1 = float(input("Enter the probability of the first event: "))

    # get the probability of the second event
    p2 = float(input("Enter the probability of the second event: "))

    # get the probability of the first event given the second event
    p1g2 = float(input("Enter the probability of the first event given the second event: "))

    # calculate the probability of the second event given the first event
    p2g1 = (p1g2 * p2) / p1

    # display the probability of the second event given the first event
    print("The probability of the second event given the first event is", p2g1)

main()