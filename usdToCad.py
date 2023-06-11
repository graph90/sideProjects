# using a command line argument to convert USD to CAD and print to the console

import os
import sys
def main():
    # take USD as a command line argument and convert it to CAD and print to console
    if len(sys.argv) != 2:
        print('Usage: python usdToCad.py <amount in USD>')
        sys.exit(1)
    try:
        amount = float(sys.argv[1])
    except ValueError:
        print('Invalid amount')
        sys.exit(1)
    rate = 1.31
    print('CAD ' + str(amount * rate))
main()