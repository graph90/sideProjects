import os
import sys
def main():
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
