def shannonInformationTheory():
    entropy = float(input("Enter the entropy: "))
    bandwidth = float(input("Enter the bandwidth: "))
    shannonInformationTheory = entropy*bandwidth
    print("The Shannon Information Theory is: ", shannonInformationTheory)
def main():
    shannonInformationTheory()
main()
