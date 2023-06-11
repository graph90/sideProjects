def shannonInformationTheory():
    # get the entropy from the user
    entropy = float(input("Enter the entropy: "))
    # get the bandwidth from the user
    bandwidth = float(input("Enter the bandwidth: "))
    # calculate the Shannon Information Theory
    shannonInformationTheory = entropy*bandwidth
    # print the Shannon Information Theory
    print("The Shannon Information Theory is: ", shannonInformationTheory)
def main():
    shannonInformationTheory()
main()