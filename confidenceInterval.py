import math
import matplotlib.pyplot as plt
import numpy as np
def confidenceInterval(sampleStatistic, criticalValue, standardErrorOfStatistic):
    return sampleStatistic + criticalValue * standardErrorOfStatistic
def main():
    sampleStatistic = 0.5
    criticalValue = 1.96
    standardErrorOfStatistic = 0.05
    print("Confidence interval: ", confidenceInterval(sampleStatistic, criticalValue, standardErrorOfStatistic))
main()