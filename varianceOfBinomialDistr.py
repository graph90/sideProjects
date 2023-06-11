import math
import matplotlib.pyplot as plt
import numpy as np
def binomialDistribution(n, p, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k)) * math.pow(p, k) * math.pow(1 - p, n - k)
def main():
    x = np.arange(0, 10, 0.01)
    y = []
    for i in x:
        y.append(binomialDistribution(10, 0.5, i))
    plt.plot(x, y)
    plt.show()
main()