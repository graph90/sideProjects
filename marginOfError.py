import math
import matplotlib.pyplot as plt
import numpy as np
def marginOfError(criticalValue, standardDeviationOfStatistic):
    return criticalValue * standardDeviationOfStatistic
def main():
    criticalValue = 1.96
    standardDeviationOfStatistic = 0.05
    print("Margin of error: ", marginOfError(criticalValue, standardDeviationOfStatistic))
main()