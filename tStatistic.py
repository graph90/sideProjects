import math
import matplotlib.pyplot as plt
import numpy as np
def tStatistic(n, x, μx, s):
    return (x - μx) / (s / math.sqrt(n))
def main():
    n = 100
    x = 0.5
    μx = 0.5
    s = 0.05
    print("t statistic: ", tStatistic(n, x, μx, s))
main()